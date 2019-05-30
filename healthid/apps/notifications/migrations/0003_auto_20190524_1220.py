# Generated by Django 2.1.7 on 2019-05-24 11:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('notifications', '0002_notification_event_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='NotificationRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('read_status', models.BooleanField(default=False)),
                ('recipient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_notifications_records', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='notification',
            name='read_status',
        ),
        migrations.RemoveField(
            model_name='notification',
            name='recipient',
        ),
        migrations.AlterField(
            model_name='notification',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AddField(
            model_name='notification',
            name='notification_records',
            field=models.ManyToManyField(related_name='notification', to='notifications.NotificationRecord'),
        ),
    ]