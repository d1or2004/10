from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views import View

from .forms import UserLoginForm
from .models import Student
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout


class StudentView(View):
    def get(self, request):
        students = Student.objects.all()
        context = {
            'students': students
        }
        return render(request, 'student.html', context)


class LendingWive(View):
    def get(self, request):
        return render(request, 'landing.html')


class UserRigisterView(View):
    def get(self, request):
        return render(request, 'auth/register.html')

    def post(self, request):
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        username = request.POST['username']
        password_1 = request.POST['password_1']
        password_2 = request.POST['password_2']
        if password_1 == password_2:
            user = User(first_name=first_name, last_name=last_name, email=email, username=username, password=password_1)
            user.set_password(password_1)
            user.save()
            return redirect("login")
        else:
            return render(request, 'auth/register.html')


class LoginView(View):
    def get(self, request):
        return render(request, 'auth/login.html')

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']

        data = {'username': username, 'password': password}

        login_form = AuthenticationForm(data=data)
        if login_form.is_valid():
            user1 = login_form.get_user()
            login(request, user1)
            return redirect('landing')
        else:
            form = UserLoginForm()
            context = {'form': form}
            return render(request, 'auth/login.html', context)


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('landing')

