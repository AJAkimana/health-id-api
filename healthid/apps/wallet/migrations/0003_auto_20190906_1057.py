# Generated by Django 2.2 on 2019-09-06 09:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wallet', '0002_storecreditwallethistory'),
    ]

    operations = [
        migrations.RenameField(
            model_name='storecreditwallethistory',
            old_name='customer',
            new_name='customer_account',
        ),
    ]
