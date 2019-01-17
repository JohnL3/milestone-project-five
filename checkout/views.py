from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages


@login_required()
def checkout(request):
    
    return render(request, "checkout.html")
