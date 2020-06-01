# Generated by Django 2.1.5 on 2020-06-01 22:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0005_auto_20200601_1424'),
    ]

    operations = [
        migrations.CreateModel(
            name='PizzaOrder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.AlterField(
            model_name='order',
            name='pizza',
            field=models.ManyToManyField(blank=True, related_name='order', to='orders.PizzaOrder'),
        ),
        migrations.AlterField(
            model_name='toppings',
            name='pizza',
            field=models.ManyToManyField(blank=True, related_name='toppings', to='orders.PizzaOrder'),
        ),
        migrations.RenameModel(
            old_name='Pizza',
            new_name='PizzaBase',
        ),
        migrations.AddField(
            model_name='pizzaorder',
            name='base',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='base', to='orders.PizzaBase'),
        ),
    ]
