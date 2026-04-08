from django.shortcuts import render
from .forms import PredictionForm
from .ml_pipeline import get_prediction

def index(request):
    form = PredictionForm()
    return render(request, 'index.html', {'form': form})

def predict(request):
    if request.method == "POST":
        form = PredictionForm(request.POST)
        if form.is_valid():
            user_input = form.save(commit=False)
            
            # Simple feature hashing for Dummy ML
            def mock_hash(string_val):
                return (hash(str(string_val)) % 100) / 100.0
                
            features = [
                mock_hash(user_input.current_intent),
                mock_hash(user_input.sleep_quality),
                mock_hash(user_input.previous_action),
                mock_hash(user_input.action_3_hours_ago),
                mock_hash(user_input.gender)
            ]
            
            # Use random forest by default
            prediction_class = get_prediction('random_forest', features)
            
            outcomes = {
                0: {"state": "Low Energy / Rest Needed", "action": "Take a 20-min break or read a book.", "forecast": "Likely to feel lethargic if forced to work."},
                1: {"state": "High Motivation / Energetic", "action": "Tackle a challenging analytical task.", "forecast": "High productivity and deep focus."},
                2: {"state": "Creative Flow / Distracted", "action": "Brainstorm ideas or organize your thoughts.", "forecast": "Bursts of insight but easily derailed."}
            }
            
            outcome = outcomes.get(prediction_class, outcomes[0])
            
            user_input.predicted_state = outcome["state"]
            user_input.suggested_action = outcome["action"]
            user_input.forecast_1hr = outcome["forecast"]
            user_input.save()
            
            context = {
                'prediction': user_input.predicted_state,
                'suggestion': user_input.suggested_action,
                'forecast': user_input.forecast_1hr,
            }
            return render(request, 'partials/prediction_result.html', context)
    return render(request, 'partials/prediction_result.html', {'error': 'Invalid Form Submission'})
