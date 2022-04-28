from django.shortcuts import render

# Create your views here.
def LearnDjango(request):
    return render(request,'learnDjango/index.html' )