from django.contrib.auth.models import User
from django.db import models


class ProfileModel(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # first_name, last_name, email, username
    image = models.ImageField(upload_to='users/', blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    place_of_birth_street = models.TextField()
    place_of_birth_city = models.TextField()
    description = models.CharField(max_length=300, blank=True, null=True)
    phone_number = models.CharField(max_length=30, blank=True, null=True)

    def __str__(self):
        return f'{self.user.username} profile'

    class Meta:
        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'

