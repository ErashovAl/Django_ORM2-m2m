# Generated by Django 4.0.6 on 2022-07-22 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0006_alter_tag_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='Картинка'),
        ),
        migrations.AlterField(
            model_name='article',
            name='published_at',
            field=models.DateTimeField(verbose_name='Опубликовано'),
        ),
        migrations.AlterField(
            model_name='article',
            name='text',
            field=models.TextField(verbose_name='Текст статьи'),
        ),
    ]