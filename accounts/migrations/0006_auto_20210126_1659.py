# Generated by Django 3.1.1 on 2021-01-26 07:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_auto_20210126_1647'),
    ]

    operations = [
        migrations.AddField(
            model_name='smsgateway',
            name='active',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='game',
            name='category',
            field=models.CharField(blank=True, choices=[('Sports', 'Sports'), ('Fish', 'Fish'), ('7/11', '7/11'), ('Slot', 'Slot'), ('Casino', 'Casino')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='promotion',
            name='game_category',
            field=models.CharField(blank=True, choices=[('Sports', 'Sports'), ('Fish', 'Fish'), ('7/11', '7/11'), ('Slot', 'Slot'), ('Casino', 'Casino')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='promotion',
            name='restriction_category',
            field=models.CharField(blank=True, choices=[('Sports', 'Sports'), ('Fish', 'Fish'), ('7/11', '7/11'), ('Slot', 'Slot'), ('Casino', 'Casino')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='promotion',
            name='tag1',
            field=models.CharField(blank=True, choices=[('Recommend', 'Recommend'), ('Borrow Credit', 'Borrow Credit'), ('Lock Credit', 'Lock Credit'), ('Withdrawal', 'Withdrawal'), ('Void Credit', 'Void Credit'), ('Free Credit', 'Free Credit'), ('Promo', 'Promo')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='promotion',
            name='tag2',
            field=models.CharField(blank=True, choices=[('Rebate Bonus', 'Rebate Bonus'), ('Ticket', 'Ticket'), ('No Bonus', 'No Bonus'), ('No Bonus Topup', 'No Bonus (Below Minimum Topup Amount)')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='promotion',
            name='usage',
            field=models.CharField(blank=True, choices=[('Weekly', 'Weekly'), ('Thrice a Day', 'Thrice a Day'), ('Monthly', 'Monthly'), ('Yearly', 'Yearly'), ('One Time Only', 'One Time Only'), ('Daily', 'Daily'), ('Unlimited', 'Unlimited'), ('Twice a Day', 'Twice a Day')], max_length=200, null=True),
        ),
    ]
