from django.urls import path, include
from creators import views
from django.contrib.auth import views as auth_views


urlpatterns=[
    path('login', auth_views.LoginView.as_view(template_name='creators/auth.html'), name='creators-login'),
    path('logout', auth_views.LogoutView.as_view(template_name='creators/auth.html', next_page='/creators'), name='creators-logout'),
    path('',views.auth_home),
    path('sign-up',views.sign_up,name='creators-sign-up'),
    path('profile',views.profile,name='profile'),
    path('profile/edit_category',views.list_category,name='list_category'),
    path('profile/edit_meal',views.list_meal,name='list_meal'),
    path('profile/add_meal',views.add_meal,name='add_meal'),
    path('profile/add_category',views.add_category,name='add_category'),
    path('profile/edit_category/<str:category_name>',views.edit_category,name='edit_category'),
    path('profile/edit_meal/<int:meal_id>',views.edit_meal,name='edit_meal'),

]