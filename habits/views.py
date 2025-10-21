from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Max
from .models import Habit, Record
from .forms import HabitForm


def home(request):
    habits = Habit.objects.annotate(last_completed=Max('records__completed_at')).order_by('created_at')
    form = HabitForm()

    if request.method == 'POST':
        form = HabitForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    return render(request, 'habits/home.html', {'habits': habits, 'form': form})


def mark_done(request, habit_id):
    habit = get_object_or_404(Habit, id=habit_id)
    Record.objects.create(habit=habit)
    return redirect('home')

def delete_habit(request, habit_id):
    habit = get_object_or_404(Habit, id=habit_id)
    habit.delete()
    return redirect('home')
