# Generated by Django 3.0.7 on 2020-11-04 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_auto_20201104_1658'),
    ]

    operations = [
        migrations.AddField(
            model_name='results',
            name='result',
            field=models.DecimalField(decimal_places=3, default='0.000', max_digits=6),
        ),
    ]