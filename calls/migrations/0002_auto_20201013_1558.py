# Generated by Django 3.0.10 on 2020-10-13 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calls', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='farm',
            name='owned_cats',
            field=models.CharField(default='no catto', max_length=100),
        ),
        migrations.AlterField(
            model_name='farm',
            name='buy_price',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='farm',
            name='capacity',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='farm',
            name='name',
            field=models.CharField(max_length=25),
        ),
    ]
