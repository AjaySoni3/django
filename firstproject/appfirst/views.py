from django.shortcuts import render
from appfirst.models import AccessRecord,Webpage,Topic

# Create your views here.

def index(request):
    webpage_list = AccessRecord.objects.order_by('date')
    date_dict = {'access_records': webpage_list}
    return render(request,'appfirst/index.html',context=date_dict)