# Generated by Django 2.2.7 on 2020-01-04 03:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('noteapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lnote',
            name='image',
        ),
        migrations.AddField(
            model_name='myphoto',
            name='lnote',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='noteapp.LNote'),
            preserve_default=False,
        ),
    ]
