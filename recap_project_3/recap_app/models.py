from django.db import models

# Create your models here.

GENDER_CHOICES = (
    ('Male', 'Male'),
    ('Female', 'Female'),
    ('Other', 'Other'),
)






class StudentModel(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField()
    address = models.TextField(null=True, blank=True)
    admission_date = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, null=True, blank=True)
    image = models.ImageField(upload_to='media/images/', null=True, blank=True)

    def __str__(self):
        return f"{self.name}"