# views.py
from django.shortcuts import render
from .models import Project, Skill, Education, Experience, ContactMessage
from django.core.mail import send_mail

def portfolio_home(request):
    projects = Project.objects.filter(featured=True)[:6]
    skills = Skill.objects.all().order_by('-proficiency')
    education = Education.objects.all().order_by('-end_date')
    experience = Experience.objects.all().order_by('-start_date')
    
    context = {
        'projects': projects,
        'skills': skills,
        'education': education,
        'experience': experience,
    }
    return render(request, 'portfolio/home.html', context)

def project_detail(request, pk):
    project = Project.objects.get(pk=pk)
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

