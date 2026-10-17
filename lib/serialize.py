# lib/serialize.py

from pprint import pprint
from marshmallow import Schema, fields

# model

class Dog:
    def __init__(self, name, breed, tail_wagging = False):
        self.name = name
        self.breed = breed
        self.tail_wagging = tail_wagging

    def give_treat(self):
        self.tail_wagging = True

    def scold(self):
        self.tail_wagging = False

# schema
class DogSchema(Schema):
    name = fields.String()
    breed = fields.String()
    tail_wagging = fields.Boolean()

# create model instance

dogs = [
    Dog(name="Snuggles", breed="Beagle", tail_wagging=True),
    Dog(name="Wags", breed="Collie", tail_wagging=False),
]

pprint(DogSchema(many=True).dumps(dogs))

