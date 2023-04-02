# Generated by Django 4.1.7 on 2023-03-25 22:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SplitWiseApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255)),
                ('user_name', models.CharField(max_length=255)),
                ('hashed_password', models.CharField(max_length=255)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.DeleteModel(
            name='Student',
        ),
    ]