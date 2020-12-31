# Generated by Django 2.0.8 on 2018-12-28 18:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('oddslingers', '0036_user_levels_data_migration'),
    ]

    operations = [
        migrations.AddField(
            model_name='userbalance',
            name='season',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='userstats',
            name='season',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='userbalance',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='userstats',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterUniqueTogether(
            name='userbalance',
            unique_together={('user', 'season')},
        ),
        migrations.AlterUniqueTogether(
            name='userstats',
            unique_together={('user', 'season')},
        ),
    ]