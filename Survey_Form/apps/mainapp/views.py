# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect



def index(request):
    return render(request, 'mainapp/index.html')

def display_result(request):
    return render(request, 'mainapp/results.html')

def process_form(request):
    try:
        request.session['tries']
    except KeyError:
        request.session['tries'] = 0
    request.session['yourname'] = request.POST['yourname']
    request.session['location'] = request.POST['location']
    request.session['favlang'] = request.POST['favlang']
    request.session['commentbox'] = request.POST['commentbox']
    request.session['tries'] += 1
    
    return redirect('/result')