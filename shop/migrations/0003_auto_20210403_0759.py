# Generated by Django 3.1.6 on 2021-04-03 03:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_auto_20210403_0737'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='category',
            field=models.CharField(choices=[('S', 'Shirt'), ('SW', 'Sport wear'), ('OW', 'Outwear'), ('CPU', 'CPU')], max_length=3),
        ),
    ]
