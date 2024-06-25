from ninja import Schema
from datetime import date

class LaptopSchema(Schema):
    name: str
    image: str

class AccessorySchema(Schema):
    name: str
    image: str

class InsuranceSchema(Schema):
    name: str
    image: str

class RentalSchema(Schema):
    laptop: int
    accessories: list[int]
    insurance: int
    start_date: date
    end_date: date
