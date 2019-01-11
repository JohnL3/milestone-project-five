from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Feature, PurchasedCount
from .forms import FeatureForm
from accounts.models import User

@login_required
def get_features(request):
    '''Get a list of all features and render them'''
    
    features = Feature.objects.filter(paid=True)
    print('features',features)
    return render(request,'features.html', {'features': features})
    

def single_feature(request, pk):
    '''Create a view that returns a single feature'''
    feature = get_object_or_404(Feature, pk=pk)
    
    return render(request, 'singlefeature.html', {'feature': feature})
    

def feature_form(request, pk=None):
    ''' Creates a form to create a feature'''
    
    if request.method == 'POST':
        # get instance of user to add to the form
        user = User.objects.get(pk=request.user.id)
        
        
        feature = get_object_or_404(Feature, pk=pk) if pk else None
        form = FeatureForm(request.POST, request.FILES, instance=feature)
    
        if form.is_valid():
            feature=form.save(commit=False)
            feature.feature_author = user
            feature.save()
            return redirect(single_feature, feature.pk)
    
    else:
        form = FeatureForm()
        return render(request, 'featureform.html', {'form': form })
    
    
