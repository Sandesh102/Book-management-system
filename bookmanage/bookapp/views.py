from django.shortcuts import render,redirect
from .models import*
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

@login_required(login_url="/login")
def book(request):
    if request.method == "POST":
        data = request.POST
        book_image = request.FILES.get('book_image')
        book_name = data.get('book_name')
        book_description = data.get('book_description')
        Book.objects.create(
            book_description=book_description,
            book_image=book_image,
            book_name=book_name,
        )
        return redirect('/book/')
    queryset=Book.objects.all()
    context={'books':queryset}
    return render(request,'books.html',context)
def delete_book(request, id):
    queryset=Book.objects.get(id=id)
    queryset.delete()
    return redirect('/book/')

def update_book(request, id):
    queryset=Book.objects.get(id=id)
    
    if request.method == "POST":
        data=request.POST
        book_image=request.FILES.get('book_image')
        book_name=data.get('book_name')
        book_description=data.get('book_description')
        
        queryset.book_name=book_name
        queryset.book_description=book_description
        
        if book_image:
            queryset.book_image=book_image
            
        queryset.save()
        return redirect('/book/')
    context = {'book': queryset}
    return render(request, 'updatebooks.html',context)


def register_page(request):
    
     if request.method=="POST":
         first_name=request.POST.get('first_name')
         last_name=request.POST.get('last_name')
         username=request.POST.get('username')
         password=request.POST.get('password')
         
         user=User.objects.filter(username=username)
         
         if user.exists():
             messages.info(request,'Username already taken ')
             return redirect('/register/')
         
         user= User.objects.create(
             first_name=first_name,
             last_name=last_name,
             username= username,
             
          )
         
         user.set_password(password)
         user.save()
         
         messages.info(request,'Account created.')
         
         return redirect('/login/')
     return render(request,'register.html')
 

def login_page(request):
    
     if request.method=="POST":
         username=request.POST.get('username')
         password=request.POST.get('password')
         
         if not User.objects.filter(username=username).exists():
             messages.error(request,'Invalid username')
             return redirect('/login/')
         
         user=authenticate(username=username, password=password)  #authenticate is a function in django that is used to check whether password and username is correct .
         
         if user is None:
             messages.error(request,'Invalid password')
             return redirect('/login/')
         else:
             login(request,user)      ##login method is used to maintain the session that is next time y loggedin it will recognize y.
             return redirect('/book/')
             
     return render(request,'login.html')
def logout_page(request):
    logout(request)
    return redirect('/login/')