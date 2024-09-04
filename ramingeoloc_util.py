import requests
import argparse

API_KEY = 'f897a99d971b5eef57be6fafa0d83239'

def get_coordinates_by_city_state(city, state):
    url = f'http://api.openweathermap.org/geo/1.0/direct?q={city},{state},US&limit=1&appid={API_KEY}'
    response = requests.get(url)
    if response.status_code == 200 and response.json():
        data = response.json()[0]
        return {
            'name': data.get('name'),
            'state': data.get('state'),
            'country': data.get('country'),
            'lat': data.get('lat'),
            'lon': data.get('lon')
        }
    else:
        return {'error': 'Location not found or API error'}

def get_coordinates_by_zip(zip_code):
    url = f'http://api.openweathermap.org/geo/1.0/zip?zip={zip_code},US&appid={API_KEY}'
    response = requests.get(url)
    if response.status_code == 200 and response.json():
        data = response.json()
        return {
            'name': data.get('name'),
            'state': data.get('state'),
            'country': data.get('country'),
            'lat': data.get('lat'),
            'lon': data.get('lon')
        }
    else:
        return {'error': 'Location not found or API error'}

def main(locations):
    results = []
    for loc in locations:
        if ',' in loc:
            city, state = map(str.strip, loc.split(','))
            result = get_coordinates_by_city_state(city, state)
        else:
            result = get_coordinates_by_zip(loc)
        results.append(result)
    
    for res in results:
        print(f"Place: {res.get('name', 'N/A')}, State: {res.get('state', 'N/A')}")
        print(f"Latitude: {res.get('lat', 'N/A')}, Longitude: {res.get('lon', 'N/A')}\n")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Get geolocation data for cities or zip codes.')
    parser.add_argument('--locations', nargs='+', required=True, help='List of locations (e.g., "Madison, WI" "12345")')
    args = parser.parse_args()
    main(args.locations)
