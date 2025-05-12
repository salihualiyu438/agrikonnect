from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages

# Create your views here.


########   SIGN UP FUNCTION   ##########
def sign_up(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        # check if the passwords match
        if password1 == password2:

            # proceed to check if username and email have not been taken
            if User.objects.filter(username=username).exists():
                messages.info(request, 'the username has been taken')
                return redirect('sign_up')
            
            elif User.objects.filter(email = email).exists():
                messages.info(request, 'this email has been taken')
                return redirect('sign_up')
                
            else:
                user = User.objects.create_user(username=username, password=password1, email=email, last_name=last_name, first_name=first_name)
                user.save()
                return redirect('login')

        else:
            print('passwords not matching')
            return redirect('sign_up')

    else:
        return render(request, 'signUp.html')
    
###### LOGIN FUNCTION   ##########

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password = password)

        if user is not None:
    
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'invalid credentials')
            return redirect('login')
    else:
        return render(request, 'login.html')
    
###########  LOGOUT FUNCTION   ##########

def logout(request):
    auth.logout(request)
    return redirect('/')
    



