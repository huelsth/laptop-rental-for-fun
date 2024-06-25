from ninja import NinjaAPI
from .models import Laptop, Accessory, Insurance, Rental
from .schema import LaptopSchema, AccessorySchema, InsuranceSchema, RentalSchema

api = NinjaAPI()

@api.get("/laptops")
def get_laptops(request):
    laptops = Laptop.objects.all()
    return [LaptopSchema.from_orm(laptop) for laptop in laptops]

@api.post("/rental")
def create_rental(request, rental: RentalSchema):
    rental_obj = Rental(**rental.dict())
    rental_obj.clean()
    rental_obj.save()
    return rental_obj
