# Generated by Django 2.2.7 on 2020-01-04 03:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vocab', '0005_lnote_myphoto'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='myphoto',
            name='lnote',
        ),
        migrations.DeleteModel(
            name='LNote',
        ),
        migrations.DeleteModel(
            name='MyPhoto',
        ),
    ]
