from django.shortcuts import render
from datetime import datetime

def show_time(request):
    context = {
        'time': datetime.strptime('Mar 24 2021 3:44 PM', '%b %d %Y %I:%M %p')
    }

    return render(request, 'index.html', context)