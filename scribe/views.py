from django.shortcuts import render
from django.views import View
from .forms import TransitRouteForm
from .models import TransitRouteModel

# Create your views here.


class GetTransitPoints(View):

    def get(self, request):
        transit_points_form = TransitRouteForm()
        all_rides = TransitRouteModel.objects.all()

        # filter(date__range=[request.transit_points_form.filter_date_from,
        #                                                           request.transit_points_form.filter_date_to])
        context = {'transit_points_form': transit_points_form,
                   'all_rides': all_rides}
        return render(request, 'scribe/transitrouteform.html',
                      context)

    def post(self, request):
        pass
