from django.db import models

class Jenis(models.Model):
    nama=models.CharField(max_length=50)
    ket=models.TextField()

    def __str__(self):
        return self.nama

class Barang(models.Model):
    kodebrg=models.CharField(max_length=8)
    imagebrg=models.ImageField(upload_to='images/', blank=True)
    namabrg=models.CharField(max_length=50)
    stokbrg=models.IntegerField()
    hargabrg=models.BigIntegerField()
    waktu_posting=models.DateTimeField(auto_now_add=True)
    jenis_id=models.ForeignKey(Jenis, on_delete=models.CASCADE,null=True)

def __str__(self):
        return "{}. {}".format(self.kodebrg,self.namabrg)

class JenisUser(models.Model):
     jenis=models.CharField(max_length=50)

class User(models.Model):
    username=models.CharField(max_length=255)
    email=models.EmailField(max_length=255)
    address=models.CharField(max_length=255)
    phone_number=models.IntegerField()
    jenisid=models.ForeignKey(JenisUser, on_delete=models.CASCADE,null=True)

    def __str__(self):
        return "{}. {}".format(self.username,self.email)
    
