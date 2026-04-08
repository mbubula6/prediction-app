from django import forms
from .models import UserInput

class PredictionForm(forms.ModelForm):
    class Meta:
        model = UserInput
        fields = [
            'name', 
            'gender', 
            'preferences', 
            'current_intent', 
            'previous_action', 
            'action_3_hours_ago', 
            'sleep_quality',
            'device_type',
            'browser',
            'os',
            'weather',
            'temperature'
        ]
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Your Name'}),
            'gender': forms.Select(choices=[('', 'Select...'), ('M', 'Male'), ('F', 'Female'), ('O', 'Other')], attrs={'class': 'form-input'}),
            'preferences': forms.Textarea(attrs={'class': 'form-input', 'rows': 2, 'placeholder': 'Any specific preferences?'}),
            'current_intent': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'What do you want to do right now?'}),
            'previous_action': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'What were you doing before this?'}),
            'action_3_hours_ago': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'What were you doing 3 hours ago?'}),
            'sleep_quality': forms.Select(choices=[
                ('great', 'Great'),
                ('good', 'Good'),
                ('okay', 'Okay'),
                ('bad', 'Bad'),
                ('terrible', 'Terrible')
            ], attrs={'class': 'form-input'}),
            'device_type': forms.HiddenInput(),
            'browser': forms.HiddenInput(),
            'os': forms.HiddenInput(),
            'weather': forms.HiddenInput(),
            'temperature': forms.HiddenInput()
        }
