from django.shortcuts import render
from Login_System.models import Register_As_Company,Register_As_Job_Searcher,Register_As_Student
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.response import Response
from datetime import datetime
from pytz import timezone
import random
import json
from Login_System.models import UserAccounts
from rest_framework.decorators import api_view
# Create your views here.

def data_fetch(username,user_type):
    if user_type=="company":
        cp=Register_As_Company.objects.get(username=username)
        return {"Status":"Success","userdata":{"Username":cp.username,"Company_Name":cp.company_name,"First_Name":cp.f_name,'Last_Name':cp.l_name,"Email_Id":cp.email_id,"Mobile_No":str(cp.cell_no)}}
    elif user_type=='job_searcher':
        js=Register_As_Job_Searcher.objects.get(username=username)

        return {"Status":"Success","userdata":{"Username":js.username,"First_Name":js.f_name,"Last_Name":js.l_name,"Highest_Qualification":js.highest_qualification,"Email_Id":js.email_id,"Branch":js.branch,"Mobile_No":str(js.cell_no),"Alternative_Mobile":js.alternative_cell_no}}

    elif user_type=="student":
        st=Register_As_Student.objects.get(username=username)
    
             
        return {"Status":"Success","userdata":{"Username":st.username,"First_Name":st.f_name,"Last_Name":st.l_name,"Email_Id":st.email_id,"Qualification":st.qualification,"Branch":st.branch,"Year":st.year,"Sem":st.sem,"Mobile_No":str(st.cell_no)}}
                
    


@api_view(["POST"])
def validator(request):
    
    username=request.data.get("username")
    auth_token=request.data.get("auth_token")
    
    
    try:
        
        get_user_data=UserAccounts.objects.get(username=username,login_token=auth_token)
        
        
        login_expire_time=int(get_user_data.login_expire_time.timestamp())
        
        #print(get_user_data)
            
        
        c_time=int(datetime.now(tz=timezone("UTC")).timestamp())
        
        if login_expire_time>c_time:
            
            UserAccounts.objects.filter(username=username).update(user_status="Logged In")
            
            resp=data_fetch(username,get_user_data.user_type)
            
            
            return Response(resp)
            
        else:
            token=''.join(random.sample(auth_token,len(auth_token)))
            
            UserAccounts.objects.filter(username=username).update(login_token=token,user_status="session_expired")
            
            return Response({"Status":"Expired","msg":"Your Session Time Is Expired..Try To Login Again"})
    
    except ObjectDoesNotExist:
        
        return Response({"Status":"Failed","msg":"User Does Not Exists or User Not Valied"})
    
    