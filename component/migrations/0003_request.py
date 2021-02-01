# Generated by Django 3.0.3 on 2021-01-27 08:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('component', '0002_auto_20210126_1158'),
    ]

    operations = [
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.IntegerField(choices=[(0, 'Pending'), (1, 'Accepted'), (2, 'Rejected')], default=0)),
                ('request_num', models.IntegerField(default=0)),
                ('component', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='component.Component')),
                ('request_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]