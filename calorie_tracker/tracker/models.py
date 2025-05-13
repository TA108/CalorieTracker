from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now

class FoodItem(models.Model):
    name = models.CharField(max_length=100)
    calories = models.IntegerField()
    protein = models.FloatField()
    carbohydrates = models.FloatField()
    fats = models.FloatField()
    def __str__(self):
        return self.name

class FoodLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    food_item = models.ForeignKey(FoodItem, on_delete=models.CASCADE)
    date = models.DateField(default=now)
    quantity = models.IntegerField()
    
    def __str__(self):
        return self.food_item.name
    
    @property
    def total_calories(self):
        return self.food_item.calories * self.quantity

    @property
    def total_protein(self):
        return self.food_item.protein * self.quantity

    @property
    def total_carbohydrates(self):
        return self.food_item.carbohydrates * self.quantity

    @property
    def total_fats(self):
        return self.food_item.fats * self.quantity
    
