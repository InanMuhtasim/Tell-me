# Generated by Django 5.1.4 on 2025-01-01 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('letters', '0004_alter_confession_creator_alter_confession_key'),
    ]

    operations = [
        migrations.AlterField(
            model_name='confession',
            name='letter_id',
            field=models.SlugField(primary_key=True, serialize=False),
        ),
    ]