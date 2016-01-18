#coding:utf-8
from django.http import HttpResponse
from django.template.loader import get_template
from django.shortcuts import render_to_response
import requests
import datetime
import os.path

base_dir=os.path.dirname(__file__)+'/templates/'

def index(request):
	return render_to_response('index.html')
	#return render_to_response('js/functions.js')
def statics(requests,x):
	return render_to_response(x)

def default(request):
	f=open(os.path.join(base_dir,'css/default.css')).read()
	return HttpResponse(f)
	#return render_to_response('css/default.css')
def jquery(request):
	f=open(os.path.join(base_dir,'js/jquery.js')).read()
	return HttpResponse(f)
	#return render_to_response('js/jquery.js')
def garden(request):
	f=open(os.path.join(base_dir,'js/garden_dev.js')).read()
	return HttpResponse(f)
	#return render_to_response('js/garden_dev.js')
def functions(request):
	f=open(os.path.join(base_dir,'js/functions_dev.js')).read()
	return HttpResponse(f)
	#return render_to_response('js/functions_dev.js')