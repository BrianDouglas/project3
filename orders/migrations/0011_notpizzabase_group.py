# Generated by Django 2.1.5 on 2020-06-02 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0010_auto_20200602_1008'),
    ]

    operations = [
        migrations.AddField(
            model_name='notpizzabase',
            name='group',
            field=models.CharField(choices=[('SUB', 'Sub Sandwich'), ('PST', 'Pasta'), ('SLD', 'Salad'), ('DPL', 'Dinner Platter')], default='NA', max_length=3),
            preserve_default=False,
        ),
    ]