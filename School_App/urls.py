from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.signup,name="signup"),
    path('index/',views.index,name="index"),
    path('login/',views.login,name="login"),
    path('logout/',views.logout,name="logout"),

    path('teachers/',views.teachers,name="teachers"),
    path('students/',views.students,name="students"),
    path('classes/',views.classes,name="classes"),
    path('dashboard/',views.dashboard,name="dashboard"),
    path('table/',views.table,name="table"),
    path('assignment/',views.assignment,name="assignment"),
    path('delete_assignment/<int:pk>/',views.delete_assignment,name="delete_assignment"),
    path('update_assignment/<int:pk>/',views.update_assignment,name="update_assignment"),
   
    path('profile/',views.profile,name="profile"),
    
    path('subject/',views.subject,name="subject"),
    path('leave/',views.leave,name="leave"),
    path('delete_leave/<int:pk>/',views.delete_leave,name="delete_leave"),
    path('update_leave/<int:pk>/',views.update_leave,name="update_leave"),

    path('virtual-reality/',views.virtual_reality,name="virtual-reality"),
   
    path('otp/',views.otp,name="otp"),
    path('forgot_password/',views.forgot_password,name="forgot_password"),
    path('change_password/',views.change_password,name="change_password"),

    

]


if settings.DEBUG: # new
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)