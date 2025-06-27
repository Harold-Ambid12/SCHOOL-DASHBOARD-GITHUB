from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('student/register/', views.student_register, name='student_register'),
    path('teacher/register/', views.teacher_register, name='teacher_register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('student/dashboard/', views.student_dashboard, name='student_dashboard'),
    path('teacher/dashboard/', views.teacher_dashboard, name='teacher_dashboard'),
    path('teacher/mark/<int:student_id>/', views.mark_attendance, name='mark_attendance'),
    
    # Attendance management URLs for teachers
    path('teacher/attendance/', views.attendance_list, name='attendance_list'),
    path('teacher/attendance/edit/<int:pk>/', views.edit_attendance, name='edit_attendance'),
    path('teacher/attendance/delete/<int:pk>/', views.delete_attendance, name='delete_attendance'),
]
