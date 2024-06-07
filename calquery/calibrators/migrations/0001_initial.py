# Generated by Django 3.1 on 2024-06-07 15:31

import calibrators.models
from django.db import migrations, models
import djongo.models.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Calibrator',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('iau_name', models.CharField(max_length=255)),
                ('equinox', models.CharField(max_length=255)),
                ('pc', models.CharField(max_length=255)),
                ('ra', models.CharField(max_length=255)),
                ('dec', models.CharField(max_length=255)),
                ('pos_ref', models.CharField(max_length=255)),
                ('alt_name', models.CharField(blank=True, max_length=255, null=True)),
                ('bands', djongo.models.fields.ArrayField(model_container=calibrators.models.BandDetail)),
            ],
        ),
    ]