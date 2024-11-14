# Generated by Django 5.1.2 on 2024-11-02 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("clients", "0001_initial"),
        ("mailing_service", "0003_mailing_is_active"),
    ]

    operations = [
        migrations.AlterField(
            model_name="mailing",
            name="clients",
            field=models.ManyToManyField(
                related_name="mailings",
                to="clients.client",
                verbose_name="Клиент сервиса",
            ),
        ),
        migrations.DeleteModel(
            name="Client",
        ),
    ]
