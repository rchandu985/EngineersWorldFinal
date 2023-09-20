from django.contrib import admin
from django.urls import path
from Login_System import views
urlpatterns = [
    #get
    path('view_company_accounts/', views.View_Register_As_Company),
    path("view_job_searchers_accounts/",views.View_Register_As_Job_Searcher),
    path("view_user_reg_types/",views.View_User_Reg_Types),
    path("view_students_accounts/",views.View_Student_Accounts),
    path("view_user_login_types/",views.View_User_Login_Types),
    
    #post
    path("register_as_company/",views.Register_As_Company_),
    path("register_as_job_searcher/",views.Register_Job_Searcher_),
    path("register_as_student/",views.Register_As_Student_),
    #login
    path("Login/",views.Login),
    path("Logout/",views.Logout),
    
]
