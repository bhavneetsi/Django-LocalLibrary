# Generated by Django 2.0.5 on 2018-06-01 12:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0004_remove_bookinstance_book'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookinstance',
            name='book',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.Book'),
        ),
    ]