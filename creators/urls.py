from django.urls import path, include
from creators import views
from django.contrib.auth import views as auth_views


urlpatterns=[
    path('login', auth_views.LoginView.as_view(template_name='creators/auth.html'), name='creators-login'),
    path('logout', auth_views.LogoutView.as_view(template_name='creators/auth.html', next_page='/creators'), name='creators-logout'),
    path('',views.auth_home),
    path('sign-up',views.sign_up,name='creators-sign-up')
]