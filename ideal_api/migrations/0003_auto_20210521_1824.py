# Generated by Django 3.1.3 on 2021-05-21 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Ideal_api', '0002_contact'),
    ]

    operations = [
        migrations.AddField(
            model_name='about',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='image/'),
        ),
        migrations.AddField(
            model_name='about',
            name='professionalism',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]