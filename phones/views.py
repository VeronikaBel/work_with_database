from django.shortcuts import render,get_object_or_404

from phones.models import Phone


def show_catalog(request):
    sort_by = request.GET.get('sort')
    if sort_by == 'name':
        phones = Phone.objects.all().order_by('name')
    elif sort_by == 'max_price':
        phones = Phone.objects.all().order_by('-price')
    elif sort_by == 'min_price':
        phones = Phone.objects.all().order_by('price')
    else:
        phones = Phone.objects.all()
    context = {'phones':phones}
    return render(request, 'catalog.html', context)


def show_product(request, slug):
    phone = get_object_or_404(Phone, slug=slug)
    context = {'phone':phone}
    return render(request, 'product.html', context)
