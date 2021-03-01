from django.db import migrations
from django.contrib.gis.geos import Point
from location_field.models.spatial import LocationField
from geoapp.models import Branch, Employee


class Migration(migrations.Migration):

    dependencies = [
        ('geoapp', '0006_employee_branch'),
    ]

    def generate_branches(apps, schema_editor):
        for i in range(10):
            name = 'Branch ' + str(i)
            Branch.objects.create(name=name)

    def generate_employees(apps, schema_editor):
        employees = [Employee(first_name='F_'+str(i), last_name='L_'+str(i)) for i in range(10000)]
        Employee.objects.bulk_create(employees)

    operations = [
        migrations.RunPython(generate_branches),
        migrations.RunPython(generate_employees),
    ]