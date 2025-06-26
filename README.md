# Aigeon AI Property Report

## Project Description

The `aigeon-ai.property-report` is a Python-based server application designed to interact with a property records search API. It provides functionality to retrieve detailed property reports based on address and optional owner information. This application leverages the FastMCP framework to facilitate communication with external APIs, ensuring secure and efficient data retrieval.

## Features Overview

- **Property Report Retrieval**: Fetch comprehensive property reports using address details and optional owner information.
- **OAuth Authentication**: Secure API access using OAuth token-based authentication.
- **FastMCP Integration**: Utilizes the FastMCP framework for streamlined server operations and API interactions.
- **JSON Payload Handling**: Constructs and sends JSON payloads for API requests, ensuring proper data formatting.

## Main Features and Functionality

1. **Get Property Report**: The core functionality of the application is to retrieve property reports based on provided address and owner details. This is achieved through a well-defined function that communicates with an external API.

2. **Token Management**: The application implements a mechanism to manage OAuth tokens, ensuring that API requests are authenticated and tokens are refreshed as needed.

3. **API Communication**: Utilizes HTTP connections to send requests and receive responses from the property report API, handling JSON data for both requests and responses.

## Main Functions Description

### `GetReport`

This function is the primary tool for fetching property reports. It requires specific parameters to be provided:

- **Addr1**: (str) The street address of the property.
- **City**: (str) The city where the property is located.
- **StateProv**: (str) The two-letter state code (e.g., CA for California) of the property.
- **PostalCode**: (str) The zip code of the property.
- **FirstName**: (Optional[str]) The first name of the property owner.
- **LastName**: (Optional[str]) The last name of the property owner.

#### Functionality

- **Token Verification and Refresh**: Checks if the current OAuth token is valid or needs to be refreshed. If expired, it requests a new token using client credentials.
- **API Request Construction**: Constructs a JSON payload with the provided address and owner information.
- **API Request Execution**: Sends the constructed request to the property report API and processes the response.
- **Response Handling**: Returns the property report data if the request is successful, or an empty dictionary if an error occurs.

This function is integral to the application, enabling users to obtain detailed property information efficiently and securely.