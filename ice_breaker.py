import os
import openai
from langchain import PromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain
from dotenv import load_dotenv, find_dotenv
from typing import Tuple

from third_parties.linkedin import scrape_linkedin_profile
from agents.linkedin_lookup_agent import lookup as linkedin_lookup_agent
from output_parser import person_intel_parser
from output_parser import PersonIntel


_ = load_dotenv(find_dotenv())  # read local .env file
openai.api_key = os.environ["OPENAI_API_KEY"]
serpapi_api_key = os.environ["SERPAPI_API_KEY"]


def ice_break(name: str) -> Tuple[PersonIntel,str]:
    summary_template = """
        given the information {information} about a person from I want you to create:
        1. a short summary
        2. two interesting facts about them.
        3. A topic that may interest them
        4. 2 creative Ice breakers to open a conversation with them {format_instructions}
"""

    summary_prompt_template = PromptTemplate(
        input_variables=["information"],
        template=summary_template,
        partial_variables={
            "format_instructions": person_intel_parser.get_format_instructions()
        },
    )

    llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")

    chain = LLMChain(llm=llm, prompt=summary_prompt_template)

    linkedin_profile_url = linkedin_lookup_agent(name=name)
    print(linkedin_profile_url)

    linkedin_data = scrape_linkedin_profile(
        linkedin_profile_url=linkedin_profile_url
    )

    print(linkedin_data)

    result = chain.run(information=linkedin_data)
    return person_intel_parser.parse(result),linkedin_data.get("profile_pic_url")


if __name__ == "__main__":
    print("hello langchain")

    result = ice_break(name="Harsh Walia Data Scientist")
    print(type(result))
    print(result)
