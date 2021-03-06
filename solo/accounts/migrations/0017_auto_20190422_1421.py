# Generated by Django 2.1.5 on 2019-04-22 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0016_auto_20190422_1417'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofileinfo',
            name='age',
            field=models.IntegerField(default=0, max_length=2),
        ),
        migrations.AlterField(
            model_name='userprofileinfo',
            name='bed',
            field=models.CharField(choices=[('U', 'Unspecified'), ('E', 'Early Riser'), ('L', 'Late Riser')], default='U', max_length=1),
        ),
        migrations.AlterField(
            model_name='userprofileinfo',
            name='class_year',
            field=models.CharField(choices=[('FR', 'Freshman'), ('SO', 'Sophomore'), ('JR', 'Junior'), ('SR', 'Senior'), ('UU', 'Unspecified')], default='UU', max_length=2),
        ),
        migrations.AlterField(
            model_name='userprofileinfo',
            name='dorm',
            field=models.CharField(choices=[('UU', 'Unspecified'), ('BE', 'Belk Hall'), ('EL', 'Elm Hall'), ('GR', 'Greek Village'), ('HA', 'Hawthorn Hall'), ('HO', 'Holshouser Hall'), ('HU', 'Hunt Hall'), ('LA', 'Laurel Hall'), ('LE', 'Levine Hall'), ('LY', 'Lynch Hall'), ('MA', 'Martin Hall'), ('WI', 'Witherspoon Hall'), ('MI', 'Miltimore Hall'), ('OA', 'Oak Hall'), ('PI', 'Pine Hall'), ('SC', 'Scott Hall'), ('WA', 'Wallis Hall'), ('SA', 'Sanford Hall')], default='UU', max_length=2),
        ),
        migrations.AlterField(
            model_name='userprofileinfo',
            name='smoking',
            field=models.CharField(choices=[('Y', 'Smoking'), ('N', 'No Smoking')], default='U', max_length=1),
        ),
    ]
