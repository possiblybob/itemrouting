# Generated by Django 2.2.10 on 2020-03-04 04:38

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0004_auto_20200303_2228'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]
