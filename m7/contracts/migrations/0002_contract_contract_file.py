# Generated by Django 4.1.7 on 2023-03-24 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contracts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contract',
            name='contract_file',
            field=models.FileField(blank=True, null=True, upload_to='cotratos/%Y/%m/%d/'),
        ),
    ]
