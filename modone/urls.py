from django.urls import path
from . import views


urlpatterns = [

    path('sel_pre_mod/', views.select_semester, name='pre_mod'),
    path('sel_pre_qty/<int:semester_id>/', views.select_semester_quantity, name='sel_pre_mod_qty'),
    path('get_mod_exam/<int:semester_id>/<int:num_questions>/', views.start_semester_quiz, name='get_pre_mod_exm'),


]