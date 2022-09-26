from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Data
# Create your views here.

def index(request):

    data = Data.objects.all()
    page = Paginator(data, 3)

    page_list = request.GET.get('page')
    page = page.get_page(page_list)

    context = {
        'page': page,
    }
    return render(request, 'dashboard/index.html', context)