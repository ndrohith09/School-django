from django.shortcuts import render , redirect 
from .models import * 
from django.contrib import messages
from django.contrib.auth.models import User , auth
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail



def login(request):    
    if request.user.is_authenticated:
        return redirect('/')

    else:
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']

            try:
                user = auth.authenticate(username = User.objects.get(email=username) , password = password)
            except:
                user = auth.authenticate(username =username, password = password) 
            if user is not None:
                auth.login(request , user)
                return redirect('/login/')

            else:
                messages.info(request ,'Invalid credintials')
                return redirect('/login/')

        else:
            return render(request , 'login.html' , context={})

def logout(request):       
    auth.logout(request)
    return redirect('/')
    
def home (request):
    return render(request , 'home.html')

def admission(request):
    if request.method == "POST":
            fullname = request.POST["fullname"]
            username = request.POST["username"]
            email = request.POST["email"]
            phonenumber = request.POST["phonenumber"]
            password1 = request.POST["password1"]
            password2 = request.POST["password2"]
            gender = request.POST["gender"]

            p = Admission(fullname=fullname, username=username , email=email,phonenumber=phonenumber,password1=password1,password2=password2,gender=gender)
            p.save()
            return redirect('/')
    return render(request , 'admission.html')

def academics(request):
    return render (request ,'ACADEMICS.html')

def facilities(request):
    return render(request , 'FACILITIES.html')


def faculty(request):
    return render(request , 'FACULTY.html')


def gallery(request):
    images= Gallery.objects.all()
    return render(request , 'gallery.html',context={"image":images})

def hostel(request):
    return render(request , 'HOSTEL.html')

def labs(request):
    return render(request , 'LABS.html')

def sports(request):
    return render(request , 'SPORTS.html')
    
def about(request):
    return render(request , 'about us.html')

def contact(request):
        if request.method == 'POST':
            firstname = request.POST['firstname']
            lastname= request.POST['lastname']
            country = request.POST['country']
            subject = request.POST['subject']

            data = {
            'firstname':firstname ,
            'lastname':lastname,
            'country':country ,
            'subject':subject,
            }
            message = '''
            --------------
            CONTACT FORM
            --------------
            FirstName:{}
            LastName:{}
            NEW MESSAGE: {}
            Country:{}
            --------------
            '''.format(data['firstname'],data['lastname'],data['subject'],data['country'])
            send_mail(data['firstname'], message,'',['yeddala.e0120024@sret.edu.in'])  #recepitents email
            return redirect('/')

        return render(request , 'contact.html')

def signup(request):
    if request.user.is_authenticated:
        return redirect('/')

    else:
        if request.method == 'POST':
            username = request.POST['username']
            email = request.POST['email']
            password1 = request.POST['password1']
            password2 = request.POST['password2']

            if password1 == password2:
                if User.objects.filter( username= username).exists():
                    messages.info(request ,'Username Taken')
                    print('username taken')
                    return redirect('/signup/')
                elif User.objects.filter(email= email).exists():
                    print('email taken')
                    messages.info(request ,'email taken')
                    return redirect('/signup/')
                else:
                    user = User.objects.create_user(username = username ,email = email , password = password1)
                    user.save()
                    messages.info(request ,'User Created')
                    print('user created')
                
            
            else:
                print('password not matching')
                messages.info(request,'password not matching')
                return redirect('/signup/')
            return redirect('/login/')
        
        else:
            return render(request , 'signup.html')
