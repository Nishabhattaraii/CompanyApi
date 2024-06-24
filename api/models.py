from django.db import models

class Company(models.Model):
    company_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    about = models.TextField()
    type = models.CharField(max_length=100, choices=(('IT', 'IT'), ('Non IT', 'Non IT')))
    added_date = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

class Employee(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=50)  # Corrected typo: removed extra "models."
    about = models.TextField()
    position = models.CharField(max_length=50, choices=(('Manager', 'Manager'), ('Software Developer', 'Software Developer'), ('Project Leader', 'PL')))  # Corrected typo: adjusted max_length and choices
    company = models.ForeignKey(Company, on_delete=models.CASCADE)  # Corrected typo: changed 'comapny' to 'company'
