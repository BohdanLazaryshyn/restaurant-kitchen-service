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
    toggle_assign_to_dish,
    CookDeleteView,
    CookUpdateView,
    CookCreateView,
    CookListView,
    CookDetailView,
    register, ChangePasswordView, ChangePasswordDoneView,
)

urlpatterns = [
    path("", index, name="index"),
    path("register/", register, name='register'),
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
        "dishes/create/",
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
        name="dish-type-list",
    ), path(
        "dish-types/<int:pk>/",
        DishTypeDetailView.as_view(),
        name="dish-type-detail"
    ), path(
        "dish-types/create/",
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
    ), path(
        "cooks",
        CookListView.as_view(),
        name="cook-list",
    ), path(
        "cook/<int:pk>/",
        CookDetailView.as_view(),
        name="cook-detail"
    ), path(
        "cook/create/",
        CookCreateView.as_view(),
        name="cook-create"
    ), path(
        "cook/<int:pk>/update/",
        CookUpdateView.as_view(),
        name="cook-update"
    ), path(
        'change-password/',
        ChangePasswordView.as_view(),
        name='change_password'
    ), path(
        'change-password-done/',
        ChangePasswordDoneView.as_view(),
        name='change-password-done'
    ), path(
        "cook/<int:pk>/delete/",
        CookDeleteView.as_view(),
        name="cook-delete")
]

app_name = "kitchen"
