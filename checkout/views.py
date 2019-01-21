from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import MakePaymentForm, OrderForm
from .models import OrderLineItem
from django.conf import settings
from django.utils import timezone
import stripe
from features.models import PurchasedCount, Feature
from accounts.models import User

stripe.api_key = settings.STRIPE_SECRET

@login_required()
def checkout(request):
    cart = request.session.get('cart', {})
    if request.method == 'POST' and len(cart) > 0:
        user = User.objects.get(pk=request.user.id)
        order_form = OrderForm(request.POST)
        payment_form = MakePaymentForm(request.POST)
        
        if order_form.is_valid() and payment_form.is_valid():
            order = order_form.save(commit=False)
            order.date = timezone.now()
            order.save()
            
            cart = request.session.get('cart', {})
           
            total = 0
            for id, quantity in cart.items():
                
                feature = get_object_or_404(Feature, pk=id)
                
                total += 1 * 50
                order_line_item = OrderLineItem(
                    order = order, 
                    feature = feature, 
                    quantity = quantity
                    )
                order_line_item.save()
                
            try:
                print('TOTAL',total)
                customer = stripe.Charge.create(
                    amount = int(total * 100),
                    currency = "EUR",
                    card = payment_form.cleaned_data['stripe_id'],
                )
            except stripe.error.CardError:
                messages.error(request, "Your card was declined!")
                
            if customer.paid:
                
                for id, quantity in cart.items():
                    purchased_count = PurchasedCount()
                    purchased_count.name = get_object_or_404(Feature, pk=id)
                    
                    purchased_count.creator = user
                    purchased_count.save()
                    
                    #Keep track of how many purchased each feature
                    feature = get_object_or_404(Feature, pk=id)
                    purchased = feature.purchased
                    feature.purchased = purchased +1
                    if feature.paid == False:
                        feature.paid = True
                    feature.save()
                    
                    
                
                messages.error(request, "You have successfully paid")
                request.session['cart'] = {}
                
                return redirect(reverse('profile'))
            else:
                messages.error(request, "Unable to take payment")
        else:
            print(payment_form.errors)
            messages.error(request, "We were unable to take a payment with that card!")
    else:
        payment_form = MakePaymentForm()
        order_form = OrderForm(label_suffix='')
        
        return render(request, "checkout.html",{'order_form': order_form, 'payment_form': payment_form, 'publishable': settings.STRIPE_PUBLISHABLE})
