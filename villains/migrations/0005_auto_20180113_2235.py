# Generated by Django 2.1.dev20171005184450 on 2018-01-13 13:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('villains', '0004_auto_20180110_1703'),
    ]

    operations = [
        migrations.AlterField(
            model_name='villain',
            name='writter_id',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
