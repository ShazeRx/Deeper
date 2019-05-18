from django.db import models
from django.db.models.signals import post_delete
from django.dispatch import receiver
from django.utils import timezone

# Create your models here.
class Movie(models.Model):
    name= models.CharField(max_length=128)
    description=models.TextField(default="",null=True,blank=True)
    year= models.IntegerField(null=True,blank=True)
    released=models.IntegerField(null=True,blank=True)
    rating=models.DecimalField(null=True,blank=True,max_digits=2,decimal_places=1)
    photo=models.ImageField(null=True,blank=True, upload_to='plakaty')
    def __str__(self):
        return self.name_with_year()

    def name_with_year(self):
        return str(self.name) + " (" + str(self.year) + ")"

    @property
    def photo_url(self):
        if self.photo and hasattr(self.photo, 'url'):
            return self.photo.url

    def get_picture(self):
        if self.photo:
            return self.photo.url
        else:
            return 'your_default_img_url_path'
@receiver(post_delete, sender=Movie)
def photo_post_delete_handler(sender, **kwargs):
    listingImage = kwargs['instance']
    storage, path = listingImage.photo.storage, listingImage.photo.path
    storage.delete(path)
class Comment(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE,related_name='comments',blank=True,null=True)
    content = models.TextField()
    timestamp = models.DateTimeField(default=timezone.now)
    user=models.CharField(max_length=250)
    approved=models.BooleanField(default=False)


    def __str__(self):
        return self.user
