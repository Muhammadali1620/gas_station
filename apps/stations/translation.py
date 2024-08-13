from modeltranslation.translator import TranslationOptions, register
from apps.stations.models import Station


@register(Station)
class StationTranslationOptions(TranslationOptions):
    fields = ('short_text', 'address',)