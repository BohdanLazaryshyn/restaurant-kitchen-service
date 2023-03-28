from django.urls import path

from kitchen.views import index

urlpatterns = [
    path("", index, name="kitchen")]
    # path(
    #     "manufacturers/",
    #     ManufacturerListView.as_view(),
    #     name="manufacturer-list",
    # )]

app_name = "kitchen"
