from django.shortcuts import render
from .forms import SignUpForm
from .forms import LoginForm
# Create your views here.


def SignUp(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'loginpage.html', {'form': form})
    else:
        form = SignUpForm()
    return render(request, 'SignUp.html', {'form': form})


from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .forms import LoginForm


def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                # Redirect to a success page or dashboard
                return redirect('mainpage/')  # Change 'mainpage/' to the appropriate URL name
            else:
                # Handle invalid login credentials
                messages.error(request, "Invalid username or password.")
    else:
        form = LoginForm()

    return render(request, 'loginpage.html', {'form': form})


def homepage(request):
    return render(request, 'homepage.html')
def about(request):
    return render(request, 'aboutus.html')


def profile(request):
    return render(request, 'profile.html')


from .models import User


def mainpage(request):
    users = User.objects.all()
    return render(request, 'mainpage.html', {'users': users})


from django.shortcuts import render, redirect
from .forms import BookForm
from .models import Book

def book_list(request):
    books = Book.objects.all()
    return render(request, 'book_list.html', {'books': books})

def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm()
    return render(request, 'add_book.html', {'form': form})
