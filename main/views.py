from django.shortcuts import render, redirect
from .models import ReviewableProduct, ImageModel, FrontPageImages, Order, CartProduct, ContactModel, FormWithCaptcha, ProductReview, ProductQuestion, ProductAnswer, Profile
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import logout, authenticate, login
from django.contrib import messages
from .forms import NewUserForm, OrderForm, QuantityEditForm, ContactForm
from django.contrib.auth.models import User
from django.urls import reverse
from django.http import JsonResponse
# Create your views here.
def homepage(request):
    try:
        fpis = FrontPageImages.objects.all()
        products = ReviewableProduct.objects.filter(featured=True)
        frameimg = ImageModel.objects.get(tag="frameimg")
        electricalimg = ImageModel.objects.get(tag="electricalimg")
        motorsimg = ImageModel.objects.get(tag="motorsimg")
        finalizeimg = ImageModel.objects.get(tag="finalizeimg")
    except FrontPageImages.DoesNotExist:
        active_fpi = None
        fpis = None
    except ReviewableProduct.DoesNotExist:
        products = None
    except ImageModel.DoesNotExist:
        frameimg = None
        electricalimg = None
        motorsimg = None
        finalizeimg = None
    return render(request = request,
                  template_name='main/home.html',
                  context = {"motorsimg":motorsimg, "finalizeimg":finalizeimg, "electricalimg":electricalimg, "frameimg":frameimg, "fpis":fpis, "products":products})

def register(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            try:
                User.objects.get(email=form.cleaned_data.get('email'))
                messages.error(request, "The email {form.cleaned_data.get('email')} has already been taken")
                User.objects.get(username=form.cleaned_data.get('username'))
                messages.error(request, "The email {form.cleaned_data.get('username')} has already been taken")
            except User.DoesNotExist:
                user = form.save()
                profile = Profile(username=user).save()
                username = form.cleaned_data.get('username')
                messages.success(request, f"New account created: {username}")
                login(request, user)
                return redirect("main:homepage")

        else:
            for msg in form.error_messages:
                messages.error(request, f"{msg}: {form.error_messages[msg]}")

            return render(request = request,
                          template_name = "main/register.html",
                          context={"form":form})

    form = NewUserForm
    return render(request = request,
                  template_name = "main/register.html",
                  context={"form":form})


def inventory(request):
    return render(request = request,
                  template_name='main/inventory.html',
                  context = {"products":ReviewableProduct.objects.all()[:6]})

def design(request):
    return render(request = request,
                  template_name='main/design.html',
                  context = {"products":ReviewableProduct.objects.all})

def contactus(request):
    if request.method == 'POST':
        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():
            contact_model = ContactModel.objects.create()
            try:
                if request.user.is_authenticated:
                    contact_model.user_profile = Profile.objects.get(username=request.user)
                    contact_model.email = contact_form.cleaned_data.get('email')
                    contact_model.review_description = contact_form.cleaned_data.get('message_description')
                    contact_model.review_content = contact_form.cleaned_data.get('message_content')
                    contact_model.save()
                    messages.success(request, "Thanks for sending us a message! We'll get back to you as soon as possible!")
                else:
                    messages.error(request, "It looks like you aren't logged in. Login in an try again!")
                    contact_model.delete()
            except Profile.DoesNotExist:
                contact_model.delete()
                messages.error(request, "It looks like you aren't logged in. <a href='/login/'>Login</a> or <a href='/register/'>Register</a> to submit!")
            return redirect('/')
    contact_form = ContactForm
    return render(request = request,
                  template_name='main/contactus.html',
                  context = {"contact_form":contact_form})

def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}")
                return redirect('/')
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request = request,
                    template_name = "main/login.html",
                    context={"form":form})

def logout_request(request):
    logout(request)
    messages.info(request, "Logged Out Successfully!")
    return redirect("main:homepage")

def storebody(request):
    try:
        product = ReviewableProduct.objects.filter(category='body')
    except ReviewableProduct.DoesNotExist:
        pass
    return render(request = request,
                  template_name='main/store/body.html',
                  context={'products': product})

def designdownloadeditor(request):
    return render(request = request,
                  template_name='main/design/downloadeditor.html',)
def designelectrical(request):
    return render(request = request,
                  template_name='main/design/electrical.html',)
def designphysicalstructure(request):
    return render(request = request,
                  template_name='main/design/physicalstructure.html',)
