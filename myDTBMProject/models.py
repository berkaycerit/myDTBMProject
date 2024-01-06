from django.db import models


"""class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)"""

#veri tabanı modelleri burada tanıtılıyor. her bir tablo class şeklinde oluşturuluyor.

class Ogrenci(models.Model):
    Ad = models.CharField(max_length=50)
    Soyad = models.CharField(max_length=50)
    Cinsiyet = models.CharField(max_length=10)
    Bolum = models.CharField(max_length=50)
    Sinif = models.CharField(max_length=5)
    Numara = models.CharField(max_length=15)
    def __str__(self):
        return f"{self.Ad} {self.Soyad}"
class Dersler(models.Model):
    DersAdi = models.CharField(max_length=200)
    DersKodu = models.CharField(max_length=20)  
    def __str__(self):
        return f"{self.DersAdi} {self.DersKodu}"

class OgretimGorevlisi(models.Model):
    Ad = models.CharField(max_length=200)
    Soyad = models.CharField(max_length=200)
    Email = models.CharField(max_length=200)
    def __str__(self):
        return f"{self.Ad} {self.Soyad}"

class Kayit(models.Model):
    ogrenci = models.ForeignKey(Ogrenci, on_delete=models.CASCADE)
    ders = models.ForeignKey(Dersler, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.ogrenci} - {self.ders}"
    class Meta:
        unique_together = ['ogrenci', 'ders']

class OgretimGorevlisi_Ders(models.Model):
    ogretimGorevlisi = models.ForeignKey(OgretimGorevlisi, on_delete=models.CASCADE)
    ders = models.ForeignKey(Dersler, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.ogretimGorevlisi} {self.ders}"