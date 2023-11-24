from django.urls import path

from app.views.auth import signup_view, signin_view, verify_email_view, logout_view, \
    my_profile_view, ActivateEmailView, ActivatePasswordEmailView, forgot_password_view
from app.views.other import index_view, item_view
from app.views.post import post_view

urlpatterns = [
    path('', index_view, name='index'),
    path('signup/', signup_view, name='signup'),
    path('signin/', signin_view, name='signin'),
    path('password_reset/', password_reset_view, name='password_reset'),
    path('verify_email/', verify_email_view, name='verify_email'),
    path('logout/', logout_view, name='logout'),
    path('my_profile/', my_profile_view, name='my_profile'),
    path('item/', item_view, name='item'),
    path('post/', post_view, name='post'),
    path('activate/<str:uid>/<str:token>/', ActivateEmailView.as_view(), name='confirm-mail'),
    path('activate_password/<str:uid>/<str:token>/', ActivatePasswordEmailView.as_view(), name='activate_password'),

]
