from django.shortcuts import render
from django.views import View
from django.http import JsonResponse
from .forms import TransitRouteForm
from .models import TransitRouteModel
from django.utils.translation import ugettext as _
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from google_hermes.views import GetDataFromGoogleMap


# Create your views here.


class GetTransitPoints(View):

    @method_decorator(login_required)
    def get(self, request):

        transit_points_form = TransitRouteForm()
        all_routs = TransitRouteModel.objects.all()

        # filter(date__range=[request.transit_points_form.filter_date_from,
        #                                                           request.transit_points_form.filter_date_to])
        context = {'transit_points_form': list(transit_points_form),
                   'all_routs': all_routs,
                   }
        return render(request, 'scribe/transitrouteform.html',
                      context)
    @method_decorator(login_required)    
    def post(self, request):

        transit_points_form = TransitRouteForm(request.POST)
        try:
            if transit_points_form.is_valid():
                print('is valid')
                posted_transit_points_form = transit_points_form.save(commit=False)
                print('Numer'+ transit_points_form.cleaned_data.get('origin_number'))
                get_data_from_google_api = GetDataFromGoogleMap()
                posted_transit_points_form.origin_street,\
                posted_transit_points_form.origin_city,\
                posted_transit_points_form.destination_street,\
                posted_transit_points_form.destination_city,\
                posted_transit_points_form.distance_in_km = get_data_from_google_api.make_request(
                                                            transit_points_form.cleaned_data.get('origin_number'),
                                                            posted_transit_points_form.origin_street,
                                                            posted_transit_points_form.origin_city,
                                                            posted_transit_points_form.origin_district,
                                                            transit_points_form.cleaned_data.get('destination_number'),
                                                            posted_transit_points_form.destination_street,
                                                            posted_transit_points_form.destination_city,
                                                            posted_transit_points_form.destination_district)
                

                posted_transit_points_form.paycheck_for_route = posted_transit_points_form.distance_in_km * 1#\
                #     #posted_transit_points_form.pln_per_km

                posted_transit_points_form.save()
                

                data = {'frome': 'Z',
                        'origin_street': posted_transit_points_form.origin_street,
                        'origin_city': posted_transit_points_form.origin_city,
                        'origin_district': posted_transit_points_form.origin_district,
                        'to': 'DO',
                        'destination_street': posted_transit_points_form.destination_street,
                        'destination_city': posted_transit_points_form.destination_city,
                        'destination_district': posted_transit_points_form.destination_district,
                        'transit_date': posted_transit_points_form.transit_date,
                        'distance_in_km': posted_transit_points_form.distance_in_km,
                        'paycheck_for_route': posted_transit_points_form.paycheck_for_route}

            else:
                if transit_points_form.errors:
                    data = {'form_errors': transit_points_form.errors}
                print(data)
        except Exception as e:
            data = {'adress_error': _(
                'Entered address is invalid. Please check your data.')}
            print('Error' + str(e))

        return JsonResponse(data)
