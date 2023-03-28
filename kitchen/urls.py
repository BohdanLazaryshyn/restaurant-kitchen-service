from django.urls import path

from kitchen.views import (
    index,
    DishListView,
    DishDetailView,
    DishCreateView,
    DishUpdateView,
    DishDeleteView,
    DishTypeDetailView,
    DishTypeListView,
    DishTypeDeleteView,
    DishTypeUpdateView,
    DishTypeCreateView,
    toggle_assign_to_dish
)

urlpatterns = [
    path("", index, name="kitchen"),
    path(
        "dishes/",
        DishListView.as_view(),
        name="dish-list",
    ), path(
        "dishes/<int:pk>/",
        DishDetailView.as_view(),
        name="dish-detail",
    ), path(
        "dishes/<int:pk>/toggle-assign/",
        toggle_assign_to_dish,
        name="toggle-dish-assign",
    ), path(
        "dishes/<int:pk>/create/",
        DishCreateView.as_view(),
        name="dish-create",
    ), path(
        "dishes/<int:pk>/update/",
        DishUpdateView.as_view(),
        name="dish-update",
    ), path(
        "dishes/<int:pk>/delete/",
        DishDeleteView.as_view(),
        name="dish-delete",
    ), path(
        "dish-types",
        DishTypeListView.as_view(),
        name="dish_type-list",
    ), path(
        "dish-types/<int:pk>/",
        DishTypeDetailView.as_view(),
        name="dish-type-detail"
    ), path(
        "dish-types/<int:pk>/create/",
        DishTypeCreateView.as_view(),
        name="dish-type-create"
    ), path(
        "dish-types/<int:pk>/update/",
        DishTypeUpdateView.as_view(),
        name="dish-type-update"
    ), path(
        "dish-types/<int:pk>/delete/",
        DishTypeDeleteView.as_view(),
        name="dish-type-delete"
    )
]

app_name = "kitchen"
