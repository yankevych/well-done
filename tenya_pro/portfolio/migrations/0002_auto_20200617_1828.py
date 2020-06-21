# Generated by Django 3.0.6 on 2020-06-17 15:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portfolio',
            name='port_image',
            field=models.ImageField(upload_to='../media/', verbose_name='port image'),
        ),
        migrations.CreateModel(
            name='PostsImages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('port_images', models.ImageField(blank=True, upload_to='../media/')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='PostsImages', to='portfolio.Portfolio')),
            ],
        ),
    ]