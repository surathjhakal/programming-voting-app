from django.http.response import JsonResponse
from django.shortcuts import render,redirect
from .models import MySiteUser,CreateProgrammingLanguage

# Create your views here.

def index(request):
    if not request.session.has_key("uid"):
        return redirect("sign_in")
    languages=CreateProgrammingLanguage.objects.all()
    mydict = {
        'languages': languages
    }

    return render(request, 'index.html', context=mydict)

def sign_up(request):
    if request.method == 'POST':
        name = request.POST['user_name']
        email = request.POST['user_email']
        password = request.POST['user_password']
        try:
            user = MySiteUser.objects.get(email=email)
            return render(request, 'signupPage.html', {'message': 'This email id is already registered'})
        except:
                new_user = MySiteUser(name=name, email=email,
                                      password=password)
                new_user.save()
                return render(request, 'signupPage.html', context={'message': 'You have created your account successfully, Now Sign In'})
    return render(request, 'signupPage.html', {'message': ''})


def sign_in(request):
    if request.method == 'POST':
        email = request.POST['user_email']
        password = request.POST['user_password']
        try:
            user = MySiteUser.objects.get(email=email)
            if user.password == password:
                request.session['uid'] = request.POST['user_email']
                return redirect('index')
            else:
                return render(request, 'signinPage.html', {'message': 'Invalid password entered'})
        except:
            return render(request, 'signinPage.html', {'message': 'There is no user with this mail'})
    return render(request, 'signinPage.html', {'message': ''})


def log_out(request):
    del request.session['uid']
    return redirect('index')


def getQuery(request):
    value = request.POST['query']
    langObj=CreateProgrammingLanguage.objects.get(name=value)
    langObj.count=langObj.count+1
    langObj.save()
    updatedlanguages=CreateProgrammingLanguage.objects.all()
    mydict = {
        'languages': updatedlanguages
    }
    return render(request, 'index.html', context=mydict)


def sortdata(request):
    mydict = {
        'languages': CreateProgrammingLanguage.objects.order_by("-count")
    }
    return render(request, 'index.html', context=mydict)
