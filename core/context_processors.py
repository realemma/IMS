from .models import Request
from django.shortcuts import render,redirect,get_object_or_404


def counts(request):
    uncom = Request.objects.filter(status='uncompleted').count()
    pends = Request.objects.filter(status='pending').count()
    add=  int(uncom + pends)
    reject = Request.objects.filter(status='rejected').count()
    approve = Request.objects.filter(status='approved').count()
    last = Request.objects.filter(status='uncompleted').last()
    lapprove = Request.objects.filter(status='approved').last()



    context = {'uncom': uncom,
               'pends': pends,
               'reject': reject,
               'approve': approve,
                'last': last,
                'lapprove': lapprove,
                'add':add


               }    
    return (context)







