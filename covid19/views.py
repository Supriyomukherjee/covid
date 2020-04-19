import requests
from django.shortcuts import render
from urllib.request import urlopen
import json
####
def home(request):
        d=[]

        url = "https://coronavirus-monitor.p.rapidapi.com/coronavirus/cases_by_particular_country.php"

        querystring = {"country":"India"}

        headers = {
            'x-rapidapi-host': "coronavirus-monitor.p.rapidapi.com",
            'x-rapidapi-key': "1c0fc11dfbmsha8931aca0d57d43p1007d5jsn6df6558e3f52"
            }

        response = requests.request("GET", url, headers=headers, params=querystring).json()
        d = response['stat_by_country']
        context={
                'total_cases':d[-1]['total_cases'],
                'new_cases':d[-1]['new_cases'],
                'active_cases':d[-1]['active_cases'],
                'total_deaths':d[-1]['total_deaths'],
                'total_recovered':d[-1]['total_recovered'],
                'total_tests':d[-1]['total_tests'],
                'record_date':d[-1]['record_date']
        }
        return render(request,"index.html",context)
