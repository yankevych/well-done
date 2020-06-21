from django.db import models


class Blog(models.Model):
    blog_title = models.CharField('blog title', max_length=200)
    blog_text = models.TextField('blog text')
    blog_pub_date = models.DateTimeField('public date')
    blog_image = models.ImageField('blog image', upload_to='../media/blog/')

    def __str__(self):
        return self.blog_title


