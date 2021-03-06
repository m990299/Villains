# Generated by Django 2.1.dev20171005184450 on 2018-01-24 18:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('villains', '0010_auto_20180125_0312'),
    ]

    operations = [
        migrations.CreateModel(
            name='Agree',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='agreer',
            name='villain',
        ),
        migrations.RenameField(
            model_name='villain',
            old_name='agree',
            new_name='agree_count',
        ),
        migrations.DeleteModel(
            name='Agreer',
        ),
        migrations.AddField(
            model_name='agree',
            name='villain',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='villains.Villain'),
        ),
        migrations.AddField(
            model_name='villain',
            name='agree_user_set',
            field=models.ManyToManyField(blank=True, related_name='agree_user_set', through='villains.Agree', to=settings.AUTH_USER_MODEL),
        ),
    ]
