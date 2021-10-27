from django.db import models
from datetime import datetime
from django.contrib.postgres.fields import ArrayField
from django import forms
from captcha.fields import ReCaptchaField
from django.contrib.auth.models import User

# Create your models here.
class FormWithCaptcha(forms.Form):
    captcha = ReCaptchaField()

class ReviewableProduct(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.FloatField()
    thumbnail = models.ImageField(upload_to='')
    short_description = models.CharField(max_length=400)
    avg_review = models.FloatField()
    product_number = models.CharField(max_length=100, default='unorderable')
    featured = models.BooleanField(default=False)
    imp_id = models.IntegerField(default=100000)
    category = models.CharField(max_length=100, default="frame")
    brand = models.CharField(max_length=100, default="Skystric Exclusive")

    def __str__(self):
        return self.title

class ProductReview(models.Model):
    published_user = models.CharField(max_length=150, default="anonymous")
    date_published = models.DateTimeField("date published", default=datetime.now())
    review_title = models.CharField(max_length=200)
    stars = models.IntegerField()
    review_description = models.TextField()
    purchased = models.BooleanField()
    reviewableproduct = models.ForeignKey(ReviewableProduct, on_delete=models.CASCADE)
    class Meta:
        verbose_name_plural = "ProductReviews"

    def __str__(self):
        return self.review_title

class ProductQuestion(models.Model):
    published_user = models.CharField(max_length=150, default="anonymous")
    question_text = models.CharField(max_length=600, default="question")
    applied_product = models.ForeignKey(ReviewableProduct, on_delete=models.CASCADE)

    def __str__(self):
        return self.question_text

class ProductAnswer(models.Model):
    published_user = models.CharField(max_length=150, default="anonymous")
    answer_text = models.CharField(max_length=600, default="answer")
    applied_question = models.ForeignKey(ProductQuestion, on_delete=models.CASCADE)
    def __str__(self):
        return self.answer_text

class Profile(models.Model):
    username = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    cart = models.ManyToManyField('CartProduct', blank=True)
    def __str__(self):
        return self.username.username

class Order(models.Model):
    orders = models.ManyToManyField('CartProduct', blank=True)
    totalprice = models.FloatField(null = True)

class CartProduct(models.Model):
    product = models.ForeignKey(ReviewableProduct, on_delete=models.CASCADE, null=True)
    number = models.IntegerField(null=True)
    total = models.FloatField(null = True)

class ContactModel(models.Model):
    user_profile = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True)
    email = models.EmailField()
    review_description = models.CharField(max_length=100)
    review_content = models.TextField()

class FrontPageImages(models.Model):
    thumbnail = models.ImageField(upload_to='')
    title_text = models.CharField(max_length=300)
    desc_text = models.TextField()
    link = models.CharField(max_length=100)
    active = models.BooleanField(default=False)
    def __str__(self):
        return self.title_text

class ImageModel(models.Model):
    tag = models.CharField(max_length=100)
    image = models.ImageField(upload_to='')
    def __str__(self):
        return self.tag
