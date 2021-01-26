# Generated by Django 3.1.1 on 2021-01-26 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0009_auto_20210127_0215'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='category',
            field=models.CharField(blank=True, choices=[('7/11', '7/11'), ('Sports', 'Sports'), ('Casino', 'Casino'), ('Slot', 'Slot'), ('Fish', 'Fish')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='promotion',
            name='game_category',
            field=models.CharField(blank=True, choices=[('7/11', '7/11'), ('Sports', 'Sports'), ('Casino', 'Casino'), ('Slot', 'Slot'), ('Fish', 'Fish')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='promotion',
            name='restriction_category',
            field=models.CharField(blank=True, choices=[('7/11', '7/11'), ('Sports', 'Sports'), ('Casino', 'Casino'), ('Slot', 'Slot'), ('Fish', 'Fish')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='promotion',
            name='tag1',
            field=models.CharField(blank=True, choices=[('Borrow Credit', 'Borrow Credit'), ('Recommend', 'Recommend'), ('Free Credit', 'Free Credit'), ('Withdrawal', 'Withdrawal'), ('Void Credit', 'Void Credit'), ('Promo', 'Promo'), ('Lock Credit', 'Lock Credit')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='promotion',
            name='tag2',
            field=models.CharField(blank=True, choices=[('No Bonus Topup', 'No Bonus (Below Minimum Topup Amount)'), ('No Bonus', 'No Bonus'), ('Rebate Bonus', 'Rebate Bonus'), ('Ticket', 'Ticket')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='promotion',
            name='usage',
            field=models.CharField(blank=True, choices=[('Yearly', 'Yearly'), ('Monthly', 'Monthly'), ('Unlimited', 'Unlimited'), ('Daily', 'Daily'), ('One Time Only', 'One Time Only'), ('Weekly', 'Weekly'), ('Thrice a Day', 'Thrice a Day'), ('Twice a Day', 'Twice a Day')], max_length=200, null=True),
        ),
    ]
