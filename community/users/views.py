from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse, reverse_lazy

from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from users.models import CommunityUser
from django.contrib import messages

from django.contrib.auth import login, logout
from users.forms import CommunityUserCreateForm, UserUpdateForm, CommunityUserUpdateForm
from django.views.generic.edit import UpdateView
from posts.models import Post
# Create your views here.


def signup(request):
    if request.method == 'POST':
        form = CommunityUserCreateForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()  # load the profile instance created by the signal
            username = form.cleaned_data.get('username')
            user.save()
            raw_password = form.cleaned_data.get('password1')
            # user = authenticate(username=username, password=raw_password)
            # login(request, user)
            return redirect('users:login')
    else:
        form = CommunityUserCreateForm()
    return render(request, 'users/signup.html', {'form': form})

@login_required
def profile(request, pk):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = CommunityUserUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.communityuser)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('users:index')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = CommunityUserUpdateForm(instance=request.user.communityuser)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'users/profile.html', context)

@login_required(redirect_field_name=None)
def index(request):
    context = {
        'posts': Post.objects.filter(user=request.user).order_by('-date'),
        'users': CommunityUser.objects.all()
    }
    return render(request, 'index.html',context)

@login_required(redirect_field_name=None)
def files(request):
    files = File.objects.order_by('filename')
    files = {'files': files}
    return render(request, 'users/files.html', context=files)

@login_required(redirect_field_name=None)
def users(request):
    users = CommunityUser.objects.order_by('user')
    users = {'users': users}
    return render(request, 'users/users.html', context=users)
