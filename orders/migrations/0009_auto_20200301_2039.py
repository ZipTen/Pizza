# Generated by Django 2.0.3 on 2020-03-01 12:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0008_auto_20200229_1337'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='addeditem',
            name='extras',
        ),
        migrations.AlterField(
            model_name='extraselection',
            name='main',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='extras', to='orders.AddedItem'),
        ),
    ]
