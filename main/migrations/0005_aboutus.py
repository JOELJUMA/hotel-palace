# Generated by Django 4.2.7 on 2023-11-29 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_contactinquiry'),
    ]

    operations = [
        migrations.CreateModel(
            name='AboutUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mission', models.TextField()),
                ('vision', models.TextField()),
                ('goal', models.TextField()),
                ('mission_statement', models.TextField()),
            ],
        ),
    ]
