from rewiser.utils import md_to_html, check_val
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
        subject: str | None = None,
        smtp_hostname: str | None = None,
        smtp_port: int | None = None,
        smtp_username: str | None = None,
        smtp_password: str | None = None,
    ) -> None:
        self.body = body
        self.to = check_val(to, "TO_EMAIL")
        self.frm = check_val(frm, "FROM_EMAIL")
        self.subject = check_val(subject, "SUBJECT") or "Rewiser Email"
        self.smtp_hostname = check_val(smtp_hostname, "SMTP_HOSTNAME")
        self.smtp_port = check_val(smtp_port, "SMTP_PORT")
        self.smtp_username = check_val(smtp_username, "SMTP_USERNAME")
        self.smtp_password = check_val(smtp_password, "SMTP_PASSWORD")

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
