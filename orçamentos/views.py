from django.shortcuts import render

def home(request):
    
    
    return render(request, 'orçamentos/pages/home.html')
