from django.urls import path
from .views import create_blog,see_all_post, see_detailed_post, account_page
from .views import delete_blog

urlpatterns = [
    path('', see_all_post),
    path('detailed/<id_blog>', see_detailed_post),
    path('profile', account_page),
    path('delete/<id_blog>', delete_blog),
    path('create', create_blog)
]


