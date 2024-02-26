from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import redirect
from django.template import loader
from rest_framework.generics import get_object_or_404
from rest_framework.views import APIView
from .models import Item
from .serliazers import ItemSerializer
from .services import get_session
import re


def get_item_html(request, pk):
    """ Контроллер для странницы товара """
    item = get_object_or_404(Item, pk=pk)
    template = loader.get_template('main/item.html')
    context = {
        'name': item.name,
        'description': item.description,
        'price': int(item.price)/100,
        'stripe_public_key': settings.STRIPE_PUBLISHABLE_KEY,
        'item_id': pk,
    }
    return HttpResponse(template.render(context, request))


class ItemView(APIView):
    """
    Контроллер страницы покупки товара
    """
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

    @staticmethod
    def get(request, *args, **kwargs):
        path = request.path
        item_id = re.search(r'\d+', path).group(0)
        item = get_object_or_404(Item, id=item_id)
        session = get_session(item)
        return redirect(session['url'])
