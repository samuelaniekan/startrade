# Generated by Django 3.2.7 on 2021-10-04 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crypto_app', '0002_auto_20211004_1425'),
    ]

    operations = [
        migrations.AddField(
            model_name='investments',
            name='start_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='investments',
            name='uri',
            field=models.CharField(default='E4F30A7123B4462987E206A8922739', max_length=50),
        ),
        migrations.AlterField(
            model_name='pop',
            name='uri',
            field=models.CharField(default='3D837CD47970435FA4657BB1BFAFF3', max_length=50),
        ),
        migrations.AlterField(
            model_name='transactions',
            name='uri',
            field=models.CharField(default='EC8534FF526B4B6FBBA6FC599423A6', max_length=50),
        ),
    ]
