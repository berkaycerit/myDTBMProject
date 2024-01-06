from django.contrib import admin
from .models import Ogrenci, OgretimGorevlisi, Dersler, Kayit, OgretimGorevlisi_Ders

admin.site.register(Ogrenci)
admin.site.register(OgretimGorevlisi)
admin.site.register(Dersler)
admin.site.register(Kayit)
admin.site.register(OgretimGorevlisi_Ders)