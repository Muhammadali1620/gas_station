from django.db import models


class Complaint(models.Model):
    class Section(models.IntegerChoices):
        SECTION = 1
        REVIEW = 2

    class Type(models.IntegerChoices):
        SPAM = 0
        SCOLD = 1
        OTHER = 2        

    section = models.PositiveSmallIntegerField(choices=Section.choices)
    complaint_type = models.PositiveSmallIntegerField(choices=Type.choices)
    message = models.CharField(max_length=255, blank=True)

    viewed = models.BooleanField(default=False)
    viewed_at = models.DateTimeField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)