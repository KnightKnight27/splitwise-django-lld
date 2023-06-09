# Generated by Django 4.1.7 on 2023-03-25 22:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SplitWiseApp', '0002_user_delete_student'),
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255)),
                ('participants', models.ManyToManyField(to='SplitWiseApp.user')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
