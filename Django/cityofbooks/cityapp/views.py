from django.shortcuts import render, redirect, get_object_or_404
from .models import bookModel
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from .forms import CreateUserForm
from django.contrib import messages

def index(request):

    obj1 = bookModel.objects.get(id=1)
    obj2 = bookModel.objects.get(id=2)
    obj3 = bookModel.objects.get(id=3)
    obj4 = bookModel.objects.get(id=4)
    obj5 = bookModel.objects.get(id=5)
    obj6 = bookModel.objects.get(id=6)
    obj7 = bookModel.objects.get(id=7)
    context = {
        "object1": obj1,
        "object2": obj2,
        "object3": obj3,
        "object4": obj4,
        "object5": obj5,
        "object6": obj6,
        "object7": obj7,
    }

    return render(request, "index.html", context)

def book1(request):
    return render(request, "books/book1.html", {})
def book2(request):
    return render(request, "books/book2.html", {})
def book3(request):
    return render(request, "books/book3.html", {})
def book4(request):
    return render(request, "books/book4.html", {})
def book5(request):
    return render(request, "books/book5.html", {})
def book6(request):
    return render(request, "books/book6.html", {})
def book7(request):
    return render(request, "books/book7.html", {})

def loginPage(request):
	if request.user.is_authenticated:
		return redirect('homepage')
	else:
		if request.method == 'POST':
			username = request.POST.get('username')
			password = request.POST.get('password')

			user = authenticate(request, username = username, password = password)

			if user is not None:
				login(request, user)
				return redirect('homepage')
			else:
				messages.info(request, 'Username of password is incorrect.')

		context = {}
		return render(request, "login.html", context)

def logoutUser(request):
    logout(request)
    return redirect('login')

def register(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Account created successfully!")
            return redirect('login')

    context = {'form': form}
    return render(request, "register.html", context)