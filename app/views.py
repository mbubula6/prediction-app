from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from .forms import PredictionForm
from .models import UserInput
from .ml_pipeline import get_prediction

@login_required(login_url='/login/')
def index(request):
    form = PredictionForm()
    return render(request, 'index.html', {'form': form})

@login_required(login_url='/login/')
def history(request):
    user_inputs = UserInput.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'history.html', {'user_inputs': user_inputs})

@login_required(login_url='/login/')
def predict(request):
    if request.method == "POST":
        form = PredictionForm(request.POST)
        # Check toggle choice from hidden input or form body, default to global logic later if implemented
        is_global = request.POST.get('use_global', 'false') == 'true'
        
        if form.is_valid():
            user_input = form.save(commit=False)
            user_input.user = request.user
            
            # Simple feature hashing for Dummy ML
            def mock_hash(string_val):
                return (hash(str(string_val)) % 100) / 100.0
                
            features = [
                mock_hash(user_input.current_intent),
                mock_hash(user_input.sleep_quality),
                mock_hash(user_input.previous_action) + mock_hash(user_input.device_type), 
                mock_hash(user_input.action_3_hours_ago),
                mock_hash(user_input.gender) + mock_hash(user_input.os) 
            ]
            
            # Select appropriate model file
            model_name = 'global_model' if is_global else f'personal_{request.user.id}'
            prediction_class = get_prediction(model_name, features)
            
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

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('index')
    else:
        form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')
