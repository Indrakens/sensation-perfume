# Generated by Django 3.2.23 on 2024-02-02 20:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0008_alter_userprofile_default_picture'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='default_country',
            new_name='profile_country',
        ),
        migrations.RenameField(
            model_name='userprofile',
            old_name='default_county',
            new_name='profile_county',
        ),
        migrations.RenameField(
            model_name='userprofile',
            old_name='default_phone_number',
            new_name='profile_phone_number',
        ),
        migrations.RenameField(
            model_name='userprofile',
            old_name='default_picture',
            new_name='profile_picture',
        ),
        migrations.RenameField(
            model_name='userprofile',
            old_name='default_postcode',
            new_name='profile_postcode',
        ),
        migrations.RenameField(
            model_name='userprofile',
            old_name='default_street_address1',
            new_name='profile_street_address1',
        ),
        migrations.RenameField(
            model_name='userprofile',
            old_name='default_street_address2',
            new_name='profile_street_address2',
        ),
        migrations.RenameField(
            model_name='userprofile',
            old_name='default_town_or_city',
            new_name='profile_town_or_city',
        ),
    ]
