from django.conf.urls import url
# from django.urls import path
from django.urls import include


from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register('hello-viewset', views.HelloViewSet, base_name='hello-viewset')
router.register('profile', views.UserProfileViewSet)       # it is a modelviewset 
router.register('login', views.LoginViewSet, base_name='login')

urlpatterns = [
    url(r'^hello-apiview/', views.HelloApiView.as_view()),
    # path('login/', views.UserLoginApiView.as_view()),
    url(r'',include(router.urls)),
]

