from re import T
from django.db import models
from django.contrib.auth.models import User
from tinymce import models as tinymce_models
from ckeditor.fields import RichTextField

# Create your models here.
class Post(models.Model):
    sno = models.AutoField(primary_key=True)
    author = models.CharField(max_length=225)
    title = models.CharField(max_length=130)
    content = RichTextField(blank=True, null = True)
    views = models.IntegerField(default=0)
    slug = models.SlugField(max_length=250)
    Timestamp = models.DateField(blank=True)

    def __str__(self):
        return 'Author By ' + self.author


class Icodercomment(models.Model):
    sno = models.AutoField(primary_key=True)
    comment = models.TextField()
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    parent = models.ForeignKey('self',on_delete=models.CASCADE,null=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.comment[0:13] + '..' + " by "+  self.user.username