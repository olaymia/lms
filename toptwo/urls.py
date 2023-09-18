from django.urls import path
from . import views


urlpatterns = [
    path('sel_para_top/', views.select_topic, name='para_top'),
    path('sel_para_qty/<int:topic_id>/', views.select_topic_quantity, name='sel_para_top_qty'),
    path('get_para_top_exam/<int:topic_id>/<int:num_questions>/', views.start_topic_quiz, name='sel_para_top_exm'),
]