# Aigeon AI Property Report

## Project Description

Aigeon AI Property Report is a Python-based server application designed to fetch detailed property reports using specific address and owner information. The application leverages the FastMCP framework to provide a streamlined and efficient mechanism for retrieving property data from external APIs.

## Features Overview

- **Property Report Retrieval**: The core functionality of this application is to obtain comprehensive property reports based on user-provided address details and optional owner information.
- **OAuth2 Authentication**: Secure token-based authentication is implemented to access the external API services.
- **RapidAPI Integration**: Utilizes the RapidAPI platform to interface with the property report service.
- **Efficient Token Management**: Implements a caching mechanism to store and manage authentication tokens, minimizing unnecessary API calls.

## Main Features and Functionality

1. **Get Property Report**: The primary function `GetReport` allows users to fetch property reports by providing the street address, city, state, postal code, and optionally, the property owner's first and last names.
2. **Authentication Handling**: The application manages OAuth2 token generation and renewal, ensuring secure and efficient access to the property report API.
3. **Data Serialization**: Input data is serialized into JSON format for compatibility with the API requirements.
4. **Error Handling**: Basic error handling is implemented to manage unsuccessful API responses gracefully.

## Main Functions Description

### `GetReport`

- **Purpose**: Fetches a detailed property report based on the provided address and optional owner information.
- **Parameters**:
  - `Addr1` (str): Street address of the property.
  - `City` (str): City where the property is located.
  - `StateProv` (str): State abbreviation (e.g., CA for California).
  - `PostalCode` (str): Zip code of the property.
  - `FirstName` (Union[str, None], optional): First name of the property owner.
  - `LastName` (Union[str, None], optional): Last name of the property owner.
- **Returns**: A JSON string containing the property report data if the request is successful; otherwise, an empty dictionary.
- **Implementation Details**:
  - Checks if the current authentication token is valid; if not, it requests a new token using client credentials.
  - Constructs a JSON payload with the provided parameters and sends a POST request to the property report API.
  - Handles the API response, decoding the data if the request is successful.

This application is designed to be run as a standalone server, utilizing the FastMCP framework to handle communication and processing tasks efficiently. The integration with external APIs is abstracted to provide a seamless experience for users seeking property information.