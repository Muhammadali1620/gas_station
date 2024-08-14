from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls.i18n import i18n_patterns
from apps.general.views import set_language
from .yasg import schema_view


urlpatterns = [
    #admin
    path('admin/', admin.site.urls),

    #2rd apps
    path('__debug__/', include('debug_toolbar.urls')),
    path('setlang/<str:lang>/', set_language, name='set_language'),
    
    path('rest_api', include('rest_framework.urls')),

    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

    #my apps
    path('api/v1/auth/', include('apps.authentication.urls')),
    path('api/v1/users/', include('apps.users.urls')),
    path('api/v1/cars/', include('apps.cars.urls')),
    path('api/v1/stations/', include('apps.stations.urls')),
    path('api/v1/wishlist/', include('apps.wishlist.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)