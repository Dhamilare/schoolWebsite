# Generated by Django 3.2.6 on 2021-08-09 19:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schoolApp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='category',
        ),
        migrations.AddField(
            model_name='course',
            name='category',
            field=models.CharField(default='Digital Marketing', max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='postImages'),
        ),
    ]
