# Generated by Django 2.1.5 on 2019-04-24 19:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0021_auto_20190424_1514'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofileinfo',
            old_name='First_Choice_Dorm',
            new_name='Dorm_Choice_One',
        ),
        migrations.RenameField(
            model_name='userprofileinfo',
            old_name='Second_Choice_Dorm',
            new_name='Dorm_Choice_Second',
        ),
        migrations.RenameField(
            model_name='userprofileinfo',
            old_name='Third_Choice_Dorm',
            new_name='Dorm_Choice_Third',
        ),
    ]
