# Generated by Django 3.2.7 on 2021-09-30 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('textBE', '0005_alter_jsondoc_json'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='jsondoc',
            name='json',
        ),
        migrations.AddField(
            model_name='jsondoc',
            name='text',
            field=models.TextField(default=''),
        ),
    ]
