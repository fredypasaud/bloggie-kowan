from django.urls import path
from .views import create_blog,see_all_post, see_detailed_post

urlpatterns = [
    path('', see_all_post),
    path('<id_blog>', see_detailed_post),
    path('create', create_blog)
]


