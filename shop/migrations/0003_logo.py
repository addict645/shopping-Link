# Generated by Django 3.1 on 2024-11-12 19:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_banner'),
    ]

    operations = [
        migrations.CreateModel(
            name='Logo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='logos/')),
                ('alt_text', models.CharField(blank=True, default='Site Logo', max_length=100, null=True)),
            ],
        ),
    ]
