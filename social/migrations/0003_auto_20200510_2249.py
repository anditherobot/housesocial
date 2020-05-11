# Generated by Django 3.0.5 on 2020-05-11 02:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('social', '0002_auto_20200510_2209'),
    ]

    operations = [
        migrations.AlterField(
            model_name='houseuserprofile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='houseuserprofile', to=settings.AUTH_USER_MODEL),
        ),
    ]
