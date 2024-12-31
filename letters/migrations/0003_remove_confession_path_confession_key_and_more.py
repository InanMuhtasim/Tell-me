# Generated by Django 5.1.4 on 2024-12-29 07:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('letters', '0002_remove_confession_id_alter_confession_path'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='confession',
            name='path',
        ),
        migrations.AddField(
            model_name='confession',
            name='key',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='confession',
            name='letter_id',
            field=models.SlugField(default='-', max_length=10, primary_key=True, serialize=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='confession',
            name='letter_receiver',
            field=models.CharField(default='-', max_length=20),
            preserve_default=False,
        ),
        migrations.AlterModelTable(
            name='confession',
            table='confession',
        ),
    ]
