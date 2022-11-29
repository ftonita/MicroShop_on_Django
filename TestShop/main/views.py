from django.shortcuts import render
import stripe
from .models import Item
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import Http404


stripe.api_key = 'sk_test_4eC39HqLyjWDarjtT1zdp7dc'

def __getSession(request, item: Item):
    session = stripe.checkout.Session.create(
    line_items=[{
    'price_data': {
        'currency': 'usd',
        'product_data': {
        'name': f'{item.name}',
        },
        'unit_amount': int(float(item.price) * 100),
    },
    'quantity': 1,
    }],
    mode='payment',
    success_url='http://localhost:8000/success',
    cancel_url='http://localhost:8000/',
    )
    return session


def index(request):
	items = Item.objects.all()
	return render(request, 'main/index.html', {'items': items})

def about(request):
	return render(request, 'main/about.html')



@api_view(['GET'])
def buy(request, idx, format=None):
    try:
        item = Item.objects.get(id=idx)
        session = __getSession(request, item)
        print(session.url)
        return Response({
            'id':f'{session.id}',
            'redirect_url':session.url,
            }, status=302)
    except Item.DoesNotExist:
        raise Http404

def item(request, idx, format=None):
    try:
        item = Item.objects.get(id=idx)
        return render(request, 'main/item.html', {'item': item})
    except Item.DoesNotExist:
        raise Http404

def success(request):
    items = Item.objects.all()
    return index(request)

def pageNotFound(request, exception):
    return render(request, 'main/404.html', status=404)

def internalServerError(request):
    raise Http404