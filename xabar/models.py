from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class ElonManager(models.Manager):
    def get_queryset(self):
        return super(ElonManager, self).get_queryset().filter(holati='chop etilgan')
        

class Xabar(models.Model):

    XABAR_HOLATI = (
        ('qoralama', 'Qoralama'),
        ('chop etilgan', 'Chop etilgan')
    )

    TOIFA =(
        ('ichki', 'mahalliy'),
        ('tashqi', 'xorijiy')
    )

    mavzu = models.CharField(max_length=255)
    matn = models.TextField()
    elon_vaqti = models.DateTimeField(default=timezone.now)
    yaratilgan_vaqti = models.DateTimeField(auto_now_add=True)
    yangilangan_vaqti = models.DateTimeField(auto_now=True)
    link_matn = models.SlugField(unique_for_date='elon_vaqti', max_length=255)
    muallif = models.ForeignKey(User, on_delete=models.CASCADE)
    holati = models.CharField(choices=XABAR_HOLATI, default='qoralama', max_length=255)
    korildi = models.IntegerField(default=0)
    image_url = models.CharField(max_length=255)
    toifa = models.CharField(max_length=255, choices=TOIFA)

    objects = models.Manager()
    elon_qilingan = ElonManager()

    class Meta:
        ordering = ['-yaratilgan_vaqti']
        verbose_name = 'Xabarlar'


    def __str__(self):
        return self.mavzu


