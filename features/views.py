from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Feature
from .forms import FeatureForm
#from accounts.models import User

@login_required
def get_features(request):
    '''Get a list of all features and render them'''
    
    features = Feature.objects.filter(paid=True)
    show_button = Feature.objects.filter(paid=False, feature_author=request.user.id)
    
    return render(request,'features.html', {'features': features, 'show_button': show_button})
    

def single_feature(request, pk):
    '''Create a view that returns a single feature'''
    
    cart = request.session.get('cart', {})
    if pk in cart:
        in_cart = True
    else:
        in_cart = False
        
    feature = get_object_or_404(Feature, pk=pk)
    username = feature.feature_author
    return render(request, 'singlefeature.html', {'feature': feature, 'username': username, 'in_cart': in_cart})
    

def feature_form(request, pk=None):
    ''' Creates a form to create a feature'''
    
    if request.method == 'POST':
        
        #leaving commented out code incase i decide to allow a user to edit a feature request
        
        #feature = get_object_or_404(Feature, pk=pk) if pk else None
        
        form = FeatureForm(request.POST)#, instance=feature)
        
        if form.is_valid():
            feature=form.save(commit=False)
            feature.feature_author_id = request.user.id
            feature.price = 50
            feature.save()
            
            cart = request.session.get('cart', {})
            item_id = feature.pk
            
            cart[item_id] = cart.get(item_id, 1)
            request.session['cart'] = cart
        
            return redirect(single_feature, feature.pk)
    else:
        form = FeatureForm()
        return render(request, 'featureform.html', {'form': form })
    
    
