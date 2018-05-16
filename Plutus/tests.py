# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
import httpretty
from unittest import mock
from google_hermes.views import GetDataFromGoogleMap

class TestHackerNewsService(TestCase):

    body = '{"destination_addresses" : [ "Petuniowa 9, 53-238 Wrocław, Poland" ],"origin_addresses" : [ "Osiedle Bolesława Śmiałego 38, Poznań, Poland" ],"rows" : [{"elements" : [{"distance" : {"text" : "184 km","value" : 184415},"duration" : {"text" : "2 hours 33 mins","value" : 9198},"status" : "OK"}]}],"status" : "OK" }'
 

def test_facebook_update(self):
    """
    Verifies that a successful Facebook update is correctly saved
    """
  
    fb_updater = GetDataFromGoogleMap()

    with mock.patch.object(GetDataFromGoogleMap, 'make_request') as mocked_method:
        mocked_method.return_value = {"destination_addresses" : [ "Petuniowa 9, 53-238 Wrocław, Poland" ],
                                        "origin_addresses" : [ "Osiedle Bolesława Śmiałego 38, Poznań, Poland" ],
                                        "rows" : [{"elements" : [{"distance" : {"text" : "184 km","value" : 184415},
                                        "duration" : {"text" : "2 hours 33 mins","value" : 9198},"status" : "OK"}]}],"status" : "OK"
                                    }
        
        # Note that specific verification of our URL and payload 
        # construction should still happen, just not in this 
        # particular unit test.
        response = fb_updater.make_request(38,'Osiedle Bolesława Śmiałego','Poznań','Wielkopolskie',9,'Petuniowa','Wrocław','Dolnośląskie')
        
        self.assertEqual(response, not None)
        # More assertions go here



#     @httpretty.activate
#     def test_get_headlines(self):
#         # mock for top stories
#         body = '{"destination_addresses" : [ "Petuniowa 9, 53-238 Wrocław, Poland" ],"origin_addresses" : [ "Osiedle Bolesława Śmiałego 38, Poznań, Poland" ],"rows" : [{"elements" : [{"distance" : {"text" : "184 km","value" : 184415},"duration" : {"text" : "2 hours 33 mins","value" : 9198},"status" : "OK"}]}],"status" : "OK" }'

#         httpretty.register_uri(
#             httpretty.GET,
#             "https://maps.googleapis.com/maps/api/distancematrix/json?origins=38,Osiedle Bolesława Śmiałego,Poznań,&destinations=9,Petuniowa,Wrocław,Dolnośląskie&key=AIzaSyDv16-NlXtPD2pgTyT6xGO3WbOV1bwOWTE",
#            body=self.body)

#         # mock for individual story item
#         # httpretty.register_uri(
#         #     httpretty.GET,
#         #     re.compile("https://hacker-news.firebaseio.com/v0/item/(w ).json"),
#         #     body="{"title":"some story title"}")

#         request = GetDataFromGoogleMap()
#         headlines = request.make_request(38,'Osiedle Bolesława Śmiałego','Poznań','Wielkopolskie',9,'Petuniowa','Wrocław','Dolnośląskie');
#         self.assertEqual(headlines,None)
#         # self.assertEqual(headlines,True)

#         # self.assertEqual(headlines,type(dict))
#         # self.assertEqual(headlines[0], 'some story title')
#         # last_request = httpretty.last_request()
#         # self.assertEqual(last_request.method, 'GET')
#         # self.assertEqual(last_request.path, '/v0/item/5.json')



{"destination_addresses" : [ "Petuniowa 9, 53-238 Wrocław, Poland" ],
"origin_addresses" : [ "Osiedle Bolesława Śmiałego 38, Poznań, Poland" ],
"rows" : [{"elements" : [{"distance" : {"text" : "184 km","value" : 184415},
"duration" : {"text" : "2 hours 33 mins","value" : 9198},"status" : "OK"}]}],"status" : "OK"
}
