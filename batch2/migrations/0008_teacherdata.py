# Generated by Django 4.1.3 on 2022-12-10 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('batch2', '0007_profiledata'),
    ]

    operations = [
        migrations.CreateModel(
            name='TeacherData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('age', models.IntegerField()),
                ('email', models.EmailField(max_length=200)),
            ],
        ),
    ]
