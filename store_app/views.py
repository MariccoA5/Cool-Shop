from django.shortcuts import render, HttpResponse
from .csv_interface import CSV_Interface
import requests
from requests_oauthlib import OAuth1
from . import csv_interface
from django.views.decorators.csrf import csrf_exempt
import os
from dotenv import load_dotenv
load_dotenv() 


products_interface = CSV_Interface('./data/products.csv')
shopping_cart_interface = CSV_Interface('./data/shopping_cart.csv')

product = products_interface.all_data
shopping_cart = shopping_cart_interface.all_data
# Create your views here.
def index(request):
  data = {'products': product}
  
  return render(request, 'index.html', data)

def petstore(request):
  data = {'products': product}
  
  return render(request, 'petstore.html', data)

def one_item(request, item):
  data = { 'item': item,
          'products': product
            }
  
  
  print(item)
  
  return render(request, 'one_item.html', data)

def gunstore(request):
  data = {'products': product}
  
  return render(request, 'gunstore.html', data)

def grocerystore(request):
  data = {'products': product}
  
  return render(request, 'grocerystore.html', data)

@csrf_exempt
def search(request):
  item = request.POST.get('user_input')

  auth = OAuth1(os.environ["key"], os.environ["secret"])
  endpoint = f"https://api.thenounproject.com/icon/{item}"

  response = requests.get(endpoint, auth=auth)
  response_json = response.json()
  print(response_json['icon'])
  icon = response_json['icon']['preview_url']
  
  
  data = { 'products': product,
            'item': item,
            'icon': icon }
  
  return render(request, 'search.html', data)


  
def cart(request):
  
  product = products_interface.all_data
  shopping_cart = shopping_cart_interface.all_data
  products_in_cart = []
  data={'items_in_cart': products_in_cart}
  total = 0
  for item in shopping_cart:
    id = item['id']
    for i in product:
      if i['id'] == id:
        total += int(i['cost'])
        products_in_cart.append(i)
        data['total'] = total
        
  return render(request, 'cart.html', data)
  

@csrf_exempt
def add_product(request, id):
  
  shopping_cart_interface.append_one_row_to_file({'id': id, 'quantity': 1})
  
  return HttpResponse('Good', content_type='text/plain')
    
  
  