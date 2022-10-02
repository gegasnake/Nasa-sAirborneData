from django.db.models import CharField
from django.db.models.functions import Cast, TruncSecond, ExtractMonth
from django.shortcuts import render
from django.template.response import TemplateResponse
from django.views import View
from .models import Data

class NasaHomeView(View):
    template_name = 'delta_app/home.html'

    def get(self, request):
        return render(request, 'delta_app/home.html')

    def post(self, request):
        return render(request, 'delta_app/home.html')


class DataListView(View):

    def get(self, request):
        data_list = []
        data = Data.objects.annotate(
            date_str=Cast('date', CharField()),
            time_str=Cast('time', CharField()),
            month=ExtractMonth('date'),
        ).values('id', 'latitude', 'longitude', 'date_str', 'time_str',
                 'turbidity', 'salinity', 'temperature', 'month'
        ).all()

        for d in data:
            data_list.append(d)

        return TemplateResponse(request, 'delta_app/data_info.html', context={'data': data_list})
