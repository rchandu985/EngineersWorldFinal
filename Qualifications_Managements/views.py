from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Qualifications

@api_view(["GET","POST"])
def fetch_qualifications_data(request):
    #print(request.method)
    if request.method=="GET":
    
        qualifications_data=[{"value":data.name,"label":data.name,"type":"qualification"} for data in  Qualifications.objects.all()]
        
        
        return Response({"qualifications":qualifications_data})
    
    elif request.method=="POST":
        
        qualification=request.data.get("qualification").title()
        required_type=request.data.get("required_type")

        if required_type=="branch":
            branches_data=[{"value":data.name,"label":data.name,"type":"branch"} for data in  Qualifications.objects.get(name=qualification).branches.all()]

            return Response({"branches":branches_data})
        elif required_type=="year":
            years_data=[{"value":data.name,"label":data.name,"type":"year"} for data in  Qualifications.objects.get(name=qualification).year.all()]
            return Response({"years":years_data})
        elif required_type=="sem":
            sems_data=[{"value":data.name,"label":data.name,"type":"sem"} for data in  Qualifications.objects.get(name=qualification).sem.all()]

            return Response({"sems":sems_data})
