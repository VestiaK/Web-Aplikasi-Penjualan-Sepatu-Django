from django.contrib import admin
from django.urls import path
from dashboard.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_redirect),
    path('home/', home, name='home'),
    path("produkl/", produkl),
    path("produkp/", produkp),
    path("seluruh-produk/", seluruhproduk),
    path("contact/", contact),
    path('Vbrg/',Barang_View, name='Vbrg'),
    path('hapusbrg/<int:id_barang>', hapus_brg, name='hapus_brg'),
    path('ubahbrg/<int:id_barang>', ubah_brg, name='ubah_brg'),
    
    path('user/',User_View, name='user'),
    path('hapususer/<int:id_user>', hapus_user, name='hapus_user'),
    path('ubahuser/<int:id_user>', ubah_user, name='ubah_user'),
    path('addbrg/',tambah_barang),
    path('adduser/',tambah_user),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
