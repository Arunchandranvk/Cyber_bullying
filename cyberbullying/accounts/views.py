# ml_app/views.py
from django.shortcuts import render
from django.http import HttpResponse
import pickle
from .forms import InputForm

def home(request):
    form = InputForm()
    return render(request, 'home.html', {'form': form})

def predict(request):
    if request.method == 'POST':
        form = InputForm(request.POST)
        if form.is_valid():
            # Get the input text from the form
            text = form.cleaned_data['text']
            # Load the TF-IDF vectorizer and the model
            with open('tfidf_vectorization', 'rb') as f:
                tfidf = pickle.load(f)
            with open('model', 'rb') as f:
                model = pickle.load(f)
            # Preprocess the text (similar to what you did before)
            # Vectorize the text
            text = tfidf.transform([text])
            # Make predictions
            prediction = model.predict(text)
            if prediction == 0:
                prediction= "The Text Mentioned Is Not Cyberbullying"
            else:
                prediction= "Cyberbullying"
            # Render the result
            return render(request, 'home.html', {'prediction': prediction})
    else:
        form = InputForm()
    return render(request, 'home.html', {'form': form})
