from django.urls import path

from . import views

urlpatterns = [
        path('', views.judge_home, name='judge_home'),
        path('<int:pk>', views.judge_case_detail, name='judge_case_detail'),
        path('profile/<int:pk>', views.judge_profile_detail_view, name='judge_profile'),
        path('profile/update/<int:pk>', views.JudgeUpdateProfile.as_view(), name='judge_update_profile'),

]

