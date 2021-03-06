# Generated by Django 2.2 on 2019-09-16 11:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('products', '0027_batchinfo_is_returnable'),
        ('stock', '0006_auto_20190715_1245'),
    ]

    operations = [
        migrations.AddField(
            model_name='stockcounttemplate',
            name='batches',
            field=models.ManyToManyField(blank=True, related_name='batches_to_count', to='products.BatchInfo'),
        ),
        migrations.AddField(
            model_name='stockcounttemplate',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='created_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='stockcounttemplate',
            name='end_on',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='stockcounttemplate',
            name='interval',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='stockcounttemplate',
            name='scheduled',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='stockcounttemplate',
            name='unique',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='stockcounttemplate',
            name='outlet',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='outlets.Outlet'),
        ),
        migrations.AddConstraint(
            model_name='stockcounttemplate',
            constraint=models.UniqueConstraint(condition=models.Q(unique=True), fields=('created_at', 'interval', 'end_on', 'created_by'), name='unique_template_user'),
        ),
    ]
