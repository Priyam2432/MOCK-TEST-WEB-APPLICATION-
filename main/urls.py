from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
   path('',views.home,name="home"),
   path('accounts/register',views.register,name="register"),
   path('all_category',views.all_category,name="all_category"),
   path('category_question//<int:cat_id>',views.category_question,name="category_question"),
   path('submit_ans/<int:cat_id>/<int:question_id>',views.submit_answer,name="submit_answer"),
   path('Leaderboard',views.leaderboard,name="leaderboard"),
   ]
   
