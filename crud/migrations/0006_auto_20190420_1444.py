# Generated by Django 2.2 on 2019-04-20 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0005_auto_20190418_1621'),
    ]

    operations = [
        migrations.AddField(
            model_name='curator',
            name='description',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='curator',
            name='photo',
            field=models.ImageField(default='/assets/image/default.png', upload_to='assets/image'),
        ),
        migrations.AlterField(
            model_name='student',
            name='photo',
            field=models.FilePathField(null=True, path='/home/woolf/Workspace/Python/graduates/static/assets/image'),
        ),
    ]