def longproddesc(request, product_title):
    if request.method == 'POST':
        messages.info(request, 'post')
        form = OrderForm(request.POST)
        if form.is_valid():
            quantity = form.cleaned_data['post']
            try:
                prod = ReviewableProduct.objects.get(title=product_title)
            except ReviewableProduct.DoesNotExist:
                return redirect('main:homepage')
            cart_product = CartProduct.objects.create()
            cart_product.number = quantity
            cart_product.product = prod
            try:
                profile = Profile.objects.get(username=request.user)
                matched = False
                for cartproduct in profile.cart.all():
                    if cartproduct.product.title == cart_product.product.title:
                        cartproduct.number = cartproduct.number + cart_product.number
                        cartproduct.save()
                        matched = True
                if matched == False:
                    cart_product.save()
                    profile.cart.add(cart_product)
            except Profile.DoesNotExist:
                return redirect('main:homepage')
            return redirect("/")
        else:
            messages.error(request, 'ERROR')
            return redirect("main:homepage")
    messages.info(request, 'not post')
    form = OrderForm
    formcaptcha = FormWithCaptcha()
    try:
        product = ReviewableProduct.objects.get(title=product_title)
    except ReviewableProduct.DoesNotExist:
        pass
    try:
        reviews = ProductReview.objects.filter(reviewableproduct=product)
    except ProductReview.DoesNotExist:
        pass
    try:
        questions = ProductQuestion.objects.filter(applied_product=product)
    except ProductQuestion.DoesNotExist:
        pass
    try:
            answers = ProductAnswer.objects.all()
    except ProductAnswer.DoesNotExist:
            pass
    return render(request = request,
                  template_name='main/store/longproddesc.html',
                  context = {"product":product, "formcaptcha":formcaptcha, "form":form, "reviews":reviews, "questions":questions, "answers":answers})

def total_cart_price2(cart):
    total_cart_price = 0
    for cart_item in cart:
        cart_item.total = cart_item.product.price * cart_item.number
        total_cart_price = total_cart_price + cart_item.total
        cart_item.total = format(cart_item.total, '.2f')
    total_cart_price = format(total_cart_price, '.2f')
    return total_cart_price

def cart(request):
    try:
        if request.user.is_authenticated:
            prof = Profile.objects.get(username=request.user)
            messages.info(request, prof)
            cart2 = prof.cart.all()
            messages.info(request, cart2)
            quantity_edit_form = QuantityEditForm
            total_cart_price = total_cart_price2(cart2)
            return render(request = request,
                          template_name="main/cart.html",
                          context = {"profile":prof, "cart":cart2, "total_cart_price":total_cart_price, "quantity_edit_form":quantity_edit_form})
    except Profile.DoesNotExist:
        return redirect("main:homepage")

def cartchg(request, product_title):
    if request.method == 'POST':
        messages.info(request, 'post')
        form = QuantityEditForm(request.POST)
        if form.is_valid():
            quantity = form.cleaned_data['post']
            prof = Profile.objects.get(username=request.user)
            target_cart_product = prof.cart.all().get(product=ReviewableProduct.objects.get(title=product_title))
            target_cart_product.number = quantity
            target_cart_product.save()
            return redirect('main:cart')
        else:
            messages.error(request, 'ERROR')
            return redirect("main:homepage")
    else:
        return redirect("main:homepage")

def deletecartitem(request, product_title):
    if request.method == 'POST':
        prof = Profile.objects.get(username=request.user)
        target_cart_product = prof.cart.all().get(product=ReviewableProduct.objects.get(title=product_title))
        target_cart_product.delete()
    return redirect('main:cart')

#def checkout(request):
    #if request.method == 'POST':
    #    order_id = request.session.get('order_id')
    #    order = get_object_or_404(Order, id=order_id)
    #    host = request.get_host()
    #    paypal_dict = {
        #    'business': settings.PAYPAL_RECEIVER_EMAIL,
    #        'amount': '%.2f' % total_cart_price(Profile.objects.get(username=request.user).cart.all()),
    #        'item_name': 'Order {}'.format(order.id),
        #    'invoice': str(order.id),
    #        'currency_code': 'USD',
    #        'notify_url': 'http://{}{}'.format(host, reverse('paypal-ipn')),
    #        'return_url': 'http://{}{}'.format(host, reverse('payment:done')),
    #        'cancel_return': 'http://{}{}'.format(host, reverse('payment:cancelled')),
    #    }
        #form = PayPalPaymentsForm(initial=paypal_dict)
    #    return render(request, 'main/checkout.html', {'order': order, 'form':form})

    #return render(request = request,
    #              template_name='main/checkout.html',)

