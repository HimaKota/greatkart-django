from django.shortcuts import render, get_object_or_404, redirect
from .models import Product,ReviewRating, ProductGallery
from category.models import Category
from cart.models import CartItem
from django.db.models import Q

from cart.views import _cart_id
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.http import HttpResponse
from .forms import ReviewForm
from django.contrib import messages
from orders.models import OrderProduct

# Create your views here.

#get categories
def store(request, category_slug=None):
    categories = None
    products = None

    if category_slug != None:
        categories = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(category=categories, is_available=True)
        #display paginator in all categories
        paginator = Paginator(products, 1)
        page = request.GET.get('page')
        paged_products = paginator.get_page(page)
        product_count = products.count()
    else:
        products = Product.objects.all().filter(is_available=True).order_by('id')
        #In stor page display 6 products foe every paginator
        paginator = Paginator(products, 6)
        page = request.GET.get('page')
        #send get_page request to html page
        paged_products = paginator.get_page(page)      
        product_count = products.count()
    # Get the reviews
    reviews = None
    for product in products:
        reviews = ReviewRating.objects.filter(product_id=product.id, status=True)
    context = {
        'products': paged_products,
        'product_count': product_count,
        'reviews' :reviews,
    }
    return render(request, 'store/store.html', context)


#for product detail page
def product_detail(request,category_slug,product_slug):
    try:
        single_product = Product.objects.get(category__slug=category_slug, slug=product_slug)
        in_cart = CartItem.objects.filter(cart__cart_id=_cart_id(request), product=single_product).exists()
    except Exception as e:
        raise e
    if request.user.is_authenticated:
        try:
            orderproduct = OrderProduct.objects.filter(user=request.user, product_id=single_product.id).exists()
        except OrderProduct.DoesNotExist:
            orderproduct = None
    else:
        orderproduct = None
     # Get the reviews
    reviews = ReviewRating.objects.filter(product_id=single_product.id, status=True)

     # Get the product gallery
    product_gallery = ProductGallery.objects.filter(product_id=single_product.id)

    context = {
        'single_product': single_product,
        'in_cart'       : in_cart,
        'orderproduct': orderproduct,
        'reviews': reviews,
        'product_gallery' : product_gallery,
    }
    return render(request, 'store/product_detail.html', context)
   
def search(request):
    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        paged_products = 0
        if keyword:
            products = Product.objects.order_by('-created_date').filter(Q(description__icontains=keyword) | Q(product_name__icontains=keyword))
            paginator = Paginator(products, 3)
            page = request.GET.get('page')
            #send get_page request to html page
            paged_products = paginator.get_page(page)    
            product_count = products.count()
        else:
            keyword = None
        context = {
            'products': paged_products,
            'product_count': product_count,
            'keyword' :keyword,
        }
        return render(request, 'store/store.html', context)
    return render(request, 'store/store.html')

def submit_review(request, product_id):
    url = request.META.get('HTTP_REFERER')
    if request.method == 'POST':
        try:
            reviews = ReviewRating.objects.get(user__id=request.user.id, product__id=product_id)
            form = ReviewForm(request.POST, instance=reviews)
            form.save()
            messages.success(request, 'Thank you! Your review has been updated.')
            return redirect(url)
        except ReviewRating.DoesNotExist:
            form = ReviewForm(request.POST)
            if form.is_valid():
                data = ReviewRating()
                data.rating = form.cleaned_data['rating']
                data.review = form.cleaned_data['review']
                data.ip = request.META.get('REMOTE_ADDR')
                data.product_id = product_id
                data.user_id = request.user.id
                data.save()
                messages.success(request, 'Thank you! Your review has been submitted.')
                return redirect(url)