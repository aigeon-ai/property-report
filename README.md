# Aigeon AI Property Report

## Project Description

The `aigeon-ai.property-report` project is a Python-based server application designed to retrieve detailed property reports using address and optional owner information. It leverages the Microbilt API to access property records, providing users with comprehensive data about properties in the United States. This application is built on the FastMCP framework, which facilitates efficient microservice communication.

## Features Overview

- **Property Report Retrieval**: Fetches detailed property information using specified address details and optional owner names.
- **OAuth Token Management**: Implements secure OAuth token handling to authenticate API requests.
- **Microservice Architecture**: Utilizes FastMCP for streamlined microservice operations.
- **RapidAPI Integration**: Connects to the RapidAPI platform for accessing the property report API.

## Main Features and Functionality

1. **Get Property Report**: The core functionality of this application is to obtain a property report by providing the street address, city, state, and postal code. Users can also include the property owner's first and last name to refine the search.

2. **OAuth Token Handling**: The application manages OAuth tokens to authenticate requests to the Microbilt API. It checks the token's validity and refreshes it as needed to ensure seamless API communication.

3. **API Request Construction**: Constructs and sends HTTP requests to the property report API, handling JSON payloads and headers to ensure proper communication and data retrieval.

4. **Error Handling**: Implements basic error handling to manage unsuccessful API responses, returning an empty dictionary when errors occur.

## API Endpoints or Main Functions Description

### `GetReport`

- **Description**: Fetches a property report based on the provided address and optional owner information.
- **Parameters**:
  - `Addr1` (str): Street address of the property.
  - `City` (str): City where the property is located.
  - `StateProv` (str): State of the property in two-letter format (e.g., CA for California).
  - `PostalCode` (str): Zip code of the property.
  - `FirstName` (Union[str, None], optional): First name of the property owner.
  - `LastName` (Union[str, None], optional): Last name of the property owner.
- **Returns**: A JSON string containing the property report data if successful, or an empty dictionary if an error occurs.

### OAuth Token Management

- **Functionality**: The application checks if the current OAuth token is valid. If expired or not present, it requests a new token from the Microbilt OAuth service using client credentials.

### FastMCP Integration

- **Functionality**: The application is structured as a microservice using FastMCP, allowing it to run efficiently and communicate over standard input/output.

This project is ideal for users needing detailed property information for real estate analysis, legal purposes, or personal interest. By leveraging modern API and microservice technologies, it provides a robust solution for accessing property data.