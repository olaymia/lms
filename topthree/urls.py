from django.urls import path
from . import views


urlpatterns = [
    path('sel_clinical_top/', views.select_topic, name='clinical_top'),
    path('sel_clinical_qty/<int:topic_id>/', views.select_topic_quantity, name='sel_clinical_top_qty'),
    path('get_clinical_top_exam/<int:topic_id>/<int:num_questions>/', views.start_topic_quiz, name='sel_clinical_top_exm'),
]
