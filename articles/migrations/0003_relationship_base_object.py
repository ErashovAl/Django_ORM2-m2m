# Generated by Django 4.0.6 on 2022-07-20 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_object_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='relationship',
            name='base_object',
            field=models.BooleanField(default=True, verbose_name='Основной раздел'),
            preserve_default=False,
        ),
    ]