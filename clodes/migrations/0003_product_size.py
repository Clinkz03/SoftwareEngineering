# Generated by Django 5.1.5 on 2025-03-09 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clodes', '0002_alter_category_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='size',
            field=models.CharField(max_length=1, null=True),
        ),
    ]
