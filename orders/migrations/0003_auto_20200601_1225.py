# Generated by Django 2.1.5 on 2020-06-01 19:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_auto_20200601_1147'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='notpizza',
            name='sub_mod',
        ),
        migrations.RemoveField(
            model_name='pizza',
            name='toppings',
        ),
        migrations.AddField(
            model_name='submodifications',
            name='sub',
            field=models.ManyToManyField(blank=True, related_name='mod', to='orders.NotPizza'),
        ),
        migrations.AddField(
            model_name='toppings',
            name='pizza',
            field=models.ManyToManyField(blank=True, related_name='toppings', to='orders.Pizza'),
        ),
    ]
