# Generated by Django 5.1.3 on 2024-12-04 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_remove_profile_id_user_alter_profile_profileimg_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profileimg',
            field=models.ImageField(default='blank-profilepicture.png', upload_to='profile_images/'),
        ),
    ]
