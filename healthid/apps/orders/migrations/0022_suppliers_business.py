# Generated by Django 2.2 on 2019-11-26 15:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('business', '0004_auto_20190711_1004'),
        ('orders', '0021_auto_20191121_2143'),
    ]

    operations = [
        migrations.AddField(
            model_name='suppliers',
            name='business',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='supplier_business', to='business.Business'),
        ),
    ]