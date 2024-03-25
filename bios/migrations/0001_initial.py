# Generated by Django 5.0.3 on 2024-03-25 15:58

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('musicians', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=100)),
                ('title', models.CharField(max_length=50)),
                ('published_date', models.DateField(null=True)),
                ('musician', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='musicians.musician')),
            ],
        ),
    ]
