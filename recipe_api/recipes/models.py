from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone

User = get_user_model()

CATEGORY_CHOICES = [
    ('Appetizer', 'Appetizer'),
    ('Main Course', 'Main Course'),
    ('Dessert', 'Dessert'),
    ('Beverage', 'Beverage'),
    ('Breakfast', 'Breakfast'),
    ('Side Dish', 'Side Dish'),
]

class Recipe(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='recipes')
    title = models.CharField(max_length=255)
    description = models.TextField()
    instructions = models.TextField()
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='Main Course')
    preparation_time = models.IntegerField()
    cooking_time = models.IntegerField()
    servings = models.IntegerField()
    created_date = models.DateTimeField(default=timezone.now)
    image = models.ImageField(upload_to='recipe_images/', blank=True, null=True)
    
    class Meta:
        ordering = ['-created_date']
        verbose_name = "Recipe"

    def __str__(self):
        return self.title

class Ingredient(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name='recipe_ingredients')
    name = models.CharField(max_length=100)
    quantity = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        unique_together = ('recipe', 'name')
        verbose_name = "Ingredient"

    def __str__(self):
        return f"{self.name} for {self.recipe.title}"
