# Generated by Django 5.1.2 on 2024-11-04 15:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mailing_service', '0005_alter_mailing_message_delete_message'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='mailing',
            options={'permissions': [('can_view_mailing', 'Can view mailing'), ('can_block_user', 'Can block user'), ('can_disable_mailing', 'Can disable mailing')], 'verbose_name': 'Рассылка', 'verbose_name_plural': 'Рассылки'},
        ),
    ]

