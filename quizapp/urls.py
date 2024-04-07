"""
URL configuration for quizapp project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from . import views



urlpatterns = [
    path('admin/', admin.site.urls),
    path("index/", views.Index.as_view(), name="index"),
    path("", include("account.urls")),
    path("quiz/", include("quiz.urls")),
    path("management/", include("management.urls")),
#     path('studentDashboard/course/<int:course>/', views.view_course, name="view_course"), # View Course Page TODO: Add course Number
#     #path('studentDashboard/courselist', views.courselist, name="courselist"), #TODO: Implement this later
#     #path('studentDashboard/profile', views.profile, name="profile"), 
#     path('studentDashboard/availableCourses/', views.show_avl_course, name="show_courses"),
# ####    #path('signin/', views.auth_email, name="auth_email"),
#     # path('setNewPwd/', views.set_new_pwd, name="set_new_pwd"),
  
   
#     path('studentDashboard/module/<int:course>/<int:week>/<int:material>/', views.module, name="module"),
]
