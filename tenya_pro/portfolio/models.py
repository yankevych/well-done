from django.db import models


class Portfolio(models.Model):
    port_title = models.CharField('port title', max_length=200)
    port_text = models.TextField('port text')
    port_pub_date = models.DateTimeField('public date')
    port_image = models.ImageField('port image', upload_to='../media/')

    def __str__(self):
        return self.port_text


class PostsImages(models.Model):
    port_images = models.ImageField(upload_to='../media/', blank=True)
    post = models.ForeignKey(Portfolio, related_name='PostsImages', on_delete=models.CASCADE)
