from django.urls import path
from . import views

urlpatterns = [
    path("<int:quiz_id>/", views.Quiz.as_view(), name="quiz"),
    path("add_question/", views.AddQuestion.as_view(), name="add_question"),
    path("add_course/", views.AddCourse.as_view(), name="add_course"),
    
    path("result/", views.Result.as_view(), name="result"),
    path("leaderboard/<int:quiz_id>/", views.Leaderboard.as_view(), name="leaderboard"),
    path("leaderboards/", views.Leaderboards.as_view(), name="leaderboards"),
    path("", views.Quiz_module.as_view(), name="module"),
    path('studentDashboard/course/<int:course>/', views.view_course, name="view_course"), # View Course Page TODO: Add course Number
    #path('studentDashboard/courselist', views.courselist, name="courselist"), #TODO: Implement this later
    #path('studentDashboard/profile', views.profile, name="profile"), 
    path('studentDashboard/availableCourses/', views.show_avl_course, name="show_courses"),
####    #path('signin/', views.auth_email, name="auth_email"),
    # path('setNewPwd/', views.set_new_pwd, name="set_new_pwd"),
  
   
    path('studentDashboard/module/<int:course>/<int:week>/<int:material>/', views.module, name="module"),

]
