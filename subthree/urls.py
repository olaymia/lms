from django.urls import path
from . import views



urlpatterns = [

    path('sel_clinical_sub/', views.select_subject, name='clinical_sub'),
    path('sel_clinical_qty/<int:subject_id>/', views.select_quantity, name='sle_clinical_sub_qty'),
    path('get_clinical_sub_exam/<int:subject_id>/', views.start_quiz, name='get_clinical_exm'),
    path('smt_clinical_exam/', views.submit_quiz, name='smt_clinical_exm'),
    path('exam_clinical_sub_completed/', views.complete_quiz, name='exm_clinical_comt'),
   
]
