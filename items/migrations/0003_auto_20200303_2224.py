# Generated by Django 2.2.10 on 2020-03-04 04:24

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0002_auto_20200303_2215'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='id',
            field=models.UUIDField(default=uuid.UUID('a3b99163-acd3-43cd-b44f-0f5574993c8f'), editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='id',
            field=models.UUIDField(default=uuid.UUID('ed9fda40-ab8d-49ce-b0e5-3c51ea442ece'), editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='location',
            field=models.CharField(blank=True, choices=[('originator_bank', 'Origination Bank'), ('routable', 'Routable'), ('destination_bank', 'Destination Bank')], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='status',
            field=models.CharField(blank=True, choices=[('processing', 'Processing'), ('completed', 'Completed'), ('error', 'Error')], max_length=20, null=True),
        ),
    ]
