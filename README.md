# Ramin's Geolocation Utility

## Overview

This project I created includes a Python utility for fetching geolocation data using the OpenWeatherMap Geocoding API. The utility retrieves latitude and longitude for cities, states, and zip codes. Also, I included a testing script to verify the functionality of the utility.

## Files

1. **`ramingeoloc_util.py`**: The main utility script that interfaces with the OpenWeatherMap Geocoding API.
2. **`test_geo.py`**: The testing script that verifies the functionality of `ramingeoloc_util.py`.

## Setup

### Prerequisites

- Python version 3 and above
- `requests` library (for making HTTP requests)

You can install the necessary Python library using pip: pip install requests

## Usage

To run the geolocation utility, execute the following command: python ramingeoloc_util.py --locations "City, State" "ZipCode"
So for example: python ramingeoloc_util.py --locations "Madison, WI" "12345" "Chicago, IL" "10001"
This command will print the geolocation data (name, state, latitude, and longitude) for the specified locations.

## Testing

To run the tests for the utility, execute the following command: python test_geo.py
This command will run a series of tests to ensure that ramingeoloc_util.py works correctly with valid inputs, invalid inputs, and edge cases.

## Test Cases

For transparency, ramingeoloc_util.py script includes these test scenarios: valid and invalid inputs, empty inputs, single city and zip code, and multiple locations.

## Example Output

When running the utility with valid inputs, the output might look like this:
Place: Madison, WI
Latitude: 43.0731, Longitude: -89.4012

Place: 12345
Latitude: 40.7500, Longitude: -73.9800

Place: Chicago, IL
Latitude: 41.8781, Longitude: -87.6298

Place: 10001
Latitude: 40.7527, Longitude: -73.9772






