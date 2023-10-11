# Generated by Django 4.2.6 on 2023-10-11 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='название курса')),
                ('image', models.ImageField(blank=True, null=True, upload_to='univer/', verbose_name='Фото')),
                ('description', models.TextField(verbose_name='описание курса')),
            ],
            options={
                'verbose_name': 'Курс',
                'verbose_name_plural': 'Курсы',
            },
        ),
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='название курса')),
                ('description', models.TextField(verbose_name='описание курса')),
                ('image', models.ImageField(blank=True, null=True, upload_to='lesson/', verbose_name='Фото')),
                ('link', models.TextField(verbose_name='ссылка')),
            ],
            options={
                'verbose_name': 'Урок',
                'verbose_name_plural': 'Уроки',
            },
        ),
    ]
