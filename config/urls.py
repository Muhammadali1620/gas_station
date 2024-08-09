from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls.i18n import i18n_patterns
from apps.general.views import set_language
from .yasg import schema_view


urlpatterns = [
    #2rd apps
    path('__debug__/', include('debug_toolbar.urls')),
    path('setlang/<str:lang>/', set_language, name='set_language'),

    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

]   

#apps language
urlpatterns += i18n_patterns(
    #admin
    path('admin/', admin.site.urls),

    #my apps
    path('api/v1/auth/', include('apps.authentication.urls'))
)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)