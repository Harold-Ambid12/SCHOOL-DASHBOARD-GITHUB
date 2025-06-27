# school/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from .forms import StudentRegisterForm, TeacherRegisterForm, LoginForm
from .models import Attendance, CustomUser
from django.contrib.auth.decorators import login_required

def student_register(request):
    if request.method == 'POST':
        form = StudentRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = StudentRegisterForm()
    return render(request, 'school/student_register.html', {'form': form})

def teacher_register(request):
    if request.method == 'POST':
        form = TeacherRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = TeacherRegisterForm()
    return render(request, 'school/teacher_register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            if request.user.user_type == 'student':
                return redirect('student_dashboard')
            else:
                return redirect('teacher_dashboard')
    else:
        form = LoginForm()
    return render(request, 'school/login.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('login')

@login_required
def student_dashboard(request):
    records = Attendance.objects.filter(student=request.user)
    return render(request, 'school/student_dashboard.html', {'records': records})

@login_required
def teacher_dashboard(request):
    students = CustomUser.objects.filter(user_type='student')
    return render(request, 'school/teacher_dashboard.html', {'students': students})

@login_required
def mark_attendance(request, student_id):
    student = CustomUser.objects.get(id=student_id)
    if request.method == 'POST':
        status = request.POST['status']
        Attendance.objects.create(student=student, status=status)
        return redirect('teacher_dashboard')
    return render(request, 'school/mark_attendance.html', {'student': student})


def home(request):
    return render(request, 'school/home.html')
