
from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.models import Group
from .forms import SignUpForm, LoginForm, PostForm
from .models import Post

# home page
def home(request):
    posts = Post.objects.all()
    return render(request, 'blog/home.html',{'posts':posts, 'home':'active'})

# about page
def about(request):
    return render(request, 'blog/about.html',{'about':'active'} )

# contact page
def contact(request):
    return render(request, 'blog/contact.html', {'contact':'active'})

# dashboard page
def dashboard(request):
    if request.user.is_authenticated:
        posts = Post.objects.all()
        user = request.user
        full_name = user.get_full_name()
        gps = user.groups.all()
        return render(request, 'blog/dashboard.html', {'dashboard':'active', 'posts': posts, 'full_name':full_name, 'groups':gps})
    else:
        return HttpResponseRedirect('/login/')

# logout page
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/' , {'home':'active'})

# signup page
def user_signup(request):
    if request.method == 'POST':
        fd=SignUpForm(request.POST)
        if fd.is_valid():
            messages.success(request, "Congratulation..! You have become an Author.")
            messages.success(request, "Go to Login")
            user = fd.save()
            group=Group.objects.get(name='Author')
            user.groups.add(group)
            fd = SignUpForm()
    else:
        fd = SignUpForm()
    return render(request, 'blog/signup.html', {'form':fd,'signup':'active'})

# login page
def user_login(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            fd = LoginForm(request=request, data=request.POST)
            if fd.is_valid():
                u_name = fd.cleaned_data['username']
                u_pw = fd.cleaned_data['password']
                user = authenticate(username=u_name, password=u_pw)
                if user is not None:
                    login(request, user)
                    messages.success(request, "logged in Successful..!!")
                    return HttpResponseRedirect('/dashboard/', {'dashboard':'active'})
        else:
            fd = LoginForm()
        return render(request, 'blog/login.html', {'form': fd, 'login':'active'})
    else:
        return HttpResponseRedirect('/dashboard/', {'dashboard':'active'})

# add new post
def Add_Post(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            fd = PostForm(request.POST)
            if fd.is_valid():
                tl = fd.cleaned_data['title']
                de = fd.cleaned_data['desc']
                pst = Post(title=tl,desc=de)
                messages.success(request, "Post added Successfully..!!")
                pst.save()
                fd = PostForm()
        else:
            fd = PostForm()
        return render(request, 'blog/addpost.html', {'form':fd, 'dashboard':'active'})
    else:
        return HttpResponseRedirect('/login/', {'login':'active'})


# Update  post
def Update_Post(request, id):
    if request.user.is_authenticated:
        if request.method == 'POST':
            pi = Post.objects.get(pk = id)
            fd = PostForm(request.POST, instance=pi)
            if fd.is_valid():
                fd.save()
                messages.success(request, "Post Updated Successfully..!!")
                fd = PostForm()
        else:
            pi = Post.objects.get(pk=id)
            fd = PostForm(instance=pi)
        return render(request, 'blog/updatepost.html', {'form':fd, 'dashboard':'active'})
    else:
        return HttpResponseRedirect('/login/', {'login':'active'})

# Delete  post
def Delete_Post(request, id):
    if request.user.is_authenticated:
        if request.method == 'POST':
            pi = Post.objects.get(pk=id)
            pi.delete()
            messages.warning(request, "Post is deleted..")
        return HttpResponseRedirect('/dashboard/', {'dashboard':'active'})
    else:
        return HttpResponseRedirect('/login/', {'login':'active'})