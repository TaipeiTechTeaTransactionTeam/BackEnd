# Generated by Django 2.1.3 on 2018-11-29 15:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('storeApp', '0002_auto_20181129_2254'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='shoppingcart',
            options={},
        ),
        migrations.AlterModelManagers(
            name='shoppingcart',
            managers=[
            ],
        ),
        migrations.RemoveField(
            model_name='shoppingcart',
            name='user_ptr',
        ),
    ]