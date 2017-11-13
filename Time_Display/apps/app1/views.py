from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse, redirect
from datetime import datetime
# from djangoutils import timezone


def index(request):
    context = {
        "time": datetime.now()
    }
    return render(request, "app1/index.html", context)

