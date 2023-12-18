from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages


@login_required(login_url="login")
def HomePage(request):
    return render(request, "home.html")


def SignupPage(request):
    if request.method == "POST":
        uname = request.POST.get("username")
        email = request.POST.get("email")
        pass1 = request.POST.get("password1")
        pass2 = request.POST.get("password2")
        if uname and pass1 and pass2:
            if pass1 == pass2:
                if not User.objects.filter(username=uname).exists():
                    my_user = User.objects.create_user(uname, email, pass1)
                    my_user.save()
                    messages.success(request, "Register Succesfully!!!")
                    return redirect("login")
                else:
                    messages.info(request, "Username is already taken")
            else:
                messages.info(request, "Passwords do not match")
        else:
            messages.info(request, "All fields must be filled")

    return render(request, "signup.html")


def LoginPage(request):
    if request.method == "POST":
        username = request.POST.get("username")
        pass1 = request.POST.get("pass")
        user = authenticate(request, username=username, password=pass1)
        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            messages.info(request, "Username or Password is incorrect!!!")

    return render(request, "login.html")

def LogoutPage(request):
    logout(request)
    return redirect("login")

def logpage(request):
    return redirect("home")

def about(request):
    return render(request, 'about.html')
def logabout(request):
    return redirect("home")
def contact(request):
    return render(request, 'contact.html')
def logcontact(request):
    return redirect("home")

        
from django.shortcuts import render, get_object_or_404
from .models import UploadedImage

def view_image(request, image_id):
    image = get_object_or_404(UploadedImage, id=image_id)
    return render(request, 'view_image.html')

from django.shortcuts import render, redirect
from .forms import ImageUploadForm
from .models import UploadedImage

def upload_image(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('view_image', image_id=form.instance.id)
    else:
        form = ImageUploadForm()

    return render(request, 'upload_image.html', {'form': form})

def view_image(request, image_id):
    image = UploadedImage.objects.get(id=image_id)
    return render(request, 'view_image.html', {'image': image})

from django.shortcuts import render, get_object_or_404
from .models import UploadedImage
import cv2
import numpy as np
import base64

def process_image(img):
    img_copy = img.copy()
    img_copy[::2, ::2] = [0, 0, 255]  
    _, buffer = cv2.imencode('.png', cv2.cvtColor(img_copy, cv2.COLOR_BGR2RGB))
    manipulated_image_data = base64.b64encode(buffer).decode('utf-8')
    return manipulated_image_data

def view_image(request, image_id):
    image = get_object_or_404(UploadedImage, id=image_id)

    img_path = image.image.path
    img = cv2.imread(img_path)

    manipulated_image_data = process_image(img)

    return render(request, 'view_image.html', {
        'image': image,
        'original_image_data': image.image.url,
        'manipulated_image_data': manipulated_image_data,
    })

def back(request):
    return redirect("upload_image")

from django.shortcuts import render

def check(request):
    forgery_detected = True 
    context = {
        'forgery_detected': forgery_detected,
    }

    return render(request, 'forgery_result.html', context)

def backk(request):
    return redirect("upload_image")


def Check(request):
    forgery_detected = True  
    context = {
        'forgery_detected': forgery_detected,
    }
    return render(request, 'fogery_result.html', context)
