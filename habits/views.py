from django.shortcuts import render, redirect
from .models import Habit
from .forms import HabitForm

def home(request):
    habits = Habit.objects.all().order_by('created_at')
    form = HabitForm()

    if request.method == 'POST':
        form = HabitForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    return render(request, 'habits/home.html', {'habits': habits, 'form': form})
