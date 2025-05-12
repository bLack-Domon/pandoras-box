from django.db import models

# Create your models here.
class Profile(models.Model):
    nama = models.CharField(max_length=100)
    foto = models.ImageField(upload_to='profile/', blank=True, null=True)
    jabatan = models.CharField(max_length=100)
    deskripsi = models.TextField()
    cv = models.FileField(upload_to='cv/', blank=True, null=True)

    class Meta:
        verbose_name_plural = 'Profil Diri'

    def __str__(self):
        return self.nama

class Service(models.Model):
    nama = models.CharField(max_length=100)
    deskripsi = models.TextField()
    icon = models.CharField(max_length=100, help_text='Font Awesome Icon Class')

    class Meta:
        verbose_name_plural = 'Layanan Website'

    def __str__(self):
        return self.nama


class Project(models.Model):
    nama = models.CharField(max_length=100)
    deskripsi = models.TextField()
    gambar = models.ImageField(upload_to='project/', blank=True, null=True)
    link = models.URLField(blank=True, null=True)
    stack_teknologi = models.CharField(max_length=100, help_text='Contoh: HTML, CSS, JS')

    class Meta:
        verbose_name_plural = 'Projek ShowOff'

    def __str__(self):
        return self.nama


class Testimoni(models.Model):
    nama = models.CharField(max_length=100)
    foto = models.ImageField(upload_to='testimoni/', blank=True, null=True)
    jabatan = models.CharField(max_length=100)
    testimoni = models.TextField()

    class Meta:
        verbose_name_plural = 'Testimoni Klien'

    def __str__(self):
        return self.nama

class Contact(models.Model):
    nama = models.CharField(max_length=100)
    ikon = models.CharField(max_length=100, help_text='Font Awesome Icon Class')
    link = models.URLField(blank=True, null=True)

    class Meta:
        verbose_name_plural = 'Kontak Saya'

    def __str__(self):
        return self.nama