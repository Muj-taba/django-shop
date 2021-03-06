# Generated by Django 3.1.1 on 2020-10-14 07:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20201014_0716'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='discount_price',
            field=models.FloatField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name='item',
            name='category',
            field=models.CharField(choices=[('SW', 'Sport wear'), ('S', 'Shirt'), ('OT', 'Outwear')], max_length=2),
        ),
    ]
