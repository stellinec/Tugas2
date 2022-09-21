from django.shortcuts import render
from mywatchlist.models import MyWatchedList
from django.http import HttpResponse
from django.core import serializers
# Create your views here.
data_watchlist = MyWatchedList.objects.all()

context = {
    'watchlist': data_watchlist,
    'nama' : 'Stelline Claudia',
    'id' : '2106700933'

}
def show_watchlist(request):
    return render(request, "watchlist.html", context)
def show_xml(request):
    return HttpResponse(serializers.serialize("xml", data_watchlist), content_type="application/xml")
def show_json(request):
    return HttpResponse(serializers.serialize("json", data_watchlist), content_type="application/json")
    
