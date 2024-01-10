from django.urls import path
from myapp import views

urlpatterns = [
    # path('',views.index),
    path('', views.my_view, name='my_view'),
    path('about',views.about),
    path('form',views.form),
    path('edit/<person_id>',views.edit)
]