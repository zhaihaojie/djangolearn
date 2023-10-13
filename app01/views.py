from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

# Create your views here.


def hello(request):
    return HttpResponse("Hello World!")


def articla_year(request, year):
    return HttpResponse(f"{year}所有文章")


def articla_month(request, year, month):
    return HttpResponse(f"{year}年{month}月所有文章")


def articla_flag(request, year, month, flag):
    return HttpResponse(f"{year}年{month}月{flag}所有文章")


def get_current_datetime(request):
    today = datetime.today()
    formattoday = today.strftime("%Y-%m-%d %H:%M:%S")
    return HttpResponse(f"当前时间为：{formattoday}")
