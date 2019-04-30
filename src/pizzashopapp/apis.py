from django.http import JsonResponse

from .serializers import PizzaShopSerializer,PizzaSerializer
from .models import PizzaShop,Pizza

def client_get_pizzashop(request):
    pizzashops = PizzaShopSerializer(
        PizzaShop.objects.all().order_by('-id'),
        many=True,
        context={'request':request}
    ).data

    context_dictionary = {
        "pizzashops": pizzashops,
    }

    return JsonResponse(context_dictionary)


def client_get_pizzas(request,pizzashop_id):
    pizzas = PizzaSerializer(
        Pizza.objects.all().filter(pizzashop_id=pizzashop_id).order_by('-id'),
        many=True,
        context={'request':request}
    ).data

    context_dictionary = {
        "pizzas": pizzas,
    }

    return JsonResponse(context_dictionary)
