from typing import List, Dict, Any
from django.db import models


class Value(models.Model):
    title = models.CharField(max_length=200)
    text = models.CharField(max_length=200)

    def get_by_number(self, num: int):
        """
        accepts an int to get an object with matching pk
        """
        return Value.objects.get(pk=num)

    class Meta:
        verbose_name_plural = "values"

    def __str__(self) -> str:
        return self.text


class Principle(models.Model):
    title = models.CharField(max_length=200)
    text = models.CharField(max_length=200)

    def get_by_number(self, num: int):
        """
        accepts an int to get an object with matching pk
        """
        return Principle.objects.get(pk=num)

    class Meta:
        verbose_name_plural = "principles"

    def __str__(self) -> str:
        return self.text
