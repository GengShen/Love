#coding:utf-8
from django.http import HttpResponse
from django.template.loader import get_template
from django.shortcuts import render_to_response
import requests
import datetime
import os.path

def index(request):
	#return render_to_response('index.html')
	return render_to_response('js/functions.js')
def statics(requests,x):
	return render_to_response(x)