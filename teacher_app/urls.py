"""teacher_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path, include


urlpatterns = [
    # Auth users url
    path('api/users/', include('teacher_app.apps.authentication.urls')),
    # Class related urls
    path('api/classes/', include('teacher_app.apps.classes.urls.class_urls')),
    # Student related views
    path(
        'api/students/',
        include('teacher_app.apps.classes.urls.students_urls')),
    # Subjects related views
    path(
        'api/subjects/', include('teacher_app.apps.classes.urls.subject_urls'))
]
