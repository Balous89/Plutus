# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
import httpretty
from unittest import mock
from google_hermes.views import GetDataFromGoogleMap

class TestGetDataFromGoogleMap:

    #body = '{"destination_addresses" : [ "Petuniowa 9, 53-238 Wrocław, Poland" ],"origin_addresses" : [ "Osiedle Bolesława Śmiałego 38, Poznań, Poland" ],"rows" : [{"elements" : [{"distance" : {"text" : "184 km","value" : 184415},"duration" : {"text" : "2 hours 33 mins","value" : 9198},"status" : "OK"}]}],"status" : "OK" }'
 

    def test_make_request(self):
        request_klass = GetDataFromGoogleMap()

        with mock.patch.object(GetDataFromGoogleMap, 'make_request') as mocked_method:
            mocked_method.return_value = {"destination_addresses" : [ "Petuniowa 9, 53-238 Wrocław, Poland" ],
                                            "origin_addresses" : [ "Osiedle Bolesława Śmiałego 38, Poznań, Poland" ],
                                            "rows" : [{"elements" : [{"distance" : {"text" : "184 km","value" : 184415},
                                            "duration" : {"text" : "2 hours 33 mins","value" : 9198},"status" : "OK"}]}],"status" : "OK"
                                        }
            
       
            response = request_klass.make_request(38,'Osiedle Bolesława Śmiałego','Poznań','Wielkopolskie',9,'Petuniowa','Wrocław','Dolnośląskie')
            
        assert response['rows'][0]['elements'][0]['distance']['text'] == "184 km"
 