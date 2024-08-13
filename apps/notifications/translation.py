from modeltranslation.translator import TranslationOptions, register
from apps.notifications.models import Notifications


@register(Notifications)
class NotificationTranslationOptions(TranslationOptions):
    fields = ('title', 'content',)