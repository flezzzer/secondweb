"""
URL configuration for secondweb project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from restaurant import views
from creators import api


from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('restaurant/', include("restaurant.urls")),
    path('',views.home, name='home'),
    path('creators/', include('creators.urls')),
    path('form/',include('validform.urls'),name='form'),
    path('api/client/restaurants',api.client_get_restaurants),
    path('api/client/restaurants/<str:restaurant_name>/categorys',api.get_categorys),
    path('api/client/restaurants/<str:restaurant_name>/<str:category_name>/meal',api.get_meal),
    # path('auth/social/', include('rest_framework_social_oauth2.urls')),
    # /convert-token (sign in/sign up)
    # /revoke-token (sign-out)
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
