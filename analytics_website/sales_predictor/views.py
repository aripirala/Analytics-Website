from django.shortcuts import render

def index(request):
	return render(request, 'sales_predictor/sales_model.html')
