import os
import requests


def scrape_linkedin_profile(linkedin_profile_url: str):
    """
    scrape information from linkedin Profiles,
    Manually scrape the information from the LinkedIn profile
    """
    api_endpoint = "https://nubela.co/proxycurl/api/v2/linkedin"
    header_dic = {"Authorization": f'Bearer {os.environ.get("PROXYCURL_API_KEY")}'}

    response = requests.get(
        api_endpoint, params={"url": linkedin_profile_url}, headers=header_dic
    )

    # response = requests.get(
    #     "https://gist.githubusercontent.com/harshwalia36/6d426cb9585aaa013ba7dc82efd18339/raw/a5f8fd2aa144d75022889cde587e67bfecb80280/harsh_walia.json"
    # )
    data = response.json()

    data = {
        k: v
        for k, v in data.items()
        if v not in ([], "", "", None)
        and k not in ["people_also_viewed", "certifications"]
    }
    if data.get("groups"):
        for group_dict in data.get("groups"):
            group_dict.pop("profile_pic_url")

    return data
