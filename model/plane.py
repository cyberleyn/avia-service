from peewee import *

from database import pg_db


class Plane(Model):
    planeName = CharField()
    year = IntegerField()
    seats = IntegerField()
    registration = CharField(max_length=10)

    class Meta:
        database = pg_db

    @staticmethod
    def createPlane(name, year, seats, registration):
        plane = Plane()
        plane.planeName = name
        plane.year = year
        plane.seats = seats
        plane.registration = registration
        plane.save()
        return plane

    @staticmethod
    def getPlaneById(id):
        plane = Plane.select(Plane).where(Plane.id == id).get()
        return plane
