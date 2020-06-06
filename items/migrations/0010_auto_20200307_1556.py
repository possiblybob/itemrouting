# Generated by Django 2.2.10 on 2020-03-07 21:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0009_auto_20200306_2238'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='has_errored',
            field=models.BooleanField(default=False, help_text='Whether or not processing of this Item has ever errored'),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='status',
            field=models.CharField(choices=[('processing', 'Processing'), ('completed', 'Completed'), ('error', 'Error'), ('refunding', 'Refunding'), ('refunded', 'Refunded'), ('fixing', 'Fixing')], default='processing', max_length=20),
        ),
    ]