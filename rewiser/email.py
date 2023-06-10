from utils import md_to_html, read_env_var, smtp_creds
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import ssl
import smtplib


class Emailer:
    def __init__(
        self,
        body: str,
        to: str | None = None,
        frm: str | None = None,
        subject: str = "Rewiser Email",
        smtp_hostname: str | None = None,
        smtp_port: int | None = None,
        smtp_username: str | None = None,
        smtp_password: str | None = None,
    ) -> None:
        self.body = body
        self.to = to if to else read_env_var("TO_EMAIL")
        self.frm = frm if frm else read_env_var("FROM_EMAIL")
        self.subject = subject
        (
            self.smtp_hostname,
            self.smtp_port,
            self.smtp_username,
            self.smtp_password,
        ) = smtp_creds(
            smtp_hostname=smtp_hostname,
            smtp_port=smtp_port,
            smtp_username=smtp_username,
            smtp_password=smtp_password,
        )

    def create_email(self) -> MIMEMultipart:
        message = MIMEMultipart("alternative")
        message["Subject"] = self.subject
        message["To"] = self.to
        message["From"] = self.frm

        html = md_to_html(self.body)
        part1 = MIMEText(html, "html")
        part2 = MIMEText(self.body, "text")

        message.attach(part1)
        message.attach(part2)
        return message

    def send_email(self) -> None:
        message = self.create_email()
        context = ssl.create_default_context()
        with smtplib.SMTP(self.smtp_hostname, self.smtp_port) as server:
            server.starttls(context=context)
            server.login(self.smtp_username, self.smtp_password)
            server.sendmail(self.frm, self.to, message.as_string())

        return None
