from django.db import models

class CreditCard(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    card_number = models.CharField(max_length=25)
    expiry_date = models.CharField(max_length=5)
    cvv =   models.CharField(max_length=4)
    amount = models.DecimalField(max_digits=10, decimal_places=2)


    def __str__(self):
        return f'{self.name} - {self.email}'
    


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.CharField(max_length=10)
    image = models.ImageField(upload_to='products/', blank=True, null=True)

   