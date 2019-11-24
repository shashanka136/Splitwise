# Generated by Django 2.2.7 on 2019-11-24 15:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('sgroups', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='activity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exp', models.BooleanField(default=False)),
                ('expense', models.FloatField(default=0.0)),
                ('friend1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fri1', to=settings.AUTH_USER_MODEL)),
                ('friend2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fri2', to=settings.AUTH_USER_MODEL)),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='grp', to='sgroups.Groups')),
            ],
        ),
    ]
