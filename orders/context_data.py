from .models import Cart,Cart_Detail

def get_context_data(request):
    if request.user.is_authenticated:
        cart,created= Cart.objects.get_or_create(user=request.user,status='Inprogress')
        cart_detail=Cart_Detail.objects.filter(cart=cart)
        return {'cart':cart,'cart_detail':cart_detail}
    else:
        return {}