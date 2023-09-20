from django.shortcuts import render
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate
#from django.contrib.auth import logout
#application import
import jwt
import random
from rest_framework.decorators import api_view
from rest_framework.response import Response 
from Login_System.models import UserAccounts
from Login_System.serializers import User_Login_Serializer
from django.contrib.auth.models import User
#database import
from Login_System.models import Register_As_Job_Searcher,Register_As_Company,User_Reg_Types,Register_As_Student,User_Login_Types
from Login_System.serializers import Register_As_Company_Serializer,Register_As_Job_Searcher_Serializer,User_Reg_Type_Serializer,User_Login_Type_Serializer,Register_As_Student_Serializer
#authentication import
from rest_framework.authentication import BasicAuthentication,SessionAuthentication#session_authentication didnot allow with session_authentication
from rest_framework.permissions import IsAuthenticated,IsAdminUser#isadminuser allows only admin users
import pytz
from datetime import datetime,timedelta

@api_view(['POST'])
def Login(request):
    username=request.data.get('username')
    password=request.data.get('password')
    hashed_password=make_password(password)
    auth=authenticate(username=username,password=password)
    
    

    if auth:
        
        auth_token=jwt.encode({"username":username,"password":password},username+password+str(datetime.now(tz=pytz.timezone("UTC"))),algorithm='HS256')
        token=''.join(random.sample(auth_token,len(auth_token)))
        
        op=UserAccounts.objects.filter(username=username).update(login_expire_time=datetime.now(tz=pytz.timezone("UTC"))+timedelta(minutes=5),login_token=token,last_login=datetime.now(tz=pytz.timezone("UTC")))
        
        
        
        return Response({"message":"Successfully Logged","auth_token":token})
    else:
        return Response({"message":"Failed"})
    
@api_view(['post'])
def Logout(request):
    try:
        username=request.data.get("username")
        auth_token=request.data.get("token")
        auth_token=jwt.encode({"username":username},username+str(datetime.now(tz=pytz.timezone("UTC"))),algorithm='HS256')
        token=''.join(random.sample(auth_token,len(auth_token)))
        
        op=UserAccounts.objects.filter(username=username,login_token=auth_token).update(user_message="Logged Out",login_expire_time=datetime.now(tz=pytz.timezone("UTC")),login_token=token)
        

        return Response({"message":"Successfully Logout"})
    except:
    
        return Response({"message":"Failed"})

@api_view(['GET'])
def View_User_Login_Types(request):
    get_data=User_Login_Types.objects.all()
    U_L_S=User_Login_Type_Serializer(get_data,many=True)
    return Response(U_L_S.data)



@api_view(['GET'])
def View_User_Reg_Types(request):
    get_data=User_Reg_Types.objects.all()
    U_T_S=User_Reg_Type_Serializer(get_data,many=True)
    return Response(U_T_S.data)

@api_view(['GET'])
def View_Register_As_Job_Searcher(request):
    get_data=Register_As_Job_Searcher.objects.all()
    R_A_J_S_S=Register_As_Job_Searcher_Serializer(get_data,many=True)
    return Response(R_A_J_S_S.data)


def incoming_data_validate(data:list):

    ref_data=''
    for k,v in data.items():
        if v is not None:
            #print(k,v,v=="Select The Branch")
            if v.isspace() or len(v)<=0 or v=="Select The Branch" or v=="Select The Year" or v=="Select The Sem" or v=="Select The Qualification":
                ref_data+=k+','
        else:
            ref_data+=k+','
    
    if len(ref_data)>0:
        return {"message":f"{ref_data} --> This Fields Must Be Values --> Not Empty"},False
    else:
        return {"message":"Successfully Registered"},True

def username_password_validation(i_data:list):
    ref_data={}
    for data in i_data:
        if len(data)>=8 :
            if not data.endswith(' ') and not data.startswith(" ") and not " " in data:
                #print(data,len(data),data.endswith(' '),data.startswith(" "))
                ref_data.update({"message":True})
            else:
                ref_data.update( {"message":"password or username not starts or ends with space or dont include space".title()})
                break
        else:
            ref_data.update( {"message":"password or username length must 8 characters".title()})
            break
            
    return ref_data

@api_view(['POST'])
def Register_Job_Searcher_(request):
    
    get_data=Register_As_Job_Searcher.objects.all()
    R_A_J_S_S=Register_As_Job_Searcher_Serializer(data=request.data)
    
    #if R_A_J_S_S.is_valid():
        
    f_name=request.data.get('first_name')
    l_name=request.data.get('last_name')
    highest_qualification=request.data.get('qualification')
    branch=request.data.get("branch")
    password=request.data.get('password')
    email=request.data.get('email')
    username=request.data.get('username')
    cell_no=request.data.get('cell_no')
    
    i_data={"password":password,"email_id":email,"username":username,"first_name":f_name,"last_name":l_name,"cell_no":cell_no,"qualification":highest_qualification,"branch":branch}

    validate,status=incoming_data_validate(i_data)
    if status:
        validate_user_exists=[]
        get_username=UserAccounts.objects.filter(username=username)
        for u in get_username:
            validate_user_exists.append(u.username)
            validate_user_exists.append(u.email)
        
        if email not in validate_user_exists and username not in validate_user_exists:
            
            upv=username_password_validation([username,password])
            if upv['message']==True:
                print(upv)
                hashed_password=make_password(password)

                ras=Register_As_Job_Searcher.objects.create(f_name=f_name,l_name=l_name,highest_qualification=highest_qualification,branch=branch,cell_no=cell_no,password=hashed_password,username=username,email_id=email)
                create=UserAccounts.objects.create(first_name=f_name,cell_no=cell_no,user_type="job_searcher",last_name=l_name,email=email,username=username,password=password,login_expire_time=datetime.now(tz=pytz.timezone("Asia/Kolkata")),login_token="",user_status="Registered",last_login=datetime.now(tz=pytz.timezone("Asia/Kolkata")))
                
                create.save()
                User.objects.create_user(username=username,password=password,first_name=f_name,last_name=l_name,email=email).save()
                ras.save()
                return Response({"message":"Successfully Registered"})
            else:
                return Response(upv)
            
        else:
            return Response({"message":"Username or Email Id All Ready Exists"})
    else:
        return Response(validate)
        



