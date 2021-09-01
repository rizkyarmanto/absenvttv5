from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


# Create your models here.

class MasterKelas(models.Model):
    id_kelas                = models.IntegerField(primary_key=True)
    category_kelas          = (
                                ('10', '10'),
                                ('11', '11'),
                                ('12', '12'),
                                ('13', '13'),
                            )
    kelas                   = models.CharField(max_length=100, choices=category_kelas)

    def __str__(self):
        return f'{self.id_kelas}. {self.kelas}'
    
class MasterJurusan(models.Model):
    id_jurusan              = models.IntegerField(primary_key=True)
    category_jurusan        = (
                                ('KGSP', 'KGSP'),
                                ('SIJA', 'SIJA'),
                                ('TEDK', 'TEDK'),
                                ('TFLM', 'TFLM'),
                                ('TMPO', 'TMPO'),
                                ('TTL', 'TTL'),
                            )
    jurusan                 = models.CharField(max_length=100, choices=category_jurusan)

    def __str__(self):
        return f'{self.id_jurusan}. {self.jurusan}'

class MasterSiswa(models.Model):
    nisn                    = models.CharField(primary_key=True, unique=True,  max_length=10, validators=[RegexValidator(r'^\d{1,10}$')])
    name                    = models.CharField(max_length=100)
    username                = models.CharField(max_length=16, unique=True)
    password                = models.CharField(max_length=32)
    id_kelas                = models.ForeignKey(MasterKelas, on_delete=models.CASCADE)
    id_jurusan              = models.ForeignKey(MasterJurusan, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.nisn}, {self.name}'

class Absensi(models.Model):
    id_absensi              = models.ForeignKey(MasterSiswa, on_delete=models.CASCADE)
    daily                   = models.DateField()
    status                  = models.BooleanField()
    checkin                 = models.DateTimeField(auto_now_add=True)
    checkout                = models.DateTimeField(null=True, blank=True, default=None)

    def __str__(self):
        return f'{self.id_absensi}'