from django import forms
from .models import Ogrenci, Kayit

class OgrenciForm(forms.ModelForm):
    class Meta:
        model = Ogrenci
        fields = '__all__' 

class KayitForm(forms.ModelForm):
    class Meta:
        model = Kayit
        fields = ['ogrenci', 'ders']

    def clean(self):
        cleaned_data = super().clean()
        ogrenci = cleaned_data.get('ogrenci')
        ders = cleaned_data.get('ders')
        # öğrencinin daha önce bu dersi aldığı durumu kontrol et
        if Kayit.objects.filter(ogrenci=ogrenci, ders=ders).exists():
            raise forms.ValidationError('Bu öğrenci bu dersi zaten almış.')
        return cleaned_data