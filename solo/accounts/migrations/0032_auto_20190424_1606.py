# Generated by Django 2.1.5 on 2019-04-24 20:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0031_auto_20190424_1604'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofileinfo',
            name='cleanliness',
            field=models.CharField(choices=[('UU', 'Unspecified'), ('1', 'One (lowest)'), ('2', 'Two'), ('3', 'Three'), ('4', 'Four'), ('5', 'Five (highest)')], default='UU', max_length=2),
        ),
    ]
