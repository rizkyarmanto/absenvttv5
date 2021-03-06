from master.models import *
from rest_framework import serializers
from datetime import datetime


# Serializers define the API representation.
class MasterSiswaSerializer(serializers.ModelSerializer):
    class Meta:
        model = MasterSiswa
        fields = ['nisn', 'name', 'username', 'password', 'id_kelas', 'id_jurusan']

class MasterKelasSerializer(serializers.ModelSerializer):
    class Meta:
        model = MasterKelas
        fields = ['id_kelas', 'kelas']

class MasterJurusanSerializer(serializers.ModelSerializer):
    class Meta:
        model = MasterJurusan
        fields = ['id_jurusan', 'jurusan']

class AbsensiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Absensi
        fields = ['id','id_absensi', 'daily', 'status', 'checkin', 'checkout']
