from django.urls import path
from joinapp.views import my_project

app_name = 'joinapp'

urlpatterns = [
    path('my_project/',my_project, name='my_project'),

]