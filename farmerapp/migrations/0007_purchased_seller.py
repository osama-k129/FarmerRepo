# Generated by Django 3.1.4 on 2021-04-23 16:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('farmerapp', '0006_purchased'),
    ]

    operations = [
        migrations.AddField(
            model_name='purchased',
            name='seller',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='farmerapp.user_profile'),
            preserve_default=False,
        ),
    ]
