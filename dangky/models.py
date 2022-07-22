from django.db import models

# Create your models here.
class Nguoidung(models.Model):
    ten_dang_nhap = models.CharField(max_length = 100)
    mail = models.CharField(max_length = 100)
    mat_khau = models.CharField(max_length = 100)

    def __str__(self):
        return self.ten_dang_nhap
