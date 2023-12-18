from django.urls import path
from .import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('',views.SignupPage,name='signup'),
    path('login/',views.LoginPage,name='login'),
    path('home/',views.HomePage,name='home'),
    path('home/logout/',views.LogoutPage,name='logout'),
    path('home/start/logout/',views.logpage,name='logpage'),
    path('home/start/', views.upload_image, name='upload_image'),
    path('home/about/', views.about, name='about'),
    path('home/about/logout/', views.logabout, name='logabout'),
    path('home/contact/', views.contact, name='contact'),
    path('home/contact/logout/', views.logcontact, name='logcontact'),
    path('home/start/view_image/<int:image_id>/', views.view_image, name='view_image'),
    path('home/start/view_image/back', views.back, name='back'),
    path('home/start/view_image/check/', views.check, name = 'check'),
    path('home/start/view_image/backk', views.backk, name='backk'),
    path('home/start/view_image/Check/', views.Check, name = 'Check'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)