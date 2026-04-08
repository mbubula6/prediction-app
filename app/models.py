from django.db import models
from django.contrib.auth.models import User

class UserInput(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    # Form Data
    name = models.CharField(max_length=100)
    gender = models.CharField(max_length=50, blank=True, null=True)
    preferences = models.TextField(blank=True, null=True)
    current_intent = models.CharField(max_length=255, verbose_name="What do you want to do right now?")
    previous_action = models.CharField(max_length=255, verbose_name="What were you doing before entering this site?")
    action_3_hours_ago = models.CharField(max_length=255, verbose_name="What were you doing 3 hours ago?")
    sleep_quality = models.CharField(max_length=100, verbose_name="Did you sleep well today?")

    # Auto Metadata
    created_at = models.DateTimeField(auto_now_add=True)
    season = models.CharField(max_length=50, blank=True, null=True)
    weather = models.CharField(max_length=100, blank=True, null=True)
    temperature = models.FloatField(blank=True, null=True)
    device_type = models.CharField(max_length=50, blank=True, null=True)
    browser = models.CharField(max_length=100, blank=True, null=True)
    os = models.CharField(max_length=100, blank=True, null=True)

    # Output / Predictions
    predicted_state = models.CharField(max_length=255, blank=True, null=True)
    suggested_action = models.CharField(max_length=255, blank=True, null=True)
    forecast_1hr = models.CharField(max_length=255, blank=True, null=True)
    
    def __str__(self):
        return f"{self.name} - {self.created_at.strftime('%Y-%m-%d %H:%M')}"
