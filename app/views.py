from django.shortcuts import render
from .forms import PredictionForm
import time

def index(request):
    form = PredictionForm()
    return render(request, 'index.html', {'form': form})

def predict(request):
    if request.method == "POST":
        form = PredictionForm(request.POST)
        if form.is_valid():
            # In a real app, you'd pass form.cleaned_data to ML Pipeline
            # For now, simulate delay and return dummy prediction
            time.sleep(1) # Simulate ML overhead
            
            user_input = form.save(commit=False)
            
            # Dummy predictions
            user_input.predicted_state = "High Motivation / Energetic"
            user_input.suggested_action = "Tackle a challenging task or exercise"
            user_input.forecast_1hr = "Likely to feel accomplished and relaxed"
            user_input.save()
            
            context = {
                'prediction': user_input.predicted_state,
                'suggestion': user_input.suggested_action,
                'forecast': user_input.forecast_1hr,
            }
            return render(request, 'partials/prediction_result.html', context)
    return render(request, 'partials/prediction_result.html', {'error': 'Invalid Form Submission'})
