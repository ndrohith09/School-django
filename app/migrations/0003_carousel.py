# Generated by Django 3.1.1 on 2021-07-19 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20210718_1139'),
    ]

    operations = [
        migrations.CreateModel(
            name='Carousel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('carousel', models.ImageField(upload_to='carousel/')),
            ],
        ),
    ]
