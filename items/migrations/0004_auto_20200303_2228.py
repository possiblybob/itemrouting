# Generated by Django 2.2.10 on 2020-03-04 04:28

from django.db import migrations, models
import items.models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0003_auto_20200303_2224'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='id',
            field=models.UUIDField(default=uuid.UUID('90176cc3-0f9e-4795-bc31-9bf9c3eefb87'), editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='id',
            field=models.UUIDField(default=uuid.UUID('9a594522-b93e-4dc3-8abd-4fa1cf5f16bc'), editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='location',
            field=models.CharField(choices=[('originator_bank', 'Origination Bank'), ('routable', 'Routable'), ('destination_bank', 'Destination Bank')], default='origination_bank', max_length=20),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='status',
            field=models.CharField(choices=[('processing', 'Processing'), ('completed', 'Completed'), ('error', 'Error')], default='processing', max_length=20),
        ),
    ]
