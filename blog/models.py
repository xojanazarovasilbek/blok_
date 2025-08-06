from django.db import models

# Create your models here.



class Category(models.Model):
    name = models.CharField(verbose_name="Category_name", max_length=230)
    slug = models.SlugField(max_length=250, unique=True)
   
    def __str__(self):
        return str(self.name)
    
class Tag(models.Model):
    name = models.CharField(verbose_name="Category_name", max_length=230)
    slug = models.SlugField(max_length=250, unique=True)
   
    def __str__(self):
        return str(self.name)
    


class Post(models.Model):
    title = models.CharField(verbose_name="Post_title", max_length=250)
    body = models.TextField(verbose_name="Post title")
    author = models.CharField(verbose_name="author_name", default="admin", max_length=100)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='categories')
    tag = models.ManyToManyField(Tag)
    views = models.PositiveIntegerField(default=0)
    publish_date = models.DateTimeField(verbose_name="Publish_date",auto_now_add=True) 
    published = models.BooleanField(default=True)
    on_top = models.BooleanField(default=False)

    
    def __str__(self):
        return str(self.title)
    
class Comment(models.Model):
    author = models.CharField(verbose_name="comment author", max_length=100, blank=False)
    comment = models.TextField(verbose_name="Comment")
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')

    def __str__(self):
        return str(self.author)
    
class Rating(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='ratings')
    value = models.PositiveSmallIntegerField(verbose_name="Post riting",default=0)

    def __str__(self):
        return str(self.value)


    

