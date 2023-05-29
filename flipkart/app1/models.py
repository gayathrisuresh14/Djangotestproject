from django.db import models


# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=250)
    price = models.DecimalField(max_digits=4, decimal_places=2)
    description = models.CharField(max_length=500)


# ORM Queries ---> Object Relational Mapper
#             ---> queries in pythonic way

"""
Tablename.objects.all()
Tablename.objects.all().values()
Tablename.objects.get(id=1)
delete()
save()
filter()-->Tablename.objects.all().filter(condition(eg:price<=50))
exclude()-->Tablename.objects.all().exclude(condition(eg:name = 'pen'))
variable_name = Table_name(coloumn_name='corresponding values')



"""