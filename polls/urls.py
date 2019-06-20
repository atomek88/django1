# url.py= URLconf necessary to map view to url
from django.urls import path

from . import views
# add app name to help application namespace
app_name = 'polls'
urlpatterns = [
    path('', views.index, name='index'),
    # polls/#/
    path('<int:question_id>/', views.detail, name='detail'),
    # polls/#/results
    path('<int:question_id>/results/', views.results, name='results'),
    # polls/#/votes
    path('<int:question_id>/vote/', views.vote, name='vote'),
    ]
