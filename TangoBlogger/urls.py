from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView

urlpatterns = [
    path('', TemplateView.as_view(template_name='accounts/dashboard.html'), name='home'),
    path('admin/', admin.site.urls),
    path('accounts/', include(('accounts.urls', 'accounts'), namespace='accounts')),
    path('blog/', include(('blog.urls', 'blog'), namespace='blog')),
    path('gallery/', include(('gallery.urls', 'gallery'), namespace='gallery')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)