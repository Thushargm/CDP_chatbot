from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from chatbot.views import get_response, chatbot_home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', chatbot_home, name='chatbot_home'),  # Root URL for the chatbot home
    path('get_response/', get_response, name='get_response'),  # Endpoint for chatbot responses
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls)),
    ]
