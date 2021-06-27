from django.shortcuts import render
from django.http import HttpResponse
from .forms import InputForm
import pandas as pd
import numpy as np
import pickle
from sklearn.linear_model import LogisticRegression



# Create your views here.

# Loading Simple Logistic Regression Model
lr_model = pickle.load(open('./models/LR_model.sav', 'rb'))

# Loading Probabilistic Model
with open('./models/heart_disease_model1.pkl', 'rb') as buff:
    PMLmodel_data = pickle.load(buff)

# Obtaining Model and Model trace from loaded Probabilistic Model
PML_loadModel1, PML1_trace = PMLmodel_data['model'], PMLmodel_data['trace']

def index(request):
    if request.method == "POST":
        myform = InputForm(request.POST)
        if myform.is_valid():
            cp = myform.cleaned_data['cp_value']
            thalach = myform.cleaned_data['thalach_value']
            exang = myform.cleaned_data['exang_value']
            oldpeak = myform.cleaned_data['oldpeak_value']
            slope = myform.cleaned_data['slope_value']
            thal = myform.cleaned_data['thal_value']
            # Uncomment and use the target below to test app functions
            # target = 1 + cp + thalach + exang + oldpeak + slope + thal
            m_inputs = [[cp, thalach, exang, oldpeak, slope, thal]]
            target = lr_model.predict(m_inputs)
            return render(request, 'index.html', {'prediction': target})
    else:
        myform = InputForm()

    return render(request, 'index.html', {'form': myform})
