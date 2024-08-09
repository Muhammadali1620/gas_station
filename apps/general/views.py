from django.http import HttpResponseRedirect
from django.shortcuts import render


def set_language(request, lang):
    current_lang = request.GET.get('current_lang', 'en')
    next_url = request.META['HTTP_REFERER']
    next_url = str(next_url).replace(current_lang, lang, 1)
    return HttpResponseRedirect(next_url)