# Generated by Django 5.0.6 on 2024-07-01 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_employee_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Faculty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('department', models.CharField(choices=[('Science', 'Science'), ('Management', 'Management'), ('Humanities', 'Humanities')], max_length=50)),
                ('Experience', models.CharField(max_length=50)),
            ],
        ),
    ]
