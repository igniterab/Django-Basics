# Generated by Django 3.0.5 on 2020-04-27 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='mimg',
            field=models.ImageField(default='', upload_to='images/'),
            preserve_default=False,
        ),
    ]
