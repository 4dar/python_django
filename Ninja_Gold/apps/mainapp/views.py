# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from random import randint
from datetime import datetime


def index(request):
    if not 'total' in request.session:
        request.session['total'] = 0
    return render(request, "mainapp/index.html")

def process(request, building_type):
    this_gold = 0
    action = 'earned'
    if building_type == 'farm':
        this_gold = randint(10,20)
    elif building_type == 'cave':
        this_gold = randint(5,10)
    elif building_type == 'house':
        this_gold = randint(2,5)
    else:
        this_gold = randint(-50,50)
        if this_gold < 0:
            action = 'lost'
    timestamp = datetime.now().strftime("%Y/%m/%d %-I:%M%p")
    this_log = {
        'class': action,
        'message': "You {} {} golds from the {} ({})".format(action, abs(this_gold), building_type, timestamp)
    }
    try:
        log_list = request.session['logs']
    except KeyError:
        log_list = []

    request.session['total'] += this_gold
    
    log_list.append(this_log)
    request.session['logs'] = log_list

    return redirect('/')

def clear(request):
    request.session['total'] = 0
    return redirect('/')
