from django.shortcuts import render
from timeschedulingweb.models import TimeSlots
from django.utils import timezone

# Create your views here.
def index(request):

    # query th upcoming date TODO
    upcoming_appointments = TimeSlots.objects.filter(
        start_time__gte = timezone.now()).order_by('start_time')
    
    context = {
        'upcoming_appointment' : upcoming_appointments.first(),
        'description': upcoming_appointments.first().description,
        'list_upcoming': len(upcoming_appointments)
    }
    
    
    return render(request, 'home.html', context)