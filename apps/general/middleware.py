from django.utils import translation 


class LanguageMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        old_language = request.session.get('language')
        language = request.GET.get('language', old_language)
        if not bool(language == 'uz' or language != 'en') and not bool(language == 'en' or language != 'uz'):
            language = 'ru'
        request.session['language'] = language 
        language_code = language
        translation.activate(language_code)

        response = self.get_response(request)
        a = request.GET.get('language')
        return response