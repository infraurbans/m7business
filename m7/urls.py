"""m7 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static


from django.contrib.auth.views import LogoutView
from m7.core.views import CustomLoginView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('conta/entrar/', CustomLoginView.as_view(), name="login", kwargs={'redirect_authenticated_user': True}),
    path('conta/sair/', LogoutView.as_view(), name="logout"),
    path('dashboard/', include('m7.contracts.urls', namespace="contracts")),
    path('dashboard/', include('m7.dividends.urls', namespace="dividends"))

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
