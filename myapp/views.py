from django.shortcuts import render

# Create your views here.
# coding:utf-8
import json
from django.http import HttpResponse
from myapp.models import *
from django.views.decorators.csrf import csrf_exempt
from django.db.models.query import QuerySet
import datetime

def product_list(request):
    date_from = request.GET.get('start_time','2016-10-12T12:00:00-05:00')
    date_to = request.GET.get('end_time', '2016-10-14T12:00:00-05:00')
    data = []
    for item in  MyData.objects.filter(datetime__range=(date_from, date_to)):
        data.append({
            'id':item.id,
            'sid':item.sid,
            'description':item.description,
            'datetime': str(item.datetime),
            'longitude':item.longitude,
            'latitude':item.latitude,
            'elevation':item.elevation,
        })
    res = json.dumps(data)
    return HttpResponse(res)

@csrf_exempt
def product_update(request):
    id = request.POST.get('id')
    sid = request.POST.get('sid')
    description = request.POST.get('description')
    datetime = request.POST.get('datetime')
    longitude = request.POST.get('longitude')
    latitude = request.POST.get('latitude')
    elevation = request.POST.get('elevation')
    MyData.objects.get(id=id).save(sid=sid,description=description,datetime=datetime,longitude=longitude,latitude=latitude,elevation=elevation,)
    return HttpResponse(u"200")

@csrf_exempt
def product_add(request):
    myData=MyData(
        # id=request.POST.get('id'),
        sid = request.POST.get('sid'),
        description = request.POST.get('description'),
        datetime = request.POST.get('datetime'),
        longitude = request.POST.get('longitude'),
        latitude = request.POST.get('latitude'),
        elevation = request.POST.get('elevation'),
    )
    myData.save()
    return HttpResponse(u"200")

def product_list_1(request):
    date_from = request.POST.get('start_time','2016-10-12T12:00:00-05:00')
    date_to = request.POST.get('end_time', '2016-10-14T12:00:00-05:00')
    products = request.POST.get('products', ['Cesna 120'])

    data = []

    a = MyData.objects.filter(description__in=products,datetime__range=(date_from, date_to))
    for item in a:
        print(item)
        data.append({
            'id':item.id,
            'sid':item.sid,
            'description':item.description,
            'datetime': str(item.datetime),
            'longitude':item.longitude,
            'latitude':item.latitude,
            'elevation':item.elevation,
        })
    res = json.dumps(data)
    return HttpResponse(res)


def product_delete(request):
    id = request.GET.get('id')
    MyData.objects.filter(id=id).delete()
    return HttpResponse('200')