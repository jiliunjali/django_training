# Generated by Django 5.0.1 on 2024-01-25 07:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demoapp', '0005_alter_menucard_cartegory_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='MenuChart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dish', models.CharField(max_length=100)),
                ('price', models.IntegerField()),
                ('cuisine', models.CharField(help_text='enter what cuisine it is , eg: italian ', max_length=100)),
            ],
        ),
    ]
