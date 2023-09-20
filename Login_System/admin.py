from django.contrib import admin
from Login_System.models import UserAccounts,Register_As_Company,Register_As_Student,User_Reg_Types,User_Login_Types,Register_As_Job_Searcher

# Register your models here.

class Register_Register_As_Company(admin.ModelAdmin):
    list_display=['username','company_name','email_id']
admin.site.register(Register_As_Company,Register_Register_As_Company)

class Register_As_Job_s(admin.ModelAdmin):
    list_display=['f_name','l_name','username','email_id']
admin.site.register(Register_As_Job_Searcher,Register_As_Job_s)

class Register_As_Student_s(admin.ModelAdmin):
    list_display=['f_name','l_name','username','email_id']
admin.site.register(Register_As_Student,Register_As_Student_s)


class Register_User_Types(admin.ModelAdmin):
        list_display=['type','url','created_at']
admin.site.register(User_Reg_Types,Register_User_Types)
    

class Register_User_Login_Types(admin.ModelAdmin):
        list_display=['type','url','created_at']
admin.site.register(User_Login_Types,Register_User_Login_Types)

class accounts(admin.ModelAdmin):
    
    list_display=['username']
admin.site.register(UserAccounts,accounts)