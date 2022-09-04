from ast import Return
from re import I
from urllib import request
from django.shortcuts import render
import sklearn
import joblib
import numpy as np
from sklearn.preprocessing import StandardScaler


# Create your views here.

def home(request):

    return render(request, 'index.html')


def result(request):
    list=[]
    list.append(request.GET['Age'])
    list.append(request.GET['AverageLeadTime'])
    list.append(request.GET['DaysSinceCreation'])
    list.append(request.GET['LodgingRevenue'])
    list.append(request.GET['OtherRevenue'])
    list.append(request.GET['PersonsNights'])

    model=joblib.load('svc_check_in.sav')

    answer=model.predict([list])
    if answer == 1:
        answer='The person is gooing to be checke_in'
    elif answer == 0 :
        answer = 'the person Not going to be checke_in'
    else:
        answer= 'check the enterd data, wether correct or not'
    

    return render(request,'result.html',{'answer':answer,"list":list})