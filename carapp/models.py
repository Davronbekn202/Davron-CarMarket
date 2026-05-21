from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Car(models.Model):
    class Holat(models.TextChoices):
        NEW = 'new', 'Yangi'
        USED = 'used', 'Ishlatilgan'

    class VehicleLevel(models.TextChoices):
        CHEVROLET = 'chevrolet', 'Chevrolet'
        KIA = 'kia', 'Kia'
        HYUNDAI = 'hyundai', 'Hyundai'
        BYD = 'byd', 'BYD'
        CHERY = 'chery', 'Chery'
        TOYOTA = 'toyota', 'Toyota'
        LADA = 'lada', 'Lada'
        UAZ = 'uaz', 'UAZ'
        GAZ = 'gaz', 'GAZ'
        HONDA = 'honda', 'Honda'
        NISSAN = 'nissan', 'Nissan'
        LEXUS = 'lexus', 'Lexus'
        MINIBUS = 'mikroavtobus', 'Mikroavtobus'
        BUS = 'avtobus', 'Avtobus'
        TRUCK = 'yuk_mashinasi', 'Yuk mashinasi'
        SPECIAL = 'maxsus_texnika', 'Maxsus texnika'
        SKUTER = 'skuter', 'Skuter'
        MOPED = 'moped', 'Moped'
        MOTOTSIKL = 'mototsikl', 'Mototsikl'
        YENGIL_AVTOMOBIL = 'yengil_avtomobil', 'Yengil avtomobil'
        PICKUP = 'pickup', 'Pikap'
        OTHER = 'boshqa', 'Boshqa'

    title = models.CharField(max_length=200, verbose_name='Mashina nomi')
    description = models.TextField(verbose_name='Tavsif')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Narxi')
    color = models.CharField(max_length=50, verbose_name='Rangi')
    year = models.PositiveIntegerField(verbose_name='Ishlab chiqarilgan yil')
    mileage = models.PositiveIntegerField(verbose_name='Yurgani (KM)')
    condition = models.CharField(
        max_length=20,
        choices=Holat.choices,
        verbose_name='Holati'
    )

    image = models.ImageField(upload_to='products/', verbose_name='Rasm')
    phone_number = models.CharField(max_length=20, verbose_name='Telefon raqam')
    created_at = models.DateTimeField(auto_now_add=True)
    seller = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Sotuvchi'
    )

    category = models.CharField(
        max_length=100,
        choices=VehicleLevel.choices,
        verbose_name='Kategoriya nomi'
    )

    other_brand = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        verbose_name='Boshqa marka'
    )

    def __str__(self):
        return self.title

class LocationOfProductModel(models.Model):
    class Cities(models.TextChoices):
        TOSHKENT = 'Toshkent', 'Toshkent'
        ANDIJON = 'Andijon', 'Andijon'
        BUXORO = 'Buxoro', 'Buxoro'
        FARGONA = 'Farg‘ona', 'Farg‘ona'
        JIZZAX = 'Jizzax', 'Jizzax'
        XORAZM = 'Xorazm', 'Xorazm'
        NAMANGAN = 'Namangan', 'Namangan'
        NAVOIY = 'Navoiy', 'Navoiy'
        QASHQADARYO = 'Qashqadaryo', 'Qashqadaryo'
        SAMARQAND = 'Samarqand', 'Samarqand'
        SIRDARYO = 'Sirdaryo', 'Sirdaryo'
        SURXONDARYO = 'Surxondaryo', 'Surxondaryo'

    city = models.CharField(max_length=30, choices=Cities, default=Cities.TOSHKENT, verbose_name='Viloyat')
    street = models.CharField(max_length=150)
    home = models.CharField(max_length=30)
    house = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self):
        return self.city, self.street, self.home
