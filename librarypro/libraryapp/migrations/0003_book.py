# Generated by Django 5.0 on 2024-04-24 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libraryapp', '0002_remove_user_username_user_name_alter_user_email_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('author', models.CharField(max_length=100)),
                ('publication_date', models.DateField()),
                ('isbn', models.CharField(max_length=13)),
            ],
        ),
    ]
