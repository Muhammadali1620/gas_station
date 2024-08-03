from django.db import models

from apps.users.validators import phone_validate


class Appeals(models.Model):
    user = models.ForeignKey('users.CustomUser', on_delete=models.CASCADE, related_name='appeals')
    message = models.CharField(max_length=500)
    phone_number = models.CharField(max_length=20, validators=[phone_validate])

    def __str__(self):
        return f'{self.phone_number} - {self.message[:20]}'