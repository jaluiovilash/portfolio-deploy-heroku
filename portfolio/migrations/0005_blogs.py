# Generated by Django 5.0 on 2024-07-28 20:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0004_rename_phonenumber_contact_number_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blogs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=60)),
                ('description', models.TextField()),
                ('authName', models.CharField(max_length=15)),
                ('img', models.ImageField(blank=True, null=True, upload_to='blog')),
                ('timeStamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
