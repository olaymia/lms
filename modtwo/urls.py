from django.urls import path
from . import views


urlpatterns = [

    path('sel_para_mod/', views.select_semester, name='para_mod'),
    path('sel_para_qty/<int:semester_id>/', views.select_semester_quantity, name='sel_para_mod_qty'),
    path('get_mod_exam/<int:semester_id>/<int:num_questions>/', views.start_semester_quiz, name='get_para_mod_exm'),


]