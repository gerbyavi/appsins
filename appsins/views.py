from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home_page(request):
    return render(request, 'home.html', {
        'new_item_text': request.POST.get('item_text', ''), ### catching the post from the request by it's input name="item_text" - not value !!!! 
    })
