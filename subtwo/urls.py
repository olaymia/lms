from django.urls import path
from . import views



urlpatterns = [

    path('sel_para_sub/', views.select_subject, name='para_sub'),
    path('sel_para_qty/<int:subject_id>/', views.select_quantity, name='sle_para_sub_qty'),
    path('get_para_sub_exam/<int:subject_id>/', views.start_quiz, name='get_para_exm'),
    path('smt_para_exam/', views.submit_quiz, name='smt_pre_exm'),
    path('exam_para_sub_completed/', views.complete_quiz, name='exm_para_comt'),
   
]
