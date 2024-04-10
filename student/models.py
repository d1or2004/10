from django.db import models


class Address(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name


class Role(models.Model):
    a = ("a", "A")
    b = ("b", "B")
    c = ("c", "C")


class Student(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    status = models.CharField(max_length=20, choices=(("a", "A"), ("b", "B"), ("c", "C")))
    age = models.PositiveIntegerField()
    address = models.ForeignKey(Address, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
