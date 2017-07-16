from django.shortcuts import render, HttpResponse, redirect
from django.utils.crypto import get_random_string

def index(request):
    if 'attempts' not in request.session:
        request.session['attempts'] = 1
    if 'random_str' not in request.session:
        request.session['random_str'] = get_random_string(length=14)
    return render(request, 'random_word_gen/index.html')

def attempts(request):
    request.session['attempts'] += 1
    request.session['random_str'] = get_random_string(length=14)
    return redirect('/')

def reset(request):
    request.session['attempts'] = 1;
    request.session['random_str'] = get_random_string(length=14)
    return redirect('/')