# Generated by Django 2.2.7 on 2020-01-04 02:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LNote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('desc', models.CharField(max_length=1000)),
                ('language', models.CharField(max_length=7)),
                ('created_on', models.DateField()),
                ('is_draft', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='MyPhoto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(max_length=254, upload_to='photos')),
                ('lnote', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.LNote')),
            ],
        ),
    ]
