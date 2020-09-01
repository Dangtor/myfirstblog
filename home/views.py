from django.shortcuts import render

# Create your views here.

def home_view(request):
    if request.user.is_authenticated:

        context = {
            'ad': "Mahir"

        }
    else:
        context = {
            'ad': 'Qonaq'
        }
    return render(request, 'home.html', context)