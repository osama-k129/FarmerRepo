# Generated by Django 3.2.5 on 2022-02-01 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bidding', '0002_biddingproduct_complete'),
    ]

    operations = [
        migrations.AddField(
            model_name='biddingproduct',
            name='min_price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
    ]
