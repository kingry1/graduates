# Generated by Django 2.2 on 2019-04-21 09:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0011_auto_20190421_0909'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='ball',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ball', to='crud.Ball'),
        ),
        migrations.AlterField(
            model_name='student',
            name='work',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='work', to='crud.Work'),
        ),
    ]
