from main.views import ItemView, get_item_html
from main.apps import MainConfig
from django.urls import path

app_name = MainConfig.name

urlpatterns = [
        path('buy/<int:pk>/', ItemView.as_view(), name='buy'),
        path('item/<int:pk>/', get_item_html, name='item'),
    ]
