from langchain.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field
from typing import List


class PersonIntel(BaseModel):
    """
    A class for how the output of llm will look like
    """

    summary: str = Field(description="Summary of the person")
    facts: List[str] = Field(description="Interesting Facts about the person")
    topic_of_interest: List[str] = Field(
        description="Topic that may interest the person"
    )
    ice_breaker: List[str] = Field(
        description="Create Ice breakers to open the conversation with person"
    )

    def to_dict(self):
        return {
            "summary": self.summary,
            "facts": self.facts,
            "ice_breakers": self.ice_breakers,
            "topics_of_interest": self.topics_of_interest,
        }


person_intel_parser: PydanticOutputParser = PydanticOutputParser(
    pydantic_object=PersonIntel
)
