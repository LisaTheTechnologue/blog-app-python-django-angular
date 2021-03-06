# Generated by Django 2.2.7 on 2019-12-01 21:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_abrev', models.CharField(max_length=50)),
                ('category_desc', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Vtype',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vtype_abrev', models.CharField(max_length=5)),
                ('vtype_desc', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Vocab',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('french', models.CharField(max_length=100, verbose_name='French')),
                ('pronunciation', models.CharField(max_length=100, verbose_name='Pronunciation')),
                ('english', models.CharField(max_length=255, verbose_name='English')),
                ('example', models.CharField(max_length=255, verbose_name='Example')),
                ('note', models.CharField(max_length=255, verbose_name='Note')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vocab.Category')),
                ('vtype', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vocab.Vtype')),
            ],
            options={
                'ordering': ['french'],
            },
        ),
    ]
