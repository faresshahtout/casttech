from django.shortcuts import render
from django.shortcuts import render
from forms import castrequestform
from Casts import scriptexec
from .models import casts_scan
from .models import casts
# Create your views here.
def request_view(request):

    form=castrequestform()
    print(request.POST)
    dict=request.POST
    try:
        scriptexec.scriptexec(wristwidht=dict['wristwidth'],wristhight=dict['wristhight'],clearance=dict['clearance'],ABsection=dict['ABsection'],Bwidth=dict['Bwidth'],Bhight=dict['Bheight'],castthikness=dict['castthikness'],
               rightpump=dict['rightpump'], BCsection=dict['BCsection'],midhandthikness=dict['midhandthikness'],palmlength=dict['palmlength'],palmwidth=dict['palmwidth'],
              thumby=dict['thumbmuscle'],patientname=dict['Patientname'],circulediameter=dict["circlediameter"],Chight=dict["Cheight"],Cwidth=dict["Cwidth"],hangangle=dict["hangangle"],leftpump="leftpump",handtip=dict["handtip"],doctor=request.user )
        t=casts.objects.create(
            wristwidht=dict['wristwidth'], wristhight=dict['wristhight'], clearance=dict['clearance'],
            ABsection=dict['ABsection'], Bwidth=dict['Bwidth'], Bhight=dict['Bheight'],
            castthikness=dict['castthikness'],
            rightpump=dict['rightpump'], BCsection=dict['BCsection'], midhandthikness=dict['midhandthikness'],
            palmlength=dict['palmlength'], palmwidth=dict['palmwidth'],
            thumby=dict['thumbmuscle'], patientname=dict['Patientname'], circulediameter=dict["circlediameter"],
            Chight=dict["Cheight"], Cwidth=dict["Cwidth"], hangangle=dict["hangangle"], leftpump="leftpump",
            handtip=dict["handtip"], Doctor=request.user

        )
        t.save()

    except:
        pass
    return render(request,'request.html',)


def upload_file(request):
    dict=request.POST
    try:
        t=casts_scan.objects.create(Doctor=request.user(),Patientname=dict['Patientname'],File=dict['file'])
        t.save()
    except:
        print("error")
    return render(request, 'uploadrequest.html',)
def choose(request):
    return render(request,"choose.html")
# Create your views here.
