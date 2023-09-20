from rest_framework import serializers
from Login_System.models import Register_As_Company,Register_As_Job_Searcher,User_Reg_Types,User_Login_Types,Register_As_Student
from django.contrib.auth.models import User

class User_Reg_Type_Serializer(serializers.ModelSerializer):
    class Meta:
        model=User_Reg_Types
        fields="__all__"

class User_Login_Type_Serializer(serializers.ModelSerializer):
    class Meta:
        model=User_Login_Types
        fields="__all__"



class Register_As_Company_Serializer(serializers.ModelSerializer):
    class Meta:
        model=Register_As_Company
        fields='__all__'


class Register_As_Job_Searcher_Serializer(serializers.ModelSerializer):
    class Meta:
        model=Register_As_Job_Searcher
        fields='__all__'

class Register_As_Student_Serializer(serializers.ModelSerializer):
    class Meta:
        model=Register_As_Student
        fields='__all__'


class User_Login_Serializer(serializers.ModelSerializer):
    class Meta:
        model=User
        
