# Generated by Django 4.2.7 on 2023-11-24 07:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sudent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('departent', models.CharField(max_length=10)),
                ('rollnumber', models.IntegerField()),
            ],
        ),
    ]