def checkout(request):
    if request.method == 'POST':
        order = Order.objects.create(totalprice=total_cart_price2(Profile.objects.get(username=request.user).cart.all()))
        order.orders.set(Profile.objects.get(username=request.user).cart.all())
        order.save()
        request.session['order_id'] = order.id
        return redirect(reverse('payment:process'))
    else:
        return render(request = request,template_name='main/checkout.html')

def addonetocart(request, product_title):
    try:
        prod = ReviewableProduct.objects.get(title=product_title)
    except ReviewableProduct.DoesNotExist:
        return redirect('main:homepage')
    cart_product = CartProduct.objects.create()
    cart_product.number = 1
    cart_product.product = prod
    try:
        profile = Profile.objects.get(username=request.user)
        matched = False
        for cartproduct in profile.cart.all():
            if cartproduct.product.title == cart_product.product.title:
                cartproduct.number = cartproduct.number + cart_product.number
                cartproduct.save()
                messages.success(request, "One more {prod.title} added to cart!")
                matched = True
        if matched == False:
            cart_product.save()
            profile.cart.add(cart_product)
            messages.success(request, "One {prod.title} added to cart!")
    except Profile.DoesNotExist:
        messages.error(request, "Log in to add an item to cart!")
        return redirect('/')
    return redirect("/")

def constructor(request):
    return render(request = request,
                  template_name='main/constructor.html',)

def inventorychg(request, sort_id):
    #price filtering
    def filterOnPrice(min, max):
        for product in ReviewableProduct.objects.all():
            if product.price < max and product.price > min:
                filtered_products.append(product)
    filtered_products = ReviewableProduct.objects.all()
    price_valid = True
    i = 0
    try:
        value = int(sort_id[5])
        filtered_products = []
    except ValueError:
        price_valid = False
    while price_valid:
        try:
            value = int(sort_id[5 + i])
        except ValueError:
            price_valid = False
            break
        if value > 0 and value < 10:
            price_valid = True
            if value == 1:
                filterOnPrice(0,10)
            if value == 2:
                filterOnPrice(9.99,20)
            if value == 3:
                filterOnPrice(19.99,30)
            if value == 4:
                filterOnPrice(29.99,50)
            if value == 5:
                filterOnPrice(49.99,75)
            if value == 6:
                filterOnPrice(74.99,100)
            if value == 7:
                filterOnPrice(100,9999999999)
        else:
            price_valid = False
        i = i + 1
    #end of price filtering

    #beginning of category filtering
    try:
        category_id = int(sort_id[sort_id.find("c")+1])
        category_valid = True
        temp = ReviewableProduct.objects.none()
    except ValueError:
        category_valid = False
        temp = filtered_products
    while category_valid:
        j = 1
        if category_id == 1:
            temp = temp | filtered_products.filter(category="frame")
        if category_id == 2:
            temp = temp | filtered_products.filter(category="electrical")
        if category_id == 3:
            temp = temp | filtered_products.filter(category="motor")
        else:
            category_valid = False
        try:
            j = j+1
            category_id = int(sort_id[sort_id.find("c")+j])
            category_valid = True
        except ValueError:
            category_valid = False
    filtered_products = temp
    ReviewableProduct.objects.none()
    #end of category filtering

    #beginning of brand filtering
    try:
        brand_id = int(sort_id[sort_id.find("b")+1])
        brand_valid = True
        temp = ReviewableProduct.objects.none()
    except ValueError:
        brand_valid = False
        temp = filtered_products
    while brand_valid:
        j = 1
        if brand_id == 1:
            temp = temp | filtered_products.filter(brand="Skystric Exclusive")
        if brand_id == 2:
            temp = temp | filtered_products.filter(brand="Luminier")
        if brand_id == 3:
            temp = temp | filtered_products.filter(brand="TommyFPV")
        else:
            brand_valid = False
        try:
            j = j+1
            brand_id = int(sort_id[sort_id.find("b")+j])
            brand_valid = True
        except ValueError:
            brand_valid = False
    filtered_products = temp
    temp = []
    #end of brand filtering

    titles = []
    prices = []
    thumbnails = []
    short_descriptions = []
    avg_reviews = []
    for product in filtered_products:
        titles.append(product.title)
        prices.append(product.price)
        thumbnails.append(product.thumbnail.url)
        short_descriptions.append(product.short_description)
        avg_reviews.append(product.avg_review)
    response = JsonResponse({'titles':titles,'prices':prices,'thumbnails':thumbnails,'short_descriptions':short_descriptions,'avg_reviews':avg_reviews})
    return response
