from django.db import models

# Create your models here.



   # def __str__(self):
    #    return self.date


#new db

class User(models.Model):
    user_id=models.CharField(max_length=254)
    user_name=models.CharField(max_length=254)
    user_email=models.EmailField(max_length=254)
    user_location=models.TextField(max_length=254)
    user_mob_no=models.CharField(max_length=10)


class Restaurants(models.Model):
    res_id=models.CharField(max_length=254)
    res_name=models.CharField(max_length=254)
    res_location=models.TextField(max_length=254)

class Visits(models.Model):
    user_id=models.CharField(max_length=254)
    res_id=models.CharField(max_length=254)
    review=models.TextField(max_length=254)

class Orders(models.Model):
    order_id=models.CharField(max_length=254)
    user_id=models.CharField(max_length=254)
    res_id=models.CharField(max_length=254)
    food_item=models.CharField(max_length=254)
    price=models.FloatField()

class Res_Click(models.Model):
    user_id=models.CharField(max_length=254)
    res_id=models.CharField(max_length=254)

class Posts(models.Model):
    post_id=models.CharField(max_length=254)
    user_id=models.CharField(max_length=254)
    content=models.TextField(max_length=254)
    likes=models.IntegerField()
    #image=models.ImageField()
    #gitcimage=models.ImageField()

class FacebookStatus(models.Model):

    class Meta:
        verbose_name_plural = 'Facebook Statuses'
        ordering = ['publish_timestamp']

    STATUS = (
        ('draft', 'Draft'),
        ('approved', 'Approved'),
    )
    status = models.CharField(max_length=255, 
        choices=STATUS, default=STATUS[0][0])
    publish_timestamp = models.DateTimeField(null=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField(max_length=255)
    link = models.URLField(null=True, blank=True)

    def __unicode__(self):
        return self.message
