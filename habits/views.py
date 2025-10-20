from django.shortcuts import render

# Create your views here.
from .models import Habit

def home(request):
    habits = Habit.objects.all().order_by('created_at')
    return render(request, 'habits/home.html', {'habits': habits})
