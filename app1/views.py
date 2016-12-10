from django.shortcuts import render
from django.http import HttpResponse
from models import Food_Menu

# Create your views here.
def index(request):
	return HttpResponse('This is the index page')

def detail(request, id):
	#name = Food_Menu.objects.get(food_id=id)
	#return HttpResponse('Here is the Food you want: %s'%(Food_Menu.objects.get(food_id=id)))
	return HttpResponse('Name: %s Description: %s' % ((Food_Menu.objects.get(food_id=id).name), (Food_Menu.objects.get(food_id=id).description)))