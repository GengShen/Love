#coding:utf-8
from django.http import HttpResponse
from django.template.loader import get_template
from django.shortcuts import render_to_response
import requests
import datetime
import os.path
import os

def index(request):
	now=datetime.datetime.now()
	return render_to_response('index.html')
def med(request):
	if 'q' in request.GET:
		name_raw=request.GET['q']
		name_pro=os.path.join(os.path.dirname(__file__), 'templates/media/')
		image_data=open(name_pro+name_raw).read()
		return HttpResponse(image_data, mimetype="image/png")
def alg(request):
	name_pro=os.path.join(os.path.dirname(__file__), 'templates/alg/alg.html')
	return render_to_response(name_pro)