

# Create your views here.
from django.http import HttpResponse
#from django.template import loader
from django.shortcuts import render
from demo.models import Program
from demo.models import Bundle
from demo.models import Software
from demo.models import Firmware
from demo.models import Report
import os

def queryprograms(request):    
    programs = Program.objects.all()
    c =  {'title': 'Performance Query - Select Program',
         'programs': programs}
    return render(request, 'queryprograms.html', context=c)



def querybundles(request):
    program_id = request.POST['program_id']
    bundles = Bundle.objects.filter(programId=program_id)
    c = {'title': 'Performance Query - Select Bundle',
         'bundles': bundles}
    return render(request, 'querybundles.html', context=c)



def querywares(request):
    
    bundle_id = request.POST['bundle_id']
    softwares = Software.objects.filter(bundleId=bundle_id)
    firmwares = Firmware.objects.filter(bundleId=bundle_id)
    c = {'title': 'Performance Query - Select Firmware & Software'
         , 'bundle_id': bundle_id
         , 'softwares': softwares
         , 'firmwares': firmwares 
         }
    return render(request, 'querywares.html', context=c)  



def search(request):
    bundle_id = request.POST['bundle_id']
    software_id = request.POST['software_id']
    firmware_id = request.POST['firmware_id']
    if firmware_id == '0' and software_id == '0':
        reports = Report.objects.filter(bundleId=bundle_id)
    elif firmware_id == '0':       
        reports = Report.objects.filter(softwareId=software_id)
    elif software_id == '0':       
        reports = Report.objects.filter(firmwareId=firmware_id)       
    else:
        reports = Report.objects.filter(firmwareId=firmware_id, softwareId=software_id)         
    c = {'title': 'Search results'
         , 'reports': reports
         }
    return render(request, 'searchresult.html', context=c)  


def download(request):
    report_id = request.GET['report_id']
    report = Report.objects.get(id=report_id)
    file_path = report.path
    with open(file_path, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type="application/vnd.ms-excel")
            response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
            return response


