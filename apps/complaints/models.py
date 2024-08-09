from django.db import models
from django.conf import settings


class Complaint(models.Model):
    class Section(models.IntegerChoices):
        SECTION = 1, 'Section'
        REVIEW = 2, 'Review'

    class Type(models.IntegerChoices):
        SPAM = 0, 'Spam'
        VIOLENCE = 1, 'Violence'
        AUTHOR_RIGHTS = 2, 'Author Rights'
        NARCOTICS = 3, 'Narcotics'
        PERSONAL_INFO = 4, 'Personal Info'
        SCOLD = 5, 'Scold'
        OTHER = 6, 'Other'

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='complaints')

    section = models.PositiveSmallIntegerField(choices=Section.choices)
    complaint_type = models.PositiveSmallIntegerField(choices=Type.choices)
    message = models.CharField(max_length=255, blank=True)

    viewed = models.BooleanField(default=False)
    viewed_at = models.DateTimeField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)