# Generated by Django 3.2.5 on 2022-02-08 15:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('bidding', '0004_bidded_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bidded_price',
            name='bid_price',
            field=models.IntegerField(),
        ),
        migrations.CreateModel(
            name='Bid_sold',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sold_date_time', models.DateTimeField(auto_now_add=True)),
                ('bid_product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bidding.bidded_price')),
                ('sold_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
