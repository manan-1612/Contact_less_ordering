from django.shortcuts import render
from django.shortcuts import (get_object_or_404,
                              render,
                              HttpResponseRedirect)
 

from django.template import loader
from .models import food_item
from .models import Table
from .models import Order
from .models import Order_food_mapping
from .models import Customer
from django.utils import timezone
import datetime
import razorpay
from my_project.settings import ROZERPAY_API_KEY,ROZERPAY_API_SECRET_KEY
# Create your views here.


def menu(request, id):
    context={}
    temp=id
    temp_obj=Order.objects.get(order_id=id)
    context["ordid"]=temp_obj
    return render(request,'menu.html',context)

def home(request,id):
    flag = 0
    Table.objects.filter(tb_no=id).update(status=1)
    new_ord = Order.objects.create(tb_no = Table.objects.get(tb_no=id), date_time = timezone.now())
    new_ord.save()
    context={}
    context["ord"]=new_ord
    return render(request,'index.html',context)


def south(request, cat, id, tid):
  context1 = {}
  
  if cat == 'Recommanded':
    context1 = {
      "orderId" : id,
      "catagory" : cat,
      "mymembers" : food_item.objects.filter(avg_review = 5)
    }
    # new_set = myset[: len(myset) - n]
    # ans = []
    # for m in new_set:
    #   ans.add(food_item.objects.get(food_id = items.get(m)))
  else:
    context1 = {
      "orderId" : id,
      "catagory" : cat,
      "mymembers" : food_item.objects.filter(catagory = cat)
    }
#   context1["mymembers"]=food_item.objects.filter(catagory = cat)
  return render(request, 'south.html', context1)


def additem(request, cat, orderId, food_id):
    # context1 = {}
    if request.method == 'POST':
        num = int(request.POST['qnt'])
        foodid = food_id
        orderid = orderId
        print(orderid, food_id)
        if Order_food_mapping.objects.filter(order_id = Order.objects.get(order_id = orderid), food_id = food_item.objects.get(food_id=foodid)):
          item = Order_food_mapping.objects.get(order_id = Order.objects.get(order_id = orderid), food_id = food_item.objects.get(food_id=foodid))
          item.quantity = item.quantity + num
          foo=food_item.objects.get(food_id=foodid)
          item.order_price=foo.price*item.quantity
          # Order_food_mapping.object.update(order_id = Order.objects.get(order_id = orderid), food_id = food_item.objects.get(food_id=foodid), quantity=item.quantity)
          item.save()
        else:
          foo=food_item.objects.get(food_id=foodid)
          nmap = Order_food_mapping.objects.create(order_id = Order.objects.get(order_id = orderid), food_id = food_item.objects.get(food_id=foodid), quantity=num, order_price=num*foo.price)
          nmap.save()
        if cat == 'Recommanded':
          context1 = {
            "orderId" : orderid,
            "catagory" : cat,
            "mymembers" : food_item.objects.filter(avg_review = 5)
          }
        else:
          context1 = {
          "orderId" : orderid,
          "catagory" : cat,
          "mymembers" : food_item.objects.filter(catagory = cat)
          }
    return render(request,'south.html',context1)

def details(request, delId):
    context={}
    del_obj = Order.objects.get(order_id = delId)
    context["del"]=del_obj
    return render(request,'details.html',context)

def customer_details(request, billId):
    print("in customer")
    if request.method == 'POST':
       print("in post method")
       name = request.POST['fname']
       number = request.POST['num']
       email = request.POST['email']
       newc = Customer.objects.create(phone_no=number, email=email, name=name, bill_no=Order.objects.get(order_id = billId))
       newc.save()
       context={}
       context["billobj"]=newc
       return render(request, 'bill.html',context)

def order_status(request, id):
  print("In order status")
  items = Order_food_mapping.objects.filter(order_id = id)
  foods = []
  total_price = 0
  for i in items:
      fd = food_item.objects.filter(food_id = i.food_id.food_id)
      food = fd.first()
      foods.append(food)
      total_price = total_price + food.price * i.quantity
  context = {}
  print(foods)
  mylist = zip(foods, items)
  context = {
    "mylist" : mylist,
    "total_price" : total_price,
    "orderId" : id
  }

  return render(request,'order_status.html', context)