@api_view(['GET'])
def View_Register_As_Company(request):

    get_data=Register_As_Company.objects.all()
   
    R_A_C_S=Register_As_Company_Serializer(get_data,many=True)
    return Response(R_A_C_S.data)   
    
    


@api_view(['POST'])
def Register_As_Company_(request):
    
    R_A_C_S=Register_As_Company_Serializer(data=request.data)
    
    company_name=request.data.get('company_name')
    password=request.data.get('password')
    email=request.data.get('email_id')
    username=request.data.get('username')
    cell_no=request.data.get('cell_no')
    first_name=request.data.get("first_name")
    
    last_name=request.data.get("last_name")
    
    i_data={"password":password,"username":username,"email_id":email,"company_name":company_name,"first_name":first_name,"last_name":last_name,"cell_no":cell_no}
    validate,status=incoming_data_validate(i_data)        
    if status:
        validate_user_exists=[]
        get_username=UserAccounts.objects.filter(username=username)

        for u in get_username:
            validate_user_exists.append(u.username)
            validate_user_exists.append(u.email)
        
        if email not in validate_user_exists and username not in validate_user_exists:
            upv=username_password_validation([username,password])
            if upv['message'] == True:
                
                hashed_password=make_password(password)

                rac=Register_As_Company.objects.create(f_name=first_name,l_name=last_name,company_name=company_name,cell_no=cell_no,password=hashed_password,username=username,email_id=email)
                create=UserAccounts.objects.create(first_name=first_name,last_name=last_name,email=email,cell_no=cell_no,user_type="company",username=username,password=hashed_password,login_expire_time=datetime.now(tz=pytz.timezone("Asia/Kolkata")),login_token="",user_message="Registered",last_login=datetime.now(tz=pytz.timezone("Asia/Kolkata")))
                
                User.objects.create_user(username=username,password=password).save()

                rac.save()
                create.save()
                
                return Response({"message":"Successfully Registered"})
            else:
                return Response(upv)
              
        else:
            return Response({"message":"Username or Email Id All Ready Exists"})
    else:
        #print(request.data.get('company_name'))
        return Response(validate)
    
    
    
@api_view(['GET'])
def View_Student_Accounts(request):
    get_data=Register_As_Student.objects.all()
    R_A_S_S=Register_As_Student_Serializer(get_data,many=True)
    return Response(R_A_S_S.data)

@api_view(['POST'])
def Register_As_Student_(request):
    

    R_A_S_S=Register_As_Student_Serializer(data=request.data)
    
    
        
    f_name=request.data.get('first_name')
    l_name=request.data.get('last_name')
    qualification=request.data.get('qualification')
    year=request.data.get('year')
    sem=request.data.get('sem')
    branch=request.data.get('branch')
    
    
    password=request.data.get('password')
    email=request.data.get('email')
    username=request.data.get('username')
    cell_no=request.data.get('cell_no')
        
        
    i_data={"password":password,"email_id":email,"username":username,"first_name":f_name,"last_name":l_name,"cell_no":cell_no,"qualification":qualification,"sem":sem,"year":year,"branch":branch}

    validate,status=incoming_data_validate(i_data)
    if status:
        
        validate_user_exists=[]
        get_username=UserAccounts.objects.filter(username=username)

        for u in get_username:
            validate_user_exists.append(u.username)
            validate_user_exists.append(u.email)
        
        if email not in validate_user_exists and username not in validate_user_exists:
            upv=username_password_validation([username,password])
            if upv['message']==True:
                
                hashed_password=make_password(password)

                ras=Register_As_Student.objects.create(f_name=f_name,year=year,sem=sem,l_name=l_name,qualification=qualification,branch=branch,cell_no=cell_no,password=hashed_password,username=username,email_id=email)

                create=UserAccounts.objects.create(first_name=f_name,last_name=l_name,email=email,cell_no=cell_no,user_type="student",username=username,password=hashed_password,login_expire_time=datetime.now(tz=pytz.timezone("Asia/Kolkata")),login_token="",user_status="Registered",last_login=datetime.now(tz=pytz.timezone("Asia/Kolkata")))
                
                User.objects.create_user(username=username,password=password,first_name=f_name,last_name=l_name,email=email).save()
                ras.save()
                create.save()

                
                return Response({"message":"Successfully Registered"})
            else:
                return Response(upv)
              
        else:
            return Response({"message":"Username or Email Id All Ready Exists"})
    else:
        return Response(validate)
    
