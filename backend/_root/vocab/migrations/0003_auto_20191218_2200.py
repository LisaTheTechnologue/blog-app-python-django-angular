# Generated by Django 2.2.7 on 2019-12-19 03:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vocab', '0002_auto_20191207_2305'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vocab',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vocabs', to='vocab.Category'),
        ),
        migrations.AlterField(
            model_name='vocab',
            name='vtype',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vocabs', to='vocab.Vtype'),
        ),
    ]