# Generated by Django 4.2.5 on 2024-02-23 01:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_conversationhistory_lastcommand'),
    ]

    operations = [
        migrations.AlterField(
            model_name='conversationhistory',
            name='lastCommand',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
