from django.db import models

# Create your models here.
class Habit(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
class Record(models.Model):
    habit = models.ForeignKey('Habit', on_delete=models.CASCADE, related_name='records')
    completed_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.habit.name} - {self.completed_at.strftime('%Y-%m-%d %H:%M')}"
