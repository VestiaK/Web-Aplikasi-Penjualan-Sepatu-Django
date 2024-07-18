from django.contrib import admin
from.models import Barang, Jenis, User, JenisUser
# Register your models here.
class kolomBarang(admin.ModelAdmin):
    list_display = ['kodebrg','imagebrg', 'namabrg', 'stokbrg','hargabrg', 'jenis_id']
    search_fields = ['kodebrg', 'namabrg']
    list_filter=('jenis_id',)
    list_per_page= 3
admin.site.register(Barang, kolomBarang)
admin.site.register(Jenis)

class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'address', 'phone_number','jenisid')
    search_fields = ('username', 'email', 'address')
    list_filter=('jenisid',)
    list_per_page= 3
admin.site.register(User, UserAdmin)
admin.site.register(JenisUser)