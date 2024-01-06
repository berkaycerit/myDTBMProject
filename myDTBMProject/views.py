from django.http import HttpResponse
from django.shortcuts import render
from .models import Dersler, OgretimGorevlisi_Ders, Kayit, OgretimGorevlisi, Ogrenci
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import UpdateView
from django.urls import reverse_lazy
from .forms import OgrenciForm, KayitForm
#from templates import index
def index(request):
    return render(request, "index.html")

def lessons(request):
 # veritabanından dersleri, dersleri veren hocaları ve dersi alan öğrencileri çekiyoruz
    dersler = Dersler.objects.all()
    ogretim_gorevlileri_dersler = OgretimGorevlisi_Ders.objects.select_related('ders', 'ogretimGorevlisi')
    ogrenci_dersler = Kayit.objects.select_related('ders', 'ogrenci')

# veritabanından çektiğimiz verileri birleştirerek ders listesi oluşturuyoruz
    ders_listesi = []
    for ders in dersler:
        dersi_veren_hoca = ogretim_gorevlileri_dersler.filter(ders=ders).first()
        if dersi_veren_hoca:
            dersi_veren_hoca_adi = f"{dersi_veren_hoca.ogretimGorevlisi.Ad} {dersi_veren_hoca.ogretimGorevlisi.Soyad}"
        else:
            dersi_veren_hoca_adi = "Bilinmiyor"
        dersi_alan_ogrenci_sayisi = ogrenci_dersler.filter(ders=ders).count()
        ders_listesi.append({
            'ders_kodu': ders.DersKodu,
            'ders_adi': ders.DersAdi,
            'dersi_veren_hoca': dersi_veren_hoca_adi,
            'dersi_alan_ogrenci_sayisi': dersi_alan_ogrenci_sayisi,
        })

    return render(request, 'lessons.html', {'ders_listesi': ders_listesi})

def students(request):
    ogrenciler = Ogrenci.objects.all()
    ogrenci_listesi = []
    for ogrenci in ogrenciler:
        ogrenci_listesi.append({
            'ad': ogrenci.Ad,
            'id': ogrenci.id,
            'soyad': ogrenci.Soyad,
            'cinsiyet': ogrenci.Cinsiyet,
            'bolum': ogrenci.Bolum,
            'sinif': ogrenci.Sinif,
            'numara': ogrenci.Numara,
            'ders_sayisi': Kayit.objects.filter(ogrenci=ogrenci).count(),
        })
    return render(request, 'students.html', {'ogrenci_listesi': ogrenci_listesi})
  

def student_detail(request, student_id):
    ogrenci = get_object_or_404(Ogrenci, id=student_id)
    kayitlar = Kayit.objects.filter(ogrenci=ogrenci)
    ders_sayisi = kayitlar.count()
    student_id = ogrenci.id

    context = {
        'ogrenci': ogrenci, # 'ogrenci' anahtarına karşılık gelen değer 'ogrenci' değişkeni olacak
        'ad': ogrenci.Ad,
        'soyad': ogrenci.Soyad,
        'bolum': ogrenci.Bolum,
        'sinif': ogrenci.Sinif,
        'numara': ogrenci.Numara,
        'ders_sayisi': ders_sayisi,
        'cinsiyet': ogrenci.Cinsiyet,
        'kayitlar': kayitlar,

    }
    return render(request, 'student_detail.html', context)

class StudentUpdateView(UpdateView):
    model = Ogrenci
    template_name = 'student_form.html'
    fields = '__all__'
    def get_success_url(self):
            return reverse_lazy('students')  


def ogrenci_delete(request, ogrenci_id):
    ogrenci = get_object_or_404(Ogrenci, id=ogrenci_id)

    if request.method == 'POST':
        ogrenci.delete()
        return redirect('students') 

    return render(request, 'ogrenci_delete.html', {'ogrenci': ogrenci})


def ogrenci_create(request):
    if request.method == 'POST':
        form = OgrenciForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('students')
        
    else:
        form = OgrenciForm()

    return render(request, 'ogrenci_create.html', {'form': form})

def ogrenciye_ders_atama(request, ogrenci_id):
    ogrenci = get_object_or_404(Ogrenci, id=ogrenci_id)
    dersler = Dersler.objects.all()
    if request.method == 'POST':
        form = KayitForm(request.POST)
        if form.is_valid():
            # form geçerli ise işlemleri gerçekleştir
            form.save()
            return redirect('students')  
    else:
        form = KayitForm(initial={'ogrenci': ogrenci})

    return render(request, 'ogrenciye_ders_atama.html', {'form': form, 'ogrenci': ogrenci})