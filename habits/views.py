from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.utils import timezone
from django.db.models import Max
from .models import Habit, Record
from .forms import HabitForm


def home(request):
    habits = Habit.objects.annotate(last_completed=Max('records__completed_at')).order_by('created_at')
    form = HabitForm()

    total_habits = habits.count()
    today = timezone.now().date()
    habits_done_today = Record.objects.filter(completed_at__date=today).values('habit').distinct().count()

    if request.method == 'POST':
        form = HabitForm(request.POST)
        if form.is_valid():
            habit = form.save()
            messages.success(request, f'✅ "{habit.name}" has been added!')
            return redirect('home')

    context = {
        'habits': habits,
        'form': form,
        'total_habits': total_habits,
        'habits_done_today': habits_done_today,
    }
    return render(request, 'habits/home.html', context)


def mark_done(request, habit_id):
    habit = get_object_or_404(Habit, id=habit_id)
    Record.objects.create(habit=habit)
    messages.success(request, f'🎉 You marked "{habit.name}" as done!')
    return redirect('home')


def delete_habit(request, habit_id):
    habit = get_object_or_404(Habit, id=habit_id)
    habit.delete()
    messages.warning(request, f'🗑️ "{habit.name}" has been deleted.')
    return redirect('home')
