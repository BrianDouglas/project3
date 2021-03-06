# Generated by Django 2.1.5 on 2020-06-01 22:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0007_auto_20200601_1510'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='submodifications',
            name='sub',
        ),
        migrations.AddField(
            model_name='notpizza',
            name='sandwich_mod',
            field=models.ManyToManyField(blank=True, related_name='sub', to='orders.SubModifications'),
        ),
        migrations.AlterField(
            model_name='pizzabase',
            name='size',
            field=models.CharField(choices=[('SM', 'Small'), ('LG', 'Large')], max_length=2),
        ),
        migrations.AlterField(
            model_name='pizzabase',
            name='style',
            field=models.CharField(choices=[('SIC', 'Sicilian'), ('REG', 'Regular')], max_length=3),
        ),
        migrations.AlterField(
            model_name='pizzabase',
            name='toppings_num',
            field=models.IntegerField(choices=[(0, 'Cheese'), (1, 'One'), (2, 'Two'), (3, 'Three'), (4, 'Special')]),
        ),
    ]
