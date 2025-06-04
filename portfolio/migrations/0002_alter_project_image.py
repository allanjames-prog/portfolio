from django.db import migrations
from cloudinary_storage.storage import MediaCloudinaryStorage
from django.core.files.base import ContentFile
import os

def migrate_images(apps, schema_editor):
    Project = apps.get_model('projects', 'Project')
    storage = MediaCloudinaryStorage()
    
    for project in Project.objects.all():
        if project.image and not project.image.name.startswith('http'):
            try:
                with project.image.open('rb') as f:
                    file_content = f.read()
                    project.image.save(
                        os.path.basename(project.image.name),
                        ContentFile(file_content),
                        save=True
                    )
            except Exception as e:
                print(f"Failed to migrate {project.title}: {str(e)}")

class Migration(migrations.Migration):
    dependencies = [
        ('projects', 'previous_migration'),
    ]

    operations = [
        migrations.RunPython(migrate_images),
    ]