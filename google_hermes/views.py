from django.shortcuts import render
#from urllib.request import urlopen
import requests
import json

# Create your views here.


class GetDataFromGoogleMap:

    def send_request_maps_api(self, source_no, source_street, source_city,
                              source_district, end_no, end_street, end_city, end_district):
        google_api_key = 'AIzaSyDv16-NlXtPD2pgTyT6xGO3WbOV1bwOWTE'
        url = 'https://maps.googleapis.com/maps/api/distancematrix/json?origins=' + \
            source_no + ',' + source_street + ',' + source_city + ',' + \
            source_district + '&destinations=' + end_no + ',' + end_street + ',' + end_city + \
            ',' + end_district + '&key=' + google_api_key

        json_string = requests.get(url)
        json_data = json_string.json()

        print(json_data['rows'][0]['elements'][0]['distance']['text'])
