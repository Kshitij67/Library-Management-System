# Generated by Django 5.1.1 on 2024-09-06 16:45

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lims_app', '0005_book_is_available'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='is_reading',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='users',
            name='book_reading',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='lims_app.book'),
        ),
    ]
