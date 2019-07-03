# Generated by Django 2.1.7 on 2019-06-25 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0017_auto_20190618_1441'),
    ]

    operations = [
        migrations.AddField(
            model_name='productcategory',
            name='is_vat_applicable',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='productcategory',
            name='markup',
            field=models.PositiveIntegerField(default=25),
        ),
        migrations.AlterField(
            model_name='product',
            name='markup',
            field=models.PositiveIntegerField(default=25),
        ),
        migrations.AlterField(
            model_name='product',
            name='sku_number',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='unit_cost',
            field=models.DecimalField(decimal_places=2, max_digits=12, null=True),
        ),
    ]
