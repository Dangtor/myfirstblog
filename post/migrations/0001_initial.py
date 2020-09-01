# Generated by Django 3.1 on 2020-08-30 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120, verbose_name='Basliq')),
                ('content', models.TextField(verbose_name='Mesaj')),
                ('publishing_date', models.DateTimeField(auto_now_add=True, verbose_name='Tarix')),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('slug', models.SlugField(unique=True)),
            ],
            options={
                'ordering': ['-publishing_date'],
            },
        ),
    ]