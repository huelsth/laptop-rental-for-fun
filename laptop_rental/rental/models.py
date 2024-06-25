from django.db import models

class Laptop(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='laptops/')

class Accessory(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='accessories/')

class Insurance(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='insurance/')

class Rental(models.Model):
    laptop = models.ForeignKey(Laptop, on_delete=models.CASCADE)
    accessories = models.ManyToManyField(Accessory)
    insurance = models.ForeignKey(Insurance, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()

    def clean(self):
        if self.end_date < self.start_date:
            raise ValidationError('End date cannot be before start date')
