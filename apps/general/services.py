import os
from django.db.models import FileField, ImageField


def delete_file_after_delete_obj(instance):
    for field in instance._meta.get_fields():
        if isinstance(field, (FileField, ImageField)):
            file_field = getattr(instance, field.name)
            if file_field and os.path.isfile(file_field.path):
                os.remove(file_field.path)