# Generated by Django 3.2.3 on 2021-07-12 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app17', '0002_studentregistationmodel_dob'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentregistationmodel',
            name='email',
            field=models.EmailField(default=2, max_length=254),
            preserve_default=False,
        ),
    ]
