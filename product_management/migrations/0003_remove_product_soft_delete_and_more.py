# Generated by Django 4.2.5 on 2023-10-06 07:26

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("product_management", "0002_product_soft_delete_product_variant_soft_delete"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="product",
            name="soft_delete",
        ),
        migrations.RemoveField(
            model_name="product_variant",
            name="soft_delete",
        ),
    ]