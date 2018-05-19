from django.shortcuts import render, HttpResponse, redirect
from time import gmtime, strftime
from datetime import date, datetime
from .models import users
from django.contrib import messages
# users.objects.create(fname = "Grooby", lname = "Mcbuckets", email = "grooby@mail.com" )
# users.objects.create(fname = "snookel", lname = "batboy" , email = "batboy@mail.com")
# users.objects.create(fname = "gluk", lname = "mkruk" , email = "ghat@mail.com")
# users.objects.create(fname = "poof", lname = "D'Scroof" , email = "sroo@mail.com")
def index(request):
    queries = users.objects.all().order_by("created_at")
    context = {'users' : queries}
    return render(request, "django_app/users.html", context)
def new(request):
    return render(request,"django_app/add_user.html")
def update(request,id):
    if request.method == "POST":
        errors = users.objects.basic_validator(request.POST)
        if len(errors):
            for error in errors:
                messages.add_message(request, messages.INFO, error)
        else:
            this_user = users.objects.get(id = str(id))
            this_user.fname = request.POST['fname']
            this_user.lname = request.POST['lname']
            this_user.email = request.POST['email']
        return redirect(("/users/"+id))
    else:
        return redirect(("/users/"+id))
def create(request):
    if request.method == "POST":
        errors = users.objects.basic_validator(request.POST)
        if len(errors):
            for error in errors:
                messages.add_message(request, messages.INFO, error)
        else:
            users.objects.create(fname = request.POST['fname'], lname = request.POST['lname'], email = request.POST['email'])
        return redirect(("/users"))
    else:
        return redirect(("/users"))
    return redirect('/')
def show(request, id):
    this_user = users.objects.get(id = str(id))
    print('SHOW::',this_user)
    context = {'ID' : this_user.id,
                'full_name' : (this_user.fname + this_user.lname),
                'email' : this_user.email,
                'created_at' : this_user.created_at}
    return render(request,"django_app\show_user.html", context)
def edit(request, id):
    this_user = users.objects.get(id = str(id))
    print('EDIT::',this_user)
    context = {'ID' : this_user.id,
                'fname' : this_user.fname,
                'lname' : this_user.lname,
                'email' : this_user.email,
                'created_at' : this_user.created_at}
    return render(request, "django_app\edit_user.html", context)
def destroy(request, id):
    this_user = users.objects.get(id = str(id))
    print('DESTROY::',this_user)
    this_user.delete()
    return redirect('/users')