# Generated by Django 4.1.1 on 2022-10-16 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_company_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='address',
            field=models.TextField(help_text='В google maps найти вашу компанию и вставить src ссылку'),
        ),
    ]
