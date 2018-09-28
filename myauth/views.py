from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

from .forms import UserLoginForm, UserSignupForm


def user_signup(request):
    if request.method == 'POST':
        forms = UserSignupForm(request.POST)
        if forms.is_valid():
            # collect forms data
            username = forms.cleaned_data["username"]
            password = forms.cleaned_data["password"]
            re_password = forms.cleaned_data["re_password"]
            email = forms.cleaned_data["email"]

            # Check both password is same
            if password != re_password:
                errMsg = "Password and Re Password not same"
                context = {'errMsg': errMsg, 'forms': forms}
                return render(request, 'myauth/user_signup.html', context)
            
            # Create new User
            User.objects.create_user(username, email, password)
            return redirect('user-login')


    forms = UserSignupForm()
    context = {'forms': forms}
    return render(request, 'myauth/user_signup.html', context)



def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]

            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return redirect('student_list_urls')
            else:
                errMsg = "Username or Password Invalid"
                context = {'errMsg': errMsg, 'forms': form}
                return render(request, 'myauth/user_login.html', context)

    form = UserLoginForm()
    context = {'forms': form}
    return render(request, 'myauth/user_login.html', context)

def user_logout(request):
    logout(request)
    return redirect('user-login')
