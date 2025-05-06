from django.db import models

from django.contrib.auth.models import User

from cloudinary.models import CloudinaryField

STATUS = ((0, "Draft"), (1, "Published"))

# Create your models here.


class Post(models.Model):
    """
    Stores a single blog post entry, related to :model: 'auth.User'.
    """
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="blog_posts"
    )
    featured_image = CloudinaryField('image', default='placeholder')

    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)# Automatically set the field to now when the object is first created
    status = models.IntegerField(choices=STATUS, default=0) # https://docs.djangoproject.com/en/4.2/ref/models/fields/#django.db.models.DateField
    excerpt = models.TextField(blank=True)
    updated_on = models.DateTimeField(auto_now=True)# Automatically set the field to now every time the object is saved
    # field_2 = models.IntegerField(default=47)
    # field_3 = models.CharField(null=True)

    class Meta:
        ordering = ["-created_on", "author"]

    def __str__(self):
        return f"{self.title} | written by {self.author}"


class Comment(models.Model):
    """
    Stores a single coment entry related to :model: `auth.User`
    and :model: `blog.Post`
    """
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name="comments")
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="commenter"
    )
    body = models.TextField()
    approved = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)
    # challenge = models.FloatField(default=3.0)

    class Meta():
        ordering = ["created_on"]

    def __str__(self):
        # self.body = "Give me...."
        # return f"Created on: {self.created_on}"
        return f"Comment {self.body} by '{self.author}'"
