from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.signup,name="signup"),
    path('home/',views.index,name="index"),
    path('login/',views.login,name="login"),
    path('',views.logout,name="logout")
]


if settings.DEBUG: # new
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)