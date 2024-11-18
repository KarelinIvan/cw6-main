# Generated by Django 5.1.3 on 2024-11-18 11:59

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("clients", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Attempt",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "attempt_datetime",
                    models.DateTimeField(
                        default=django.utils.timezone.now,
                        verbose_name="Дата и время попытки отправки рассылки",
                    ),
                ),
                (
                    "status",
                    models.CharField(
                        choices=[("successful", "Успешно"), ("failed", "Не успешно")],
                        max_length=20,
                    ),
                ),
                ("server_response", models.TextField(blank=True, null=True)),
            ],
            options={
                "verbose_name": "Попытка рассылки",
                "verbose_name_plural": "Попытки рассылки",
            },
        ),
        migrations.CreateModel(
            name="Mailing",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "start_datetime",
                    models.DateTimeField(
                        default=django.utils.timezone.now,
                        verbose_name="Дата и время первой рассылки",
                    ),
                ),
                (
                    "periodicity",
                    models.CharField(
                        choices=[
                            ("once", "Однократная"),
                            ("daily", "Раз в день"),
                            ("weekly", "Раз в неделю"),
                            ("monthly", "Раз в месяц"),
                        ],
                        default="once",
                        max_length=10,
                        verbose_name="Периодичность",
                    ),
                ),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("created", "Создана"),
                            ("started", "Запущена"),
                            ("completed", "Завершена"),
                        ],
                        default="created",
                        max_length=10,
                        verbose_name="Статус рассылки",
                    ),
                ),
                ("is_active", models.BooleanField(default=True)),
                (
                    "clients",
                    models.ManyToManyField(
                        related_name="mailings",
                        to="clients.client",
                        verbose_name="Клиент сервиса",
                    ),
                ),
            ],
            options={
                "verbose_name": "Рассылка",
                "verbose_name_plural": "Рассылки",
                "permissions": [
                    ("can_view_mailing", "Can view mailing"),
                    ("can_block_user", "Can block user"),
                    ("can_disable_mailing", "Can disable mailing"),
                ],
            },
        ),
    ]