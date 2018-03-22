from django.shortcuts import render
from django.views import View
from django.http import JsonResponse
from .forms import TransitRouteForm
from .models import TransitRouteModel
from google_hermes.views import GetDataFromGoogleMap

# Create your views here.


class GetTransitPoints(View):

    def get(self, request):
        transit_points_form = TransitRouteForm()
        all_routs = TransitRouteModel.objects.all()

        # filter(date__range=[request.transit_points_form.filter_date_from,
        #                                                           request.transit_points_form.filter_date_to])
        context = {'transit_points_form': transit_points_form,
                   'all_routs': all_routs}

        return render(request, 'scribe/transitrouteform.html',
                      context)

    def post(self, request):
        transit_points_form = TransitRouteForm(request.POST)
        if transit_points_form.is_valid():
            posted_transit_points_form = transit_points_form.save(commit=False)
            get_data_from_google_api = GetDataFromGoogleMap()
            posted_transit_points_form.distance_in_km = get_data_from_google_api.make_request(posted_transit_points_form.source_adress_number,
                                                                                              posted_transit_points_form.source_adress_street,
                                                                                              posted_transit_points_form.source_adress_city,
                                                                                              posted_transit_points_form.source_adress_district,
                                                                                              posted_transit_points_form.endpoint_adress_number,
                                                                                              posted_transit_points_form.endpoint_adress_street,
                                                                                              posted_transit_points_form.endpoint_adress_city,
                                                                                              posted_transit_points_form.endpoint_adress_district)

            posted_transit_points_form.paycheck_for_route = posted_transit_points_form.distance_in_km * \
                posted_transit_points_form.pln_per_km

            posted_transit_points_form.save()
        print('OK')
        return JsonResponse({'data': True, 'posted_transit_points_form.distance_in_km': posted_transit_points_form.distance_in_km})
