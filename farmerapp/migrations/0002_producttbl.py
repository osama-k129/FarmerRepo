# Generated by Django 3.1.4 on 2021-04-23 07:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('farmerapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductTbl',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(blank=True, max_length=200, null=True)),
                ('product_quantity', models.CharField(blank=True, max_length=200, null=True)),
                ('product_price', models.CharField(blank=True, max_length=200, null=True)),
                ('product_about', models.CharField(blank=True, max_length=200, null=True)),
                ('product_photo', models.FileField(upload_to='product_images')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
