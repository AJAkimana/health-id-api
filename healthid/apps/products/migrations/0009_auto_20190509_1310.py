# Generated by Django 2.1.7 on 2019-05-09 12:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import healthid.utils.app_utils.id_generator


class Migration(migrations.Migration):

    dependencies = [
        ('outlets', '0004_outlet_preference'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('products', '0008_auto_20190507_1459'),
    ]

    operations = [
        migrations.CreateModel(
            name='Quantity',
            fields=[
                ('id', models.CharField(default=healthid.utils.app_utils.id_generator.id_gen, editable=False, max_length=9, primary_key=True, serialize=False)),
                ('quantity_received', models.PositiveIntegerField(blank=True, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='batchinfo',
            name='quantity_received',
        ),
        migrations.AddField(
            model_name='product',
            name='outlet',
            field=models.ManyToManyField(to='outlets.Outlet'),
        ),
        migrations.AddField(
            model_name='product',
            name='user',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='batchinfo',
            name='outlet',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='outlet_batches', to='outlets.Outlet'),
        ),
        migrations.AlterField(
            model_name='batchinfo',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_batches', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='quantity',
            name='batch',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='batch_quantities', to='products.BatchInfo'),
        ),
        migrations.AddField(
            model_name='quantity',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='proposedQuantityChange', to='products.Quantity'),
        ),
        migrations.AddField(
            model_name='quantity',
            name='product',
            field=models.ManyToManyField(related_name='product_quantities', to='products.Product'),
        ),
        migrations.AddField(
            model_name='quantity',
            name='proposed_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='proposing_user', to=settings.AUTH_USER_MODEL),
        ),
    ]
