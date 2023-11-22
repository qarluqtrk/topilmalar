from django.urls import path

from app.views.auth import signup_view, signin_view, password_reset_view, verify_email_view, logout_view, \
    my_profile_view
from app.views.other import index_view, item_view

urlpatterns = [
    path('', index_view, name='index'),
    path('signup/', signup_view, name='signup'),
    path('signin/', signin_view, name='signin'),
    path('password_reset/', password_reset_view, name='password_reset'),
    path('verify_email/', verify_email_view, name='verify_email'),
    path('logout/', logout_view, name='logout'),
    path('my_profile/', my_profile_view, name='my_profile'),
    path('item/', item_view, name='item'),
]
