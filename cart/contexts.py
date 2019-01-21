from django.shortcuts import get_object_or_404
from features.models import Feature


def cart_contents(request):
    """
    Ensures that the cart contents are available when rendering every page
    """
    
    owed_for = Feature.objects.filter(paid=False, feature_author=request.user.id)
   
    cart = request.session.get('cart', {})
    
    cart_items = []
    total = 0
    feature_count = 0
    for item_id, quantity in cart.items():
        feature = get_object_or_404(Feature, pk=item_id)
        
        total += quantity * 50
       
        feature_count += quantity
        cart_items.append({'item_id':item_id, 'quantity': quantity, 'feature': feature})
    
    #if user has suggested feature and it is not paid for and relogs in, add that feature to cart
    if owed_for:
        for feature in owed_for:
            item_id = feature.id
            cart[item_id] = cart.get(item_id, 1)
            request.session['cart'] = cart
            
    return { 'cart_items': cart_items, 'total': total, 'feature_count': feature_count }