from django.shortcuts import render, redirect, reverse, HttpResponse
from django.contrib.auth.decorators import login_required
import json
from features.models import Feature

def view_cart(request):
    """A view that renders the cart contents page"""
   
    return render(request, "cart.html")

@login_required   
def add_to_cart(request, item_id):
    """Add a feature to the cart"""
    
    
    if request.method == 'POST':
        
        cart = request.session.get('cart', {})
        cart[item_id] = 1
        
        request.session['cart'] = cart
        
        response={'msg': 'all good here'}
        return HttpResponse(json.dumps(response), content_type='application/json')
    else:
        response={'msg': 'Something went wrong'}
        return HttpResponse(json.dumps(response), content_type='application/json')
    

@login_required
def adjust_cart(request):
    """Remove an feature from the cart"""
    
    item_id = request.POST['item_id']
    
    cart = request.session.get('cart', {})
    
    #Remove feature from cart
    cart.pop(item_id)
        
    request.session['cart'] = cart
    
    response={'msg': 'all good'}
    return HttpResponse(json.dumps(response), content_type='application/json')
