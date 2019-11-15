from django.urls import path
from . import views

app_name = 'polls'

urlpatterns =[
    # path('demo/', views.index, name='index'),
    # path('love/',views.demo, name='love'),
    #path('<int:id>/', views.detail, name='ok'),
    path('index/', views.index, name="index"),
    path('<int:question_id>/', views.detail, name="detail"),
    path('/vote/<int:question_id>/', views.vote, name="vote"),
    path('results/<int:question_id>/', views.result, name="results"),
]