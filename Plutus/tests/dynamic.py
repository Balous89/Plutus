import django


from django.http import HttpRequest
from scribe.views import home_page



request = HttpRequest()
response = home_page(request)
html = response.getvalue()
print(type(html))



google_api_key = 'AIzaSyDv16-NlXtPD2pgTyT6xGO3WbOV1bwOWTE'
            url = 'https://maps.googleapis.com/maps/api/distancematrix/json?origins=38,Osiedle Bolesława Śmiałego,Poznań,&destinations=9,Petuniowa,Wrocław,Dolnośląskie&key=AIzaSyDv16-NlXtPD2pgTyT6xGO3WbOV1bwOWTE'


Petuniowa 9 53-238 Wrocław Dolnośląskie

Osiedle Bolesława Śmiałego 38 Poznań Wielkopolskie
            + \
                source_no + ',' + source_street + ',' + source_city + ',' + \
                source_district + '&destinations=' + end_no + ',' + end_street + ',' + end_city + \
                ',' + end_district + '&key=AIzaSyDv16-NlXtPD2pgTyT6xGO3WbOV1bwOWTE