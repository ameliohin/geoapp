from os import getenv
from django.db import migrations

class Migration(migrations.Migration):

    dependencies = []

    def generate_superuser(apps, schema_editor):
        from django.contrib.auth.models import User

        DJANGO_SU_NAME = getenv('DJANGO_SU_NAME', 'admin')
        DJANGO_SU_EMAIL = getenv('DJANGO_SU_EMAIL', 'admin@gmail.com')
        DJANGO_SU_PASSWORD = getenv('DJANGO_SU_PASSWORD', 'admin123')

        superuser = User.objects.create_superuser(
            username=DJANGO_SU_NAME,
            email=DJANGO_SU_EMAIL,
            password=DJANGO_SU_PASSWORD)

        superuser.save()

    operations = [
        migrations.RunPython(generate_superuser),
    ]