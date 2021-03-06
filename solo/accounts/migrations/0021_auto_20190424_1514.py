# Generated by Django 2.1.5 on 2019-04-24 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0020_auto_20190424_1510'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofileinfo',
            name='dorm1',
        ),
        migrations.RemoveField(
            model_name='userprofileinfo',
            name='dorm2',
        ),
        migrations.RemoveField(
            model_name='userprofileinfo',
            name='dorm3',
        ),
        migrations.AddField(
            model_name='userprofileinfo',
            name='First_Choice_Dorm',
            field=models.CharField(choices=[('UU', 'Unspecified'), ('BE', 'Belk Hall'), ('EL', 'Elm Hall'), ('GR', 'Greek Village'), ('HA', 'Hawthorn Hall'), ('HO', 'Holshouser Hall'), ('HU', 'Hunt Hall'), ('LA', 'Laurel Hall'), ('LE', 'Levine Hall'), ('LY', 'Lynch Hall'), ('MA', 'Martin Hall'), ('WI', 'Witherspoon Hall'), ('MI', 'Miltimore Hall'), ('OA', 'Oak Hall'), ('PI', 'Pine Hall'), ('SC', 'Scott Hall'), ('WA', 'Wallis Hall'), ('SA', 'Sanford Hall')], default='UU', max_length=3),
        ),
        migrations.AddField(
            model_name='userprofileinfo',
            name='Second_Choice_Dorm',
            field=models.CharField(choices=[('UU', 'Unspecified'), ('BE', 'Belk Hall'), ('EL', 'Elm Hall'), ('GR', 'Greek Village'), ('HA', 'Hawthorn Hall'), ('HO', 'Holshouser Hall'), ('HU', 'Hunt Hall'), ('LA', 'Laurel Hall'), ('LE', 'Levine Hall'), ('LY', 'Lynch Hall'), ('MA', 'Martin Hall'), ('WI', 'Witherspoon Hall'), ('MI', 'Miltimore Hall'), ('OA', 'Oak Hall'), ('PI', 'Pine Hall'), ('SC', 'Scott Hall'), ('WA', 'Wallis Hall'), ('SA', 'Sanford Hall')], default='UU', max_length=3),
        ),
        migrations.AddField(
            model_name='userprofileinfo',
            name='Third_Choice_Dorm',
            field=models.CharField(choices=[('UU', 'Unspecified'), ('BE', 'Belk Hall'), ('EL', 'Elm Hall'), ('GR', 'Greek Village'), ('HA', 'Hawthorn Hall'), ('HO', 'Holshouser Hall'), ('HU', 'Hunt Hall'), ('LA', 'Laurel Hall'), ('LE', 'Levine Hall'), ('LY', 'Lynch Hall'), ('MA', 'Martin Hall'), ('WI', 'Witherspoon Hall'), ('MI', 'Miltimore Hall'), ('OA', 'Oak Hall'), ('PI', 'Pine Hall'), ('SC', 'Scott Hall'), ('WA', 'Wallis Hall'), ('SA', 'Sanford Hall')], default='UU', max_length=3),
        ),
    ]
