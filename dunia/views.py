from django.shortcuts import render

# Create your views here.
def garden(request):
    return render(request, 'garden.html')

