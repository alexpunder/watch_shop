from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from django.db.models import Count
from django.views.decorators.http import require_POST


from website.constants import PRODUCTS_ON_PAGE
from .models import Watch, Condition, Brand, Gender, BodyMaterial, CaseShape
from .forms import AddToCart
from .cart import Cart


def watch_list(request):
    template_name = 'watches/watches_with_sidebar.html'
    watches = Watch.objects.filter(
        is_published=True, is_available=True
    )

    max_price_1 = request.GET.get('max_price_1')
    max_price_2 = request.GET.get('max_price_2')
    min_price = request.GET.get('min_price')
    condition_ids = request.GET.getlist('condition')
    brand_ids = request.GET.getlist('brand')
    gender_ids = request.GET.getlist('gender')
    body_material_ids = request.GET.getlist('body_material')
    case_shape_ids = request.GET.getlist('case_shape')

    price_filters = {}

    if max_price_1:
        price_filters['price__lte'] = max_price_1
    if max_price_2:
        price_filters['price__lte'] = max_price_2
    if min_price:
        price_filters['price__gte'] = min_price

    if price_filters:
        watches = watches.filter(**price_filters)

    if condition_ids:
        watches = watches.filter(condition__id__in=condition_ids)
        condition = Condition.objects.filter(id__in=condition_ids)
    else:
        condition = None

    if brand_ids:
        watches = watches.filter(brand__id__in=brand_ids)
        brand = Brand.objects.filter(id__in=brand_ids)
    else:
        brand = None

    if gender_ids:
        watches = watches.filter(gender__id__in=gender_ids)
        gender = Gender.objects.filter(id__in=gender_ids)
    else:
        gender = None

    if body_material_ids:
        watches = watches.filter(body_material__id__in=body_material_ids)
        body_material = BodyMaterial.objects.filter(id__in=body_material_ids)
    else:
        body_material = None

    if case_shape_ids:
        watches = watches.filter(case_shape__id__in=case_shape_ids)
        case_shape = CaseShape.objects.filter(id__in=case_shape_ids)
    else:
        case_shape = None

    filters_applied = any(
        [
            max_price_1, max_price_2, min_price, condition_ids,
            brand_ids, gender_ids, body_material_ids, case_shape_ids
        ]
    )

    if not filters_applied:
        paginator = Paginator(watches, PRODUCTS_ON_PAGE)
        page_number = request.GET.get('page')
        page_obj_paginate = paginator.get_page(page_number)
        page_obj = page_obj_paginate
    else:
        page_obj = watches

    cart_product_form = AddToCart()

    category_condition = Condition.objects.annotate(
        num_watches=Count('watch')
    )
    category_brand = Brand.objects.annotate(
        num_watches=Count('watch')
    )
    category_gender = Gender.objects.annotate(
        num_watches=Count('watch')
    )
    category_body_material = BodyMaterial.objects.annotate(
        num_watches=Count('watch')
    )
    category_case_shape = CaseShape.objects.annotate(
        num_watches=Count('watch')
    )
    category_price_low = Watch.objects.filter(
        price__lte=5000
    ).count()
    category_price_mid = Watch.objects.filter(
        price__lte=50000
    ).count()
    category_price_hight = Watch.objects.filter(
        price__gte=50000
    ).count()

    context = {
        'page_obj': page_obj,
        'cart_product_form': cart_product_form,
        'category_condition': category_condition,
        'category_brand': category_brand,
        'category_gender': category_gender,
        'category_body_material': category_body_material,
        'category_case_shape': category_case_shape,
        'category_price_low': category_price_low,
        'category_price_mid': category_price_mid,
        'category_price_hight': category_price_hight,
        'filters_applied': filters_applied,
        'condition': condition,
        'brand': brand,
        'gender': gender,
        'body_material': body_material,
        'case_shape': case_shape
    }
    return render(request, template_name, context)


def watch_detail(request, pk):
    template_name = 'watches/watch_details.html'
    product = get_object_or_404(Watch, pk=pk)
    cart_product_form = AddToCart()
    similar_products = Watch.objects.filter(
        mechanism=product.mechanism, gender=product.gender
    ).exclude(
        id=product.id
    )
    context = {
        'product': product,
        'similar_products': similar_products,
        'cart_product_form': cart_product_form,
    }
    return render(request, template_name, context)


@require_POST
def cart_add(request, pk):
    cart = Cart(request)
    watch = get_object_or_404(Watch, pk=pk)
    form = AddToCart(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(
            watch=watch, update_quantity=cd['update']
        )
    return redirect('shop:cart_detail')


def cart_remove(request, pk):
    cart = Cart(request)
    watch = get_object_or_404(Watch, pk=pk)
    cart.remove(watch)
    return redirect('shop:cart_detail')


def cart_detail(request):
    template_name = 'watches/cart_detail.html'
    cart = Cart(request)
    context = {'cart': cart}
    return render(request, template_name, context)
