# Generated by Django 4.1.1 on 2022-09-28 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mywatchlist', '0002_alter_mywatchedlist_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mywatchedlist',
            name='watched',
            field=models.CharField(max_length=300),
        ),
    ]
