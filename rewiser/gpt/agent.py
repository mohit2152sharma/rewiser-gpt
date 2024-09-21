import logging
import traceback

from langchain import LLMChain, PromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.llms import OpenAI
from langchain.prompts.chat import ChatPromptValue

from rewiser.gpt.utils import create_prompt_template
from rewiser.utils import read_env_var


class OpenAIAgent:
    def __init__(self, template_name: str, openai_key: str | None = None) -> None:
        self.openai_key = openai_key or read_env_var("OPENAI_API_KEY", raise_error=True)
        self.llm = ChatOpenAI(openai_api_key=self.openai_key, model="gpt-4o")  # type: ignore
        self.template_name = template_name

    def create_template(self) -> PromptTemplate:
        return create_prompt_template(template_name=self.template_name)

    def run(self, input_text: str) -> str:
        template = self.create_template()
        llm_chain = LLMChain(prompt=template, llm=self.llm)
        resp = ""
        if input_text:
            logging.info(f"generating question for input text: {input_text}")
            try:
                resp = llm_chain.run(input_text=input_text)
            except ConnectionError:
                logging.error(
                    f"Unable to generate question. Full traceback: {traceback.format_exc()}"
                )
        else:
            try:
                resp = llm_chain.run()
            except ConnectionError:
                logging.error(
                    f"Unable to generate question. Full traceback: {traceback.format_exc()}"
                )

        logging.info("question generated")

        resp = resp.strip()
        return resp