def bill(request, id):
  if request.method == 'POST':
       print("in post method")
       name = request.POST['fname']
       number = request.POST['num']
       email = request.POST['email']
       newc = Customer.objects.create(phone_no=number, email=email, name=name, bill_no=Order.objects.get(order_id = id))
       newc.save()
  items = Order_food_mapping.objects.filter(order_id = id)
  billno=id
  foods = []
  total_price = 0
  for i in items:
      fd = food_item.objects.filter(food_id = i.food_id.food_id)
      food = fd.first()
      foods.append(food)
      total_price = total_price + food.price * i.quantity
  context = {}
  print(foods)
  gsttext = 0.05*total_price
  total = gsttext+total_price
  new_obj = Order.objects.get(order_id = id)
  new_obj.amount=total
  new_obj.save()
  date=new_obj.date_time
  mylist = zip(foods, items)
  context = {
    "date": date,
    "order_id" : id,
    "mylist" : mylist,
    "total_price" : total_price,
    "gsttext" : gsttext,
    "total":total,
    "billno":billno
  }
  return render(request,'bill.html', context)

client = razorpay.Client(auth=(ROZERPAY_API_KEY,ROZERPAY_API_SECRET_KEY))
def payment(request, o_id, price):
  table = Order.objects.filter(order_id = o_id)
  tab_no = table.first().tb_no.tb_no
  Table.objects.filter(tb_no = tab_no).update(status = 0)
  price = float(price)
  order_amount = price * 100
  order_currency = 'INR'
  
  payment_order = client.order.create(dict(amount=order_amount, currency = order_currency, payment_capture = 1))
  payment_order_id = payment_order['id']
  context = {
    'amount' : order_amount,
    'api_key' : ROZERPAY_API_KEY,
    'order_id' : payment_order_id
  }
  return render(request, 'welc.html', context)

def delete_item(request, o_id, f_id):
  items = Order_food_mapping.objects.filter(order_id = o_id)
  foods = []
  total_price = 0
  for i in items:
    fd = food_item.objects.filter(food_id = i.food_id.food_id)
    food = fd.first()
    if food.food_id != f_id:
      foods.append(food)
      total_price = total_price + food.price * i.quantity
    else:
      if i.quantity > 1:
        i.quantity = i.quantity - 1
        i.order_price = i.quantity*food.price
        i.save()
        foods.append(food)
        total_price = total_price + food.price * i.quantity
      else:
        i.delete()
    
  context = {}
  mylist = zip(foods, items)
  context = {
    "mylist" : mylist,
    "total_price" : total_price,
    "orderId" : o_id
  }

  return render(request, 'order_status.html',context)

def comment(request, o_id, f_id):
  if request.method == 'POST':
    md = request.POST['modf']
    items = Order_food_mapping.objects.filter(order_id = o_id)
    foods = []
    total_price = 0
    for i in items:
      fd = food_item.objects.filter(food_id = i.food_id.food_id)
      food = fd.first()
      foods.append(food)
      total_price = total_price + food.price * i.quantity
      if food.food_id == f_id:
        i.modification = md
        i.save()
      
    context = {}
    mylist = zip(foods, items)
    context = {
      "mylist" : mylist,
      "total_price" : total_price,
      "orderId" : o_id
    }
        
  return render(request, 'order_status.html', context)

# def order_status(request, id):
#   items = Order_food_mapping.objects.filter(order_id = id)
#   foods = []
#   total_price = 0
#   for i in items:
#       fd = food_item.objects.filter(food_id = i.food_id.food_id)
#       food = fd.first()
#       foods.append(food)
#       total_price = total_price + food.price * i.quantity
#   context = {}
#   print(foods)
#   mylist = zip(foods, items)
#   context = {
#     "mylist" : mylist,
#     "total_price" : total_price
#   }

#   return render(request,'order_status.html', context)

