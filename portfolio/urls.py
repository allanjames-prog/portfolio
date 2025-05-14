from django.urls import path
from .views import (
    portfolio_home,
    project_detail,
    all_projects,
    contact,
    skills_view,
)

urlpatterns = [
    path('', portfolio_home, name='home'),
    path('projects/', all_projects, name='projects'),
    path('projects/<int:pk>/', project_detail, name='project_detail'),
    path('contact/', contact, name='contact'),
    path('skills/', skills_view, name='skills'),
]
