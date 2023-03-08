from django.urls import path
from . import views 

urlpatterns = [
    path('auth/login', views.login_view, name='user_login'),
    path('auth/register', views.signup_view, name=''),
    path('questions', views.get_all_questions_view, name='all_questions'),
    path('questions/<str:questionID>', views.get_selected_question_view, name='selected_question'),
    path('questions/<str:questionID>/answers', views.post_answers_view, name='post_users_answer'),
    path('questions/<str:questionID>/answers/<str:answerID>', views.update_answers_view, name='update_answer'),
    path('logout/', views.logout_user_view, name='user_logout'),
    

]