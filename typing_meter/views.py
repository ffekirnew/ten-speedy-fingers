from django.shortcuts import render
from typing_meter.models import Test, TestText
from random import randint


def index(request):
    latest_text = TestText.objects.all()
    latest_text = latest_text[randint(0, len(latest_text) - 1)]
    context = {'latest_text': latest_text}
    return render(request, 'typing_meter/index.html', context)

def new_entry(request):
    return render(request, 'typing_meter/new_entry.html')

def previous_history(request):
    previous_test_history = Test.objects.all()[:10]
    context = {'previous_test_history': previous_test_history}
    return render(request, 'typing_meter/previous_history.html', context)