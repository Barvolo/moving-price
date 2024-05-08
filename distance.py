import requests
import json

def get_osrm_distance(source, destination):
    """ Calculate driving distance using OSRM public API. """
    osrm_route_url = f"http://router.project-osrm.org/route/v1/car/{source};{destination}"
    response = requests.get(osrm_route_url)
    routes = json.loads(response.text)
    
    # Check if valid routes are available
    if routes['code'] == 'Ok':
        distance = routes['routes'][0]['distance'] / 1000  # Convert meters to kilometers
        return distance
    else:
        return None


