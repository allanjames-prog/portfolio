from django.contrib import admin
from .models import Project, Skill, Education, Experience, ContactMessage

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'date_created', 'featured')
    list_filter = ('featured', 'date_created')
    search_fields = ('title', 'description', 'technologies')

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'proficiency', 'display_order')
    list_filter = ('category',)
    search_fields = ('name',)
    list_editable = ('display_order', 'proficiency')
    fieldsets = (
        (None, {
            'fields': ('name', 'proficiency', 'category', 'display_order')
        }),
        ('Advanced', {
            'fields': ('icon_class',),
            'classes': ('collapse',)
        }),
    )

@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ('degree', 'institution', 'start_date', 'end_date')
    search_fields = ('degree', 'institution', 'field_of_study')

@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ('position', 'company', 'start_date', 'end_date', 'current')
    list_filter = ('current',)
    search_fields = ('position', 'company', 'description')

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'created_at', 'is_read')
    list_filter = ('is_read', 'created_at')
    search_fields = ('name', 'email', 'subject', 'message')
    readonly_fields = ('created_at',)