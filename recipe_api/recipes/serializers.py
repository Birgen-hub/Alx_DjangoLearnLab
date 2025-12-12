from rest_framework import serializers
from .models import Recipe, Ingredient

class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = ('name', 'quantity')

class RecipeSerializer(serializers.ModelSerializer):
    ingredients = IngredientSerializer(many=True, source='recipe_ingredients', required=True)
    author_username = serializers.CharField(source='author.username', read_only=True)
    created_date = serializers.DateTimeField(read_only=True)
    
    class Meta:
        model = Recipe
        fields = (
            'id', 'author', 'author_username', 'title', 'description', 
            'ingredients', 'instructions', 'category', 'preparation_time', 
            'cooking_time', 'servings', 'created_date', 'image'
        )
        read_only_fields = ('author',)

    def create(self, validated_data):
        ingredients_data = validated_data.pop('recipe_ingredients')
        recipe = Recipe.objects.create(**validated_data)
        
        for ingredient_data in ingredients_data:
            Ingredient.objects.create(recipe=recipe, **ingredient_data)
        
        return recipe

    def update(self, instance, validated_data):
        ingredients_data = validated_data.pop('recipe_ingredients', None)
        
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.instructions = validated_data.get('instructions', instance.instructions)
        instance.category = validated_data.get('category', instance.category)
        instance.preparation_time = validated_data.get('preparation_time', instance.preparation_time)
        instance.cooking_time = validated_data.get('cooking_time', instance.cooking_time)
        instance.servings = validated_data.get('servings', instance.servings)
        instance.save()

        if ingredients_data is not None:
            instance.recipe_ingredients.all().delete()
            for ingredient_data in ingredients_data:
                Ingredient.objects.create(recipe=instance, **ingredient_data)
        
        return instance
