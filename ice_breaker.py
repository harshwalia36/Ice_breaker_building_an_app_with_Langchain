import os
import openai
from langchain import PromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain
from dotenv import load_dotenv, find_dotenv

from third_parties.linkedin import scrape_linkedin_profile
from agents.linkedin_lookup_agent import lookup as linkedin_lookup_agent


_ = load_dotenv(find_dotenv()) # read local .env file
openai.api_key = os.environ['OPENAI_API_KEY']
serpapi_api_key = os.environ['SERPAPI_API_KEY']

information="""
Elon Reeve Musk (/ˈiːlɒn/ EE-lon; born June 28, 1971) is a business magnate and investor. Musk is the founder, chairman, CEO and chief technology officer of SpaceX; angel investor, CEO, product architect and former chairman of Tesla, Inc.; owner, chairman and CTO of X Corp.; founder of the Boring Company; co-founder of Neuralink and OpenAI; and president of the Musk Foundation. He is the wealthiest person in the world, with an estimated net worth of US$226 billion as of September 2023, according to the Bloomberg Billionaires Index, and $249 billion according to Forbes, primarily from his ownership stakes in both Tesla and SpaceX.
"""


if __name__== '__main__':
    print("hello langchain")
    
    summary_template = """
        given the information {information} about a person from I want you to create:
        1. a short summary
        2. two interesting facts about them.
"""


    summary_prompt_template = PromptTemplate(input_variables=["information"], template=summary_template)

    llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")

    chain= LLMChain(llm=llm,prompt=summary_prompt_template)

    linkedin_profile_url=linkedin_lookup_agent(name="Harsh Walia Data Scientist")
    print(linkedin_profile_url)
    linkedin_data = scrape_linkedin_profile(linkedin_profile_url="https://www.linkedin.com/in/harsh-walia-32b968172")

    print(chain.run(information=linkedin_data))

    

    