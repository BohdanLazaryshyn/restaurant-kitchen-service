from django.urls import path

from storehouse.views import (
    IngredientListView,
    IngredientCreateView,
    IngredientUpdateView,
    IngredientDeleteView,
)

urlpatterns = [path(
        "ingredients",
        IngredientListView.as_view(),
        name="ingredient-list",
    ), path(
        "ingredients/create/",
        IngredientCreateView.as_view(),
        name="ingredient-create"
    ), path(
        "ingredients/<int:pk>/update/",
        IngredientUpdateView.as_view(),
        name="ingredient-update"
    ), path(
        "ingredients/<int:pk>/delete/",
        IngredientDeleteView.as_view(),
        name="ingredient-delete"
    )
]

app_name = "storehouse"
