# Generated by Django 4.0.6 on 2022-07-21 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qa', '0006_alter_question_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answer',
            name='question',
        ),
        migrations.AlterField(
            model_name='question',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
