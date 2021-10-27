from django.contrib import admin
from .models import FrontPageImages, ImageModel, ProductReview, ContactModel, CartProduct, ReviewableProduct, ProductQuestion, ProductAnswer, Profile
# Register your models here.
class MainAdmin(admin.ModelAdmin):

    fieldsets = [
        ("ShortDisplay", {'fields': ["title", "short_description", "featured", "price", "thumbnail", "avg_review",]}),
        ("LongDisplayExtension", {'fields': ["description",]}),
        ("Searchibility",{'fields':["brand","category"]}),
        #("ReviewShortDisplay", {"fields": ["review_title", "published_user", "date_published", "purchased", "stars"]}),
        #("ReviewLongDisplayExtension", {'fields': ["review_description", "users_up", "users_down"]}),
    ]

    formfield_overrides = {
        #Possibly Replace Text Box?
        }

admin.site.register(ProductQuestion)
admin.site.register(ProductAnswer)
admin.site.register(ProductReview)
admin.site.register(Profile)
admin.site.register(CartProduct)
admin.site.register(ContactModel)
admin.site.register(ReviewableProduct, MainAdmin)
