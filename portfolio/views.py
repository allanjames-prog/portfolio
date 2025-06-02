# views.py
from django.shortcuts import render
from .models import Project, Skill, Education, Experience, ContactMessage
from django.core.mail import send_mail
from django.conf import settings
from django.shortcuts import get_object_or_404

def portfolio_home(request):
    projects = Project.objects.filter(featured=True)[:6]
    all_skills = Skill.objects.all().order_by('-display_order')
    education = Education.objects.all().order_by('-end_date')
    experience = Experience.objects.all().order_by('-start_date')

    categories = {
        'Programming Languages': {
            'icon': 'fas fa-code',
            'skills': all_skills.filter(category='PROGRAMMING')
        },
        'Web Development': {
            'icon': 'fas fa-laptop-code',
            'skills': all_skills.filter(category='WEB')
        },
        'Databases & Tools': {
            'icon': 'fas fa-database',
            'skills': all_skills.filter(category__in=['DATABASE', 'TOOLS'])
        },
        'Other Skills': {
            'icon': 'fas fa-cogs',
            'skills': all_skills.filter(category='OTHER')
        }
    }

    context = {
        'projects': projects,
        'categories': categories,
        'education': education,
        'experience': experience,
    }
    return render(request, 'portfolio/home.html', context)


def project_detail(request, pk):
    project = get_object_or_404(Project, pk=pk)
    return render(request, 'portfolio/project_detail.html', {'project': project})

def all_projects(request):
    projects = Project.objects.all().order_by('-date_created')
    return render(request, 'portfolio/all_projects.html', {'projects': projects})

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        
        # Save to database
        ContactMessage.objects.create(
            name=name,
            email=email,
            subject=subject,
            message=message
        )
        # Send email
        subject = f"New message from {name}: {subject}" 
        send_mail(
            subject,
            message,
            email,
            ['james21.khiisa@gmail.com'],
            fail_silently=False,
        )

        return render(request, 'portfolio/contact_success.html')

    return render(request, 'portfolio/contact.html')


def skills_view(request):
    print("Skills view is being called!")  # Add this at start of skills_view
    # Get all skills ordered properly once
    all_skills = Skill.objects.all().order_by('-display_order')
    
    categories = {
        'Programming_Languages': {
            'icon': 'fas fa-code',
            'skills': all_skills.filter(category='PROGRAMMING')
        },
        'Web_Development': {
            'icon': 'fas fa-laptop-code',
            'skills': all_skills.filter(category='WEB')
        },
        'Databases_Tools': {
            'icon': 'fas fa-database',
            'skills': all_skills.filter(category__in=['DATABASE', 'TOOLS'])
        },
        'Other_Skills': {
            'icon': 'fas fa-cogs',
            'skills': all_skills.filter(category='OTHER')
        }
    }


    
    # Debug output
    if settings.DEBUG:
        for cat_name, cat_data in categories.items():
            print(f"{cat_name}: {list(cat_data['skills'].values_list('name', flat=True))}")
    
    return render(request, 'portfolio/skills.html', {
        'categories': categories,
        'debug_mode': settings.DEBUG
    })