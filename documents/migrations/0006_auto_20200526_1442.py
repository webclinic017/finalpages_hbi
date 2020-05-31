# Generated by Django 2.2 on 2020-05-26 06:42

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('documents', '0005_rawproduct'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Product',
            new_name='ProductModel',
        ),
        migrations.RenameModel(
            old_name='Proposal',
            new_name='ProposalModel',
        ),
        migrations.RenameModel(
            old_name='PurchaseOrder',
            new_name='PurchaseOrderModel',
        ),
        migrations.RenameModel(
            old_name='RawProduct',
            new_name='RawProductModel',
        ),
    ]