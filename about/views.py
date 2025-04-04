from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import AboutUs, TeamMember

def about(request):
    # Fetch all AboutUs data
    abouts = AboutUs.objects.all()
    
    # Fetch all TeamMember data
    team_members = TeamMember.objects.all()
    
    context = {
        'abouts': abouts,
        'team_members': team_members
    }
    
    # Render the template with the context data
    return render(request, 'about.html', context)
