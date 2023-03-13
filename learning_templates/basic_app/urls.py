from django.urls import path #--------important
from basic_app import views

# for template_tagging
# this name should match the application name
app_name = 'basic_app'

urlpatterns = [
    path('relative/', views.relative, name = 'relative'),
]
