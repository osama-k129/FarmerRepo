# Generated by Django 3.2.5 on 2022-02-08 15:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('bidding', '0003_biddingproduct_min_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bidded_price',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bid_price', models.IntegerField(max_length=10)),
                ('bid_date_time', models.DateTimeField(auto_now_add=True)),
                ('bid_product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bidding.biddingproduct')),
                ('bidded_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
