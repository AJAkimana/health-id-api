# Generated by Django 2.1.7 on 2019-07-08 09:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0002_auto_20190523_1327'),
    ]

    operations = [
        migrations.AlterField(
            model_name='register',
            name='outlet',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='outlet_register', to='outlets.Outlet'),
        ),
    ]
