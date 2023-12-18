from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from django.db.models import Count
from django.views.decorators.http import require_POST


from .models import Watch, Condition, Brand, Gender, BodyMaterial, CaseShape
from .forms import AddToCart
from .cart import Cart


PRODUCTS_ON_PAGE = 2


def watch_list(request):
    template_name = 'watches/watches_with_sidebar.html'
    watches = Watch.objects.filter(
        is_published=True, is_available=True
    )

    condition_ids = request.GET.getlist('condition')
    brand_ids = request.GET.getlist('brand')
    gender_ids = request.GET.getlist('gender')
    body_material_ids = request.GET.getlist('body_material')
    case_shape_ids = request.GET.getlist('case_shape')

    if condition_ids:
        watches = watches.filter(condition__id__in=condition_ids)
    if brand_ids:
        watches = watches.filter(brand__id__in=brand_ids)
    if gender_ids:
        watches = watches.filter(gender__id__in=gender_ids)
    if body_material_ids:
        watches = watches.filter(body_material__id__in=body_material_ids)
    if case_shape_ids:
        watches = watches.filter(case_shape__id__in=case_shape_ids)

    paginator = Paginator(watches, PRODUCTS_ON_PAGE)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
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
    context = {
        'page_obj': page_obj,
        'cart_product_form': cart_product_form,
        'category_condition': category_condition,
        'category_brand': category_brand,
        'category_gender': category_gender,
        'category_body_material': category_body_material,
        'category_case_shape': category_case_shape
    }
    return render(request, template_name, context)


def watch_detail(request, pk):
    template_name = 'watches/watch_details.html'
    product = get_object_or_404(Watch, pk=pk)
    cart_product_form = AddToCart()
    context = {
        'product': product, 'cart_product_form': cart_product_form
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
