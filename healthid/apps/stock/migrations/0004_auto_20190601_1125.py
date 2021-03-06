# Generated by Django 2.1.7 on 2019-06-01 10:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import healthid.utils.app_utils.id_generator


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('outlets', '0005_auto_20190523_1327'),
        ('products', '0014_auto_20190530_0124'),
        ('stock', '0003_auto_20190523_1327'),
    ]

    operations = [
        migrations.CreateModel(
            name='StockTransfer',
            fields=[
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('id', models.CharField(default=healthid.utils.app_utils.id_generator.id_gen, editable=False, max_length=9, primary_key=True, serialize=False)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('complete_status', models.BooleanField(default=False)),
                ('batch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='stock_transfer_batch', to='products.BatchInfo')),
                ('deleted_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('destination_outlet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='destination_outlet', to='outlets.Outlet')),
                ('sending_outlet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sending_outlet', to='outlets.Outlet')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='StockTransferRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('quantity', models.IntegerField()),
                ('deleted_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='stock_transfer_product', to='products.Product')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='stocktransfer',
            name='stock_transfer_record',
            field=models.ManyToManyField(related_name='stock_transfer_record', to='stock.StockTransferRecord'),
        ),
    ]
