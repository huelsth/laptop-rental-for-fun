from django.db import models
from django.core.exceptions import ValidationError

class Laptop(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='laptops/')

    def __str__(self):
        return self.name

class Accessory(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='accessories/')

    def __str__(self):
        return self.name

class Insurance(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='insurance/')

    def __str__(self):
        return self.name

class Rental(models.Model):
    laptop = models.ForeignKey(Laptop, on_delete=models.CASCADE)
    accessories = models.ManyToManyField(Accessory)
    insurance = models.ForeignKey(Insurance, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()

    def clean(self):
        if self.end_date < self.start_date:
            raise ValidationError('End date cannot be before start date')

    def __str__(self):
        return f"Rental of {self.laptop.name} from {self.start_date} to {self.end_date}"
