# Generated by Django 2.2.7 on 2020-01-04 03:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('noteapp', '0002_auto_20200103_2231'),
    ]

    operations = [
        migrations.AddField(
            model_name='lnote',
            name='image',
            field=models.ImageField(null=True, upload_to='images'),
        ),
        migrations.DeleteModel(
            name='MyPhoto',
        ),
    ]