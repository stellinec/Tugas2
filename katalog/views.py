from django.shortcuts import render
from katalog.models import CatalogItem

# TODO: Create your views here.

# Create your views here.
data_barang_katalog = CatalogItem.objects.all()
context = {
    'list_barang': data_barang_katalog,
    'nama' : 'Stelline Claudia',
    'id' : '2106700933'
}
def show_katalog(request):
    return render(request, "katalog.html", context)