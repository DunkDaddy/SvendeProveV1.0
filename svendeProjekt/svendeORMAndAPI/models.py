from django.db import models

# Create your models here.

class Bruger(models.Model):
    navn = models.CharField(max_length=255)
    brugernavn = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    email = models.CharField(max_length=255)

    def __str__(self):
        return self.navn


class Kategori(models.Model):
    navn = models.CharField(max_length=255)

    def __str__(self):
        return self.navn


class Geo(models.Model):
    lattitude = models.DecimalField(max_digits=9, decimal_places=6)
    longtitude = models.DecimalField(max_digits=9, decimal_places=6)


class Subscribed_kategori(models.Model):
    bruger_id = models.ForeignKey(Bruger, on_delete=models.CASCADE)
    kategori_id = models.ForeignKey(Kategori, on_delete=models.CASCADE)


class Billeder(models.Model):
    titel = models.CharField(max_length=255)
    beskrivelse = models.TextField()
    billedet = models.ImageField(upload_to='media/images')
    geo_id = models.ForeignKey(Geo, on_delete=models.CASCADE)
    kategori_id = models.ForeignKey(Kategori, on_delete=models.CASCADE)
    upload_id = models.ForeignKey(Bruger, on_delete=models.CASCADE)

    def __str__(self):
        return self.titel


class Rapport(models.Model):
    beskrivelse = models.TextField(default="Bruger er utilfreds med billedet")
    billed_id = models.ForeignKey(Billeder, on_delete=models.CASCADE)
    snitch_id = models.ForeignKey(Bruger,on_delete=models.CASCADE)

    def __str__(self):
        return self.snitch_id.navn + " har rappoteret et billed fra: " + self.billed_id.upload_id.navn

