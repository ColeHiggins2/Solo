# Generated by Django 2.1.5 on 2019-04-24 19:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0028_auto_20190424_1551'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofileinfo',
            name='cleanliness',
            field=models.IntegerField(choices=[('UU', 'Unspecified'), ('1', 'One (lowest)'), ('2', 'Two'), ('3', 'Three'), ('4', 'Four'), ('5', 'Five (highest)')], default='UU', max_length=2),
        ),
    ]
