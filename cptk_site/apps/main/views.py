from django.shortcuts import render
from catalog.models import Manufacturer

# Create your views here.
def home(request):
	manuf = Manufacturer.objects.all()
	return render(
			request,
			'main/home.html',
			context = {'manufs': manuf}
	)