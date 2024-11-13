from django.shortcuts import render
from shop.models import Logo, Product, ReviewRating, Banner



def home(request):
    # Fetch products that are available
    products = Product.objects.all().filter(is_available=True).order_by('created_date')

    # Get the reviews for each product
    reviews = None
    for product in products:
        reviews = ReviewRating.objects.filter(product_id=product.id, status=True)

    # Get the first banner
    banner = Banner.objects.first()

    logo = Logo.objects.first()  # Fetch the logo

    # Pass banner along with other data to the context
    context = {
        'products': products,
        'reviews': reviews,
        'banner': banner,  # Add banner to the context
        'logo': logo, 
    }

    return render(request, 'home.html', context)
