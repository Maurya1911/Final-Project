# Generated by Django 2.0.3 on 2018-08-16 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gotrees', '0009_auto_20180816_1226'),
    ]

    operations = [
        migrations.AddField(
            model_name='trees',
            name='kind',
            field=models.CharField(max_length=3, null=True),
        ),
    ]
