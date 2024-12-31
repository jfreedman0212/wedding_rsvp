"""
URL configuration for wedding project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.flatpages import views
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

# statically configured routes. configure these first.
# then, serve user-uploaded media files during development.
# in production, these will be served by S3 (or some other file storage).
# The static function itself checking settings.DEBUG
urlpatterns = [
    path('rsvp/', include('guests.urls')),
    path('admin/', admin.site.urls),
] + static(
    settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT
)

# flatpage urls for the customizable homepage and any other page too
urlpatterns += [
    path('', views.flatpage, {'url': '/'}, name='home'),
    path('<path:url>', views.flatpage, name='flatpages'),

]
