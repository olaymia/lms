from django.urls import path
from . import views


urlpatterns = [
    path('sel_pre_top/', views.select_topic, name='pre_top'),
    path('sel_pre_qty/<int:topic_id>/', views.select_topic_quantity, name='sel_pre_top_qty'),
    path('get_pre_top_exam/<int:topic_id>/<int:num_questions>/', views.start_topic_quiz, name='sel_pre_top_exm'),
]
