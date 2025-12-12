from rest_framework import viewsets
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from .models import Recipe
from .serializers import RecipeSerializer
from .permissions import IsAuthorOrReadOnly

class RecipeViewSet(viewsets.ModelViewSet):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
    
    permission_classes = [IsAuthorOrReadOnly]

    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    
    filterset_fields = ['category'] 
    
    search_fields = ['title', 'category', 'recipe_ingredients__name', 'description']
    
    ordering_fields = ['preparation_time', 'cooking_time', 'servings', 'created_date']
    ordering = ['-created_date']

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
