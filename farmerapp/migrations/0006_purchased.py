# Generated by Django 3.1.4 on 2021-04-23 14:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('farmerapp', '0005_auto_20210423_1442'),
    ]

    operations = [
        migrations.CreateModel(
            name='Purchased',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('accept', models.BooleanField(blank=True, null=True)),
                ('buyer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('select_product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='farmerapp.producttbl')),
            ],
        ),
    ]
