# Generated by Django 3.1.4 on 2021-04-23 09:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('farmerapp', '0004_auto_20210423_1341'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product_catagory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('catagory_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='producttbl',
            name='select_catagory',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='farmerapp.product_catagory'),
            preserve_default=False,
        ),
    ]
