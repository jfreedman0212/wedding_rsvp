# Generated by Django 5.1.4 on 2024-12-07 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('guests', '0003_guestgroup_updated_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='guestgroup',
            name='name',
            field=models.CharField(default='default_name', max_length=100),
            preserve_default=False,
        ),
    ]