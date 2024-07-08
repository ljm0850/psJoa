"""
URL configuration for psJoa project.

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
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/accounts/',include('accounts.urls')),     # accounts/urls.py 에 정의
    path('api/accounts/',include('dj_rest_auth.urls')), # dj_rest_auth 라이브러리 정의
    path('api/accounts/signup',include('dj_rest_auth.registration.urls')),  # dj_rest_auth.registration 에 정의
    path('api/articles/',include('articles.urls')), # articles/urls.py에 정의
    path('api/problems/',include('problems.urls'))  # problems/urls.py에 정의
]
