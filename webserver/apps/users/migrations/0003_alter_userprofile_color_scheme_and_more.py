# Generated by Django 4.1.7 on 2023-03-02 21:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_userprofile_user_register_ip'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='color_scheme',
            field=models.CharField(choices=[('light', 'Light'), ('dark', 'Dark'), ('system', 'System')], default='system', max_length=50),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='flag',
            field=models.ImageField(blank=True, null=True, upload_to='flags'),
        ),
    ]
