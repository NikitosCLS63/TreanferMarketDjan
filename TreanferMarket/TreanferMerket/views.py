from django.shortcuts import render
def info_view(request):
    return render(request, 'info.html')
def index_view(request):
    return render(request, 'index.html')
# Create your views here.
