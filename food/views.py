from django.shortcuts import render
from django.http import HttpResponse
from .models import Item
from django.template import loader
# Create your views here.
#views basically process the urls
def index(request):

    item_list=Item.objects.all()
    template=loader.get_template('food/index.html')
    context={
        'item_list':item_list,

    }

    return HttpResponse(template.render(context,request))

def item(request):
    return HttpResponse("Hi user how are u?, you came to items views")

def detail(request,item_id):
    Item.objects.get(pk=item_id)
    return HttpResponse("this is item no/id: %s" % item_id)