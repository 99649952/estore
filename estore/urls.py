from django.contrib import admin
from django.conf.urls import url, include
from .account.urls import urlpatterns as account_urls
from .core.views import home
from .core.views import handle_404

urlpatterns = [
    url('^$', home, name='home'),
    url('admin/', admin.site.urls),
    url(r'account/', include((account_urls, 'account'), namespace='account')),
    url(r'^404', handle_404, name='handle-404'),
]
