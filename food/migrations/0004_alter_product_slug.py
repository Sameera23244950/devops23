# Generated by Django 5.0.3 on 2024-03-31 05:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0003_product_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='slug',
            field=models.SlugField(max_length=250, unique=True),
        ),
    ]
