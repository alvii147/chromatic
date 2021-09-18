from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.conf import settings

from .forms import UserRegisterForm
from .models import Post, Face
from .utils import get_faces

def home(request):
    context = {
        'posts': Post.objects.all(),
    }
    return render(request, 'chromatic_app/home.html', context)

def login(request):
    return render(request, 'chromatic_app/login.html')

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')

            return redirect('chromatic_app_login')
    else:
        form = UserRegisterForm()

    context = {
        'form' : form,
    }

    return render(request, 'chromatic_app/register.html', context)

@login_required(login_url='chromatic_app_login')
def upload(request):
    if request.method == 'POST':
        caption = request.POST.get('caption', '')
        image = request.FILES.get('imagefile')

        post = Post(
            uploader=request.user,
            caption=caption,
            image=image,
        )
        post.save()

        faces = get_faces(str(image))
        for (x, y, w, h) in faces:
            face = Face(
                post=post,
                topLeftX=x,
                topLeftY=y,
                width=w,
                height=h,
            )
            face.save()

        return redirect('chromatic_app_home')

    return render(request, 'chromatic_app/upload_image.html')