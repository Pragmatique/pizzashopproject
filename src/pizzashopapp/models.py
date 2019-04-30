from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class PizzaShop(models.Model):
    owner = models.OneToOneField(User,on_delete=models.CASCADE,related_name="pizzashop")
    name=models.CharField(max_length=100,verbose_name="Пиццерия")
    phone = models.CharField(max_length=100, verbose_name="Телефон")
    address = models.CharField(max_length=100, verbose_name="Адрес")
    logo = models.ImageField(upload_to="pizzashop_logo/", blank=False)


    class Meta:
        verbose_name = 'Пиццерия'
        verbose_name_plural = 'Пиццерии'

    def __str__(self):
        return self.name

class Pizza(models.Model):
    pizzashop = models.ForeignKey(PizzaShop, on_delete=models.CASCADE)
    name = models.CharField(max_length=40, verbose_name="Пицца")
    short_description = models.CharField(max_length=100, verbose_name="Краткое описание")
    image=models.ImageField(upload_to="pizza_images/", blank=False)
    price=models.IntegerField(default=0)

    class Meta:
        verbose_name = 'Пицца'
        verbose_name_plural = 'Пиццы'

    def __str__(self):
        return self.name
