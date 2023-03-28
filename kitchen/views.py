from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views import generic

from .models import Cook, Dish, DishType, Ingredient


@login_required
def index(request):

    num_cooks = Cook.objects.count()
    num_dishes = Dish.objects.count()
    num_type_dishes = DishType.objects.count()
    num_ingredients = Ingredient.objects.count()
    # num_visit = request.session.get("num_visit", 0)
    # request.session["num_visit"] = num_visit + 1

    context = {
        "num_cooks": num_cooks,
        "num_dishes": num_dishes,
        "num_type_dishes": num_type_dishes,
        "num_ingredients": num_ingredients + 1
    }

    return render(request, "kitchen/index.html", context=context)


class CookListView(LoginRequiredMixin, generic.ListView):
    model = Cook
    paginate_by = 10


class CookDetailView(LoginRequiredMixin, generic.DetailView):
    model = Cook
    queryset = Cook.objects.prefetch_related("dishes")


class DishListView(LoginRequiredMixin, generic.ListView):
    model = Dish
    paginate_by = 10
    queryset = Dish.objects.select_related("dish_type")


class DishDetailView(LoginRequiredMixin, generic.DetailView):
    model = Dish


class DishTypeListView(LoginRequiredMixin, generic.ListView):
    model = DishType
    paginate_by = 10


class DishTypeDetailView(LoginRequiredMixin, generic.DetailView):
    model = DishType


class IngredientListView(LoginRequiredMixin, generic.ListView):
    model = Ingredient
    paginate_by = 10



