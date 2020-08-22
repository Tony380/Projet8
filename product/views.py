from django.shortcuts import render, redirect
from .models import Product, Favorite
from django.contrib import messages
from django.db import IntegrityError


def search(request):
    query = request.GET.get('query')
    if query != '':
        products = Product.objects.filter(name__icontains=query).order_by('nutriscore')

        if not products.exists():
            products = Product.objects.filter(brands__icontains=query).order_by('nutriscore')

        if not products.exists():
            messages.success(request, "Nous n'avons trouvé aucun produit correspondant à votre recherche")
            return redirect('index')

        context = {'products': products}
        return render(request, 'product/search.html', context)

    else:
        messages.success(request, "Vous n'avez rien saisi")
        return redirect('index')


def product(request, product_id):
    prod = Product.objects.get(id=product_id)
    context = {'prod': prod}
    return render(request, 'product/product.html', context)


def substitute(request, product_id):
    prod = Product.objects.get(id=product_id)
    cat = prod.categories.get()
    subs = cat.products.all().order_by('nutriscore')
    sub_list = []
    for i in subs:
        if i.nutriscore < prod.nutriscore:
            sub_list.append(i)
        elif i.nutriscore == prod.nutriscore:
            sub_list.append(i)
    sub_list.remove(prod)
    context = {'prod': prod,
               'sub_list': sub_list}
    return render(request, 'product/substitute.html', context)


def save(request, product_id, prod_id):
    user = request.user
    try:
        fav = Favorite.objects.filter(user_id=user.id, sub_id=product_id, prod_id=prod_id)
        if not fav:
            Favorite.objects.create(user_id=user.id, sub_id=product_id, prod_id=prod_id)
            messages.success(request, 'Produit sauvegardé')
            return redirect('index')
        else:
            messages.success(request, 'Le produit est déjà sauvegardé')
            return redirect('index')

    except IntegrityError:
        return redirect('index')


def favorite(request):
    user = request.user
    favs = Favorite.objects.filter(user_id=user.id)
    context = {
        'user': user,
        'favs': favs,
    }
    return render(request, 'favorite.html', context)


def delete(request, fav):
    favori = Favorite.objects.filter(id=fav)
    favori.delete()
    messages.success(request, 'Le favori à bien été supprimé')
    return redirect('index')
