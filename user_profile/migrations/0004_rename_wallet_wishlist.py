# Generated by Django 4.2.5 on 2023-10-23 18:37

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("product_management", "0002_alter_product_product_description"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("user_profile", "0003_initial"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="Wallet",
            new_name="WishList",
        ),
    ]