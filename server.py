import json

import requests
from datetime import datetime, timedelta
from typing import Union
from mcp.server import FastMCP
from pydantic import Field
from typing import Annotated
from mcp.server.fastmcp import FastMCP
from fastmcp import FastMCP, Context
import os
from dotenv import load_dotenv
load_dotenv()
microbilt_client_id = os.getenv("MICROBILT_CLIENT_ID")
microbilt_client_secret = os.getenv("MICROBILT_CLIENT_SECRET")
rapid_api_key = os.getenv("RAPID_API_KEY")
import http.client

__rapidapi_url__ = 'https://rapidapi.com/IgorMicrobilt/api/property-report'

mcp = FastMCP('property-records-search')

token = None
token_time = None
expiration = None

@mcp.tool()
def GetReport(Addr1: Annotated[str, Field(description='Street address of the property')],
              City: Annotated[str, Field(description='City of the property')],
              StateProv: Annotated[str, Field(description='State of the property in two letters, e.g. CA for California')],
              PostalCode: Annotated[str, Field(description='Zip code of the property')],
              FirstName: Annotated[Union[str, None], Field(description='Property owner\'s first name')] = None,
              LastName: Annotated[Union[str, None], Field(description='Property owner\'s last name')] = None):
    '''Get property report by address and owner name'''
    global token, token_time, expiration
    if token is None or datetime.now() - timedelta(seconds=expiration) > token_time:
        url = "https://apitest.microbilt.com/OAuth/Token"

        headers = {
            "Content-Type": "application/json"
        }

        data = {
            "client_id": microbilt_client_id,
            "client_secret": microbilt_client_secret,
            "grant_type": "client_credentials"
        }
        response = requests.post(url, headers=headers, json=data)
        if response.status_code != 200:
            return {}
        response_data = response.json()
        token = response_data.get('access_token')
        token_time = datetime.now()
        expiration = int(response_data.get('expires_in', 3600)) - 60

    conn = http.client.HTTPSConnection("property-report.p.rapidapi.com")

    payload = {"OwnerInfo":{"PersonName":{"FirstName":FirstName,"LastName": LastName}},"PropertyAddress":{"Addr1":Addr1,"City":City,"StateProv":StateProv,"PostalCode":PostalCode}}
    payload = json.dumps(payload)

    headers = {
        'x-rapidapi-key': rapid_api_key,
        'x-rapidapi-host': "property-report.p.rapidapi.com",
        'Content-Type': "application/json",
        'Authorization': f"Bearer {token}",
        'Accept': "application/json"
    }

    conn.request("POST", "/GetReport", payload, headers)

    res = conn.getresponse()
    data = res.read()
    if res.status != 200:
        return {}
    return data.decode("utf-8")


if __name__ == "__main__":
    mcp.run(transport="stdio")