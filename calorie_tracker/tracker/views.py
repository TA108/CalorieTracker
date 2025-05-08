from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from .forms import SignUpForm, FoodItemForm, FoodLogForm
from .models import FoodLog, FoodItem
from django.contrib.auth.decorators import login_required
from django.db.models import Count, Max,  F


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'tracker/signup.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'tracker/login.html', {'form': form})


@login_required
def user_logout(request):
    if request.method == 'POST':
        logout(request)
        return redirect('login')
        

@login_required
def home(request):
    return render(request, 'tracker/home.html')

@login_required
def add_food_item(request):
    if request.method == 'POST':
        form = FoodItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = FoodItemForm()
    return render(request, 'tracker/add_food_item.html', {'form': form})


@login_required
def add_food_log(request):
    if request.method == 'POST':
        form = FoodLogForm(request.POST)
        if form.is_valid():
            food_log = form.save(commit=False)
            food_log.user = request.user
            food_log.save()
            return redirect('home')
    else:
        form = FoodLogForm()
    return render(request, 'tracker/add_food_log.html', {'form': form})


@login_required
def foods_logged(request):
    logs = (
        FoodLog.objects
        .filter(user=request.user)
        .values(
            'food_item__name',
            'food_item__calories',
            'food_item__protein',
            'food_item__carbohydrates',
            'food_item__fats'
        )
        .annotate(latest_date=Max('date'))
        .order_by('-latest_date')
    )
    return render(request, 'tracker/foods_logged.html', {'logs': logs})


@login_required
def progress_chart(request):
    logs = FoodLog.objects.filter(user=request.user)
    return render(request, 'tracker/progress_chart.html', {'logs': logs})