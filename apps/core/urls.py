from django.urls import path
from django.contrib.auth.views import LogoutView
from apps.core.views import CustomLoginView

app_name = 'core'

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
