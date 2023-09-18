from django.urls import path
from . import views



urlpatterns = [

    path('sel_pre_sub/', views.select_subject, name='pre_sub'),
    path('sel_pre_qty/<int:subject_id>/', views.select_quantity, name='sle_pre_sub_qty'),
    path('get_pre_sub_exam/<int:subject_id>/', views.start_quiz, name='get_pre_exm'),
    path('smt_pre_exam/', views.submit_quiz, name='smt_pre_exm'),
    path('exam_pre_sub_completed/', views.complete_quiz, name='exm_pre_comt'),
   
]

