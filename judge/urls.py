from django.urls import path

from . import views

urlpatterns = [
        path('', views.judge_home, name='judge_home'),
        path('<int:pk>', views.judge_case_detail, name='judge_case_detail'),
        # path('lawyers', lawyer_list_view, name='lawyers_user'),
        # path('profile/<int:pk>', user_profile_detail_view, name='user_profile'),
        # path('profile/update/<int:pk>', PlaintifUpdateProfile.as_view(), name='user_update_profile'),

]

