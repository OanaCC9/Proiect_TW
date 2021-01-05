# Generated by Django 3.1.5 on 2021-01-04 22:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='melriverModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('genre', models.CharField(blank=True, max_length=50, null=True)),
                ('img', models.ImageField(upload_to='media')),
            ],
        ),
    ]