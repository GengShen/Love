#coding:utf-8
from django.http import HttpResponse
from django.template.loader import get_template
from django.shortcuts import render_to_response
import requests
import datetime
import os.path
import os

def index(request):
	return render_to_response('index.html')

def statics(requests,x):
	return render_to_response(os.path.join(os.path.dirname(__file__), 'templates/'+x))