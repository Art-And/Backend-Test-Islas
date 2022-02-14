# Generated by Django 3.0.8 on 2022-02-14 08:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Option',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='meal option name', max_length=255, verbose_name='label name')),
                ('text_option', models.TextField(blank=True, help_text='meal text', null=True)),
            ],
        ),
    ]
