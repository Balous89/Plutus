from django.shortcuts import render
# from urllib.request import urlopen
import requests
import json

# Create your views here.


class GetDataFromGoogleMap:

    def make_request(self, source_no, source_street, source_city,
                     source_district, end_no, end_street, end_city, end_district):
        try:
            google_api_key = 'AIzaSyDv16-NlXtPD2pgTyT6xGO3WbOV1bwOWTE'
            url = 'https://maps.googleapis.com/maps/api/distancematrix/json?origins=' + \
                source_no + ',' + source_street + ',' + source_city + ',' + \
                source_district + '&destinations=' + end_no + ',' + end_street + ',' + end_city + \
                ',' + end_district + '&key=' + google_api_key

            json_from_google_api = requests.get(url)
            json_data = json_from_google_api.json()

            distance_from_google = json_data['rows'][0]['elements'][0]['distance']['text'].replace(
                'km', '')
            origin_street_from_google = json_data['origin_addresses'][0].split(',')[0]
            origin_city_from_google = json_data['origin_addresses'][0].split(',')[1]

            destination_street_from_google = json_data['destination_addresses'][0].split(',')[0]
            destination_city_from_google = json_data['destination_addresses'][0].split(',')[1]

            return(origin_street_from_google, origin_city_from_google, destination_street_from_google,
                   destination_city_from_google, float(distance_from_google))
        except Exception as e:
            print('Error' + str(e))
