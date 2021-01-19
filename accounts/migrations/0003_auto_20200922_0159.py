# Generated by Django 3.0.7 on 2020-09-21 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20200922_0126'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='category',
            field=models.CharField(blank=True, choices=[('Fish', 'Fish'), ('Sports', 'Sports'), ('Casino', 'Casino'), ('7/11', '7/11'), ('Slot', 'Slot')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='promotion',
            name='game_category',
            field=models.CharField(blank=True, choices=[('Fish', 'Fish'), ('Sports', 'Sports'), ('Casino', 'Casino'), ('7/11', '7/11'), ('Slot', 'Slot')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='promotion',
            name='restriction_category',
            field=models.CharField(blank=True, choices=[('Fish', 'Fish'), ('Sports', 'Sports'), ('Casino', 'Casino'), ('7/11', '7/11'), ('Slot', 'Slot')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='promotion',
            name='tag1',
            field=models.CharField(blank=True, choices=[('Lock Credit', 'Lock Credit'), ('Withdrawal', 'Withdrawal'), ('Borrow Credit', 'Borrow Credit'), ('Free Credit', 'Free Credit'), ('Promo', 'Promo'), ('Recommend', 'Recommend'), ('Void Credit', 'Void Credit')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='promotion',
            name='tag2',
            field=models.CharField(blank=True, choices=[('No Bonus Topup', 'No Bonus (Below Minimum Topup Amount)'), ('Rebate Bonus', 'Rebate Bonus'), ('Ticket', 'Ticket'), ('No Bonus', 'No Bonus')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='promotion',
            name='usage',
            field=models.CharField(blank=True, choices=[('Twice a Day', 'Twice a Day'), ('Yearly', 'Yearly'), ('Thrice a Day', 'Thrice a Day'), ('Monthly', 'Monthly'), ('Daily', 'Daily'), ('Unlimited', 'Unlimited'), ('Weekly', 'Weekly'), ('One Time Only', 'One Time Only')], max_length=200, null=True),
        ),
    ]
