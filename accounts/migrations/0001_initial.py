# Generated by Django 3.1.1 on 2021-01-25 16:22

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import re


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bank',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bank_name', models.CharField(max_length=200, unique=True)),
                ('bank_code', models.CharField(max_length=200)),
                ('bank_username', models.CharField(blank=True, max_length=200, null=True)),
                ('bank_password', models.CharField(blank=True, max_length=200, null=True)),
                ('bank_url', models.CharField(blank=True, max_length=200, null=True)),
                ('account_name', models.CharField(blank=True, max_length=200, null=True)),
                ('account_number', models.CharField(blank=True, max_length=30, null=True)),
                ('image', models.ImageField(upload_to='bank/')),
                ('status', models.CharField(choices=[('Active', 'Active'), ('Inactive', 'Inactive')], default='Active', max_length=80, verbose_name='Status')),
                ('status_deposit', models.CharField(choices=[('Active', 'Active'), ('Inactive', 'Inactive')], default='Active', max_length=80)),
                ('status_withdrawal', models.CharField(choices=[('Active', 'Active'), ('Inactive', 'Inactive')], default='Active', max_length=80)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=15, unique=True, validators=[django.core.validators.RegexValidator(re.compile('^\\d+(?:,\\d+)*\\Z'), code='invalid', message=None), django.core.validators.MinLengthValidator(9)])),
                ('gander', models.CharField(blank=True, max_length=50, null=True)),
                ('wechat', models.CharField(blank=True, max_length=254, null=True)),
                ('telegram', models.CharField(blank=True, max_length=254, null=True)),
                ('email', models.EmailField(blank=True, default='NoEmail@gmail.com', max_length=254, null=True)),
                ('status', models.CharField(choices=[('Active', 'Active'), ('Inactive', 'Inactive')], default='Active', max_length=80)),
                ('blacklist', models.CharField(choices=[('No', 'No'), ('Blacklist', 'Blacklist'), ('Banned', 'Banned')], default='No', max_length=80)),
                ('language', models.CharField(choices=[('Malay', 'Malay'), ('Chinese', 'Chinese'), ('English', 'English')], default='Malay', max_length=80)),
                ('remark', models.TextField(blank=True, max_length=254, null=True)),
                ('description', models.TextField(blank=True, max_length=254, null=True)),
                ('game_count', models.IntegerField(default=0)),
                ('user_link', models.CharField(blank=True, max_length=50, null=True)),
                ('account_name', models.CharField(blank=True, max_length=254, null=True)),
                ('account_number', models.CharField(blank=True, max_length=254, null=True)),
                ('bank_message', models.TextField(blank=True, max_length=3000, null=True)),
                ('Bank_remark', models.TextField(blank=True, max_length=3000, null=True)),
                ('Bank_status', models.CharField(choices=[('Active', 'Active'), ('Inactive', 'Inactive')], default='Active', max_length=80)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('bank_name', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.bank')),
            ],
        ),
        migrations.CreateModel(
            name='CustomerBank',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account_name', models.CharField(blank=True, max_length=200, null=True)),
                ('account_number', models.CharField(blank=True, max_length=200, null=True)),
                ('message', models.TextField(blank=True, max_length=3000, null=True, verbose_name='Message')),
                ('remark', models.TextField(blank=True, max_length=3000, null=True, verbose_name='Remark')),
                ('status', models.CharField(choices=[('Active', 'Active'), ('Inactive', 'Inactive')], default='Active', max_length=80)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('bank_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.bank')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.customer')),
            ],
        ),
        migrations.CreateModel(
            name='CustomerGame',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(blank=True, max_length=200, null=True)),
                ('password', models.CharField(blank=True, max_length=200, null=True)),
                ('message', models.TextField(blank=True, max_length=254, null=True, verbose_name='Message')),
                ('remark', models.TextField(blank=True, max_length=254, null=True, verbose_name='Remark')),
                ('status', models.CharField(choices=[('Active', 'Active'), ('Inactive', 'Inactive')], default='Active', max_length=80)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('customerID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.customer')),
            ],
        ),
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=254, unique=True)),
                ('category', models.CharField(blank=True, choices=[('Fish', 'Fish'), ('Sports', 'Sports'), ('Casino', 'Casino'), ('7/11', '7/11'), ('Slot', 'Slot')], max_length=200, null=True)),
                ('url', models.CharField(blank=True, max_length=254, null=True)),
                ('code', models.CharField(blank=True, max_length=254, null=True)),
                ('admin_username', models.CharField(blank=True, max_length=254, null=True)),
                ('admin_password1', models.CharField(blank=True, max_length=254, null=True)),
                ('admin_password2', models.CharField(blank=True, max_length=254, null=True)),
                ('admin_agent_id', models.CharField(blank=True, max_length=254, null=True)),
                ('kiosk_url', models.CharField(blank=True, max_length=254, null=True)),
                ('link_adduser', models.CharField(blank=True, max_length=254, null=True)),
                ('link_setscore', models.CharField(blank=True, max_length=254, null=True)),
                ('link_scorelog', models.CharField(blank=True, max_length=254, null=True)),
                ('link_gamelog', models.CharField(blank=True, max_length=254, null=True)),
                ('link_resetpass', models.CharField(blank=True, max_length=254, null=True)),
                ('message_topup', models.TextField(blank=True, max_length=254, null=True)),
                ('point', models.FloatField(default=0)),
                ('display_status', models.CharField(choices=[('Active', 'Active'), ('Inactive', 'Inactive')], default='Active', max_length=200, null=True)),
                ('status', models.CharField(choices=[('Active', 'Active'), ('Inactive', 'Inactive')], default='Active', max_length=200, null=True)),
                ('display_pool_id_status', models.CharField(choices=[('Active', 'Active'), ('Inactive', 'Inactive')], default='Active', max_length=200, null=True)),
                ('credit', models.FloatField(default=0)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='MaxWithdrawal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('limit', models.IntegerField(default=3)),
                ('status', models.CharField(choices=[('Active', 'Active'), ('Inactive', 'Inactive')], default='Active', max_length=80, verbose_name='Status')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Promotion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=254)),
                ('category', models.CharField(blank=True, choices=[('Main', 'Main')], max_length=200, null=True)),
                ('tag1', models.CharField(blank=True, choices=[('Promo', 'Promo'), ('Recommend', 'Recommend'), ('Free Credit', 'Free Credit'), ('Borrow Credit', 'Borrow Credit'), ('Lock Credit', 'Lock Credit'), ('Void Credit', 'Void Credit'), ('Withdrawal', 'Withdrawal')], max_length=200, null=True)),
                ('tag2', models.CharField(blank=True, choices=[('Ticket', 'Ticket'), ('No Bonus Topup', 'No Bonus (Below Minimum Topup Amount)'), ('No Bonus', 'No Bonus'), ('Rebate Bonus', 'Rebate Bonus')], max_length=200, null=True)),
                ('ticket_tag', models.CharField(blank=True, choices=[('Accumulate', 'By Accumulate'), ('Ticket', 'By Per Ticket')], max_length=200, null=True)),
                ('amount_percentage', models.IntegerField(default=0)),
                ('amount', models.FloatField(default=0.0)),
                ('max_claim_amount', models.FloatField(default=0.0)),
                ('min_transaction_amount', models.FloatField(default=0.0)),
                ('max_transaction_amount', models.FloatField(default=0.0)),
                ('min_deposit_amount', models.FloatField(default=0.0)),
                ('max_deposit_amount', models.FloatField(default=0.0)),
                ('min_withdrawal_rollover', models.FloatField(default=0.0)),
                ('max_withdrawal_rollover', models.FloatField(default=0.0)),
                ('min_withdrawal_turnover', models.FloatField(default=0.0)),
                ('max_withdrawal_turnover', models.FloatField(default=0.0)),
                ('min_withdrawal_amount', models.FloatField(default=0.0)),
                ('max_withdrawal_amount', models.FloatField(default=0.0)),
                ('override', models.CharField(blank=True, choices=[('On', 'On'), ('Off', 'Off')], default='Off', max_length=200, null=True)),
                ('rebate_date_from', models.CharField(blank=True, max_length=254, null=True)),
                ('rebate_date_to', models.CharField(blank=True, max_length=254, null=True)),
                ('rebate_day', models.CharField(blank=True, choices=[('Monday', 'Monday'), ('Tuesday', 'Tuesday'), ('Wednesday', 'Wednesday'), ('Thursday', 'Thursday'), ('Friday', 'Friday'), ('Saturday', 'Saturday'), ('Sunday', 'Sunday')], default='Off', max_length=200, null=True)),
                ('game_category', models.CharField(blank=True, choices=[('Fish', 'Fish'), ('Sports', 'Sports'), ('Casino', 'Casino'), ('7/11', '7/11'), ('Slot', 'Slot')], max_length=200, null=True)),
                ('restriction_category', models.CharField(blank=True, choices=[('Fish', 'Fish'), ('Sports', 'Sports'), ('Casino', 'Casino'), ('7/11', '7/11'), ('Slot', 'Slot')], max_length=200, null=True)),
                ('usage', models.CharField(blank=True, choices=[('Unlimited', 'Unlimited'), ('Thrice a Day', 'Thrice a Day'), ('Weekly', 'Weekly'), ('Twice a Day', 'Twice a Day'), ('Yearly', 'Yearly'), ('Daily', 'Daily'), ('One Time Only', 'One Time Only'), ('Monthly', 'Monthly')], max_length=200, null=True)),
                ('message', models.TextField(blank=True, max_length=254, null=True)),
                ('status', models.CharField(choices=[('Active', 'Active'), ('Inactive', 'Inactive')], default='Active', max_length=200, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('restriction_game', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.game')),
            ],
        ),
        migrations.CreateModel(
            name='Referral',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=254, unique=True)),
                ('image', models.ImageField(upload_to='referral/')),
                ('status', models.CharField(choices=[('Active', 'Active'), ('Inactive', 'Inactive')], default='Active', max_length=80, verbose_name='Status')),
                ('total', models.IntegerField(blank=True, default=0, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='SMSGateway',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=254, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='SuccessMessage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('m_deposit', models.TextField(blank=True, default='No Setup Message', max_length=5000, null=True)),
                ('m_withdrawal', models.TextField(blank=True, default='No Setup Message', max_length=5000, null=True)),
                ('m_transfer', models.TextField(blank=True, default='No Setup Message', max_length=5000, null=True)),
                ('m_newgameid', models.TextField(blank=True, default='No Setup Message', max_length=5000, null=True)),
                ('m_lock', models.TextField(blank=True, default='No Setup Message', max_length=5000, null=True)),
                ('m_unlock', models.TextField(blank=True, default='No Setup Message', max_length=5000, null=True)),
                ('m_withdrawal_verify_bank', models.TextField(blank=True, default='No Setup Message', max_length=5000, null=True)),
                ('m_promotion_4d', models.TextField(blank=True, default='No Setup Message', max_length=5000, null=True)),
                ('c_deposit', models.TextField(blank=True, default='No Setup Message', max_length=5000, null=True)),
                ('c_withdrawal', models.TextField(blank=True, default='No Setup Message', max_length=5000, null=True)),
                ('c_transfer', models.TextField(blank=True, default='No Setup Message', max_length=5000, null=True)),
                ('c_newgameid', models.TextField(blank=True, default='No Setup Message', max_length=5000, null=True)),
                ('c_lock', models.TextField(blank=True, default='No Setup Message', max_length=5000, null=True)),
                ('c_unlock', models.TextField(blank=True, default='No Setup Message', max_length=5000, null=True)),
                ('c_withdrawal_verify_bank', models.TextField(blank=True, default='No Setup Message', max_length=5000, null=True)),
                ('c_promotion_4d', models.TextField(blank=True, default='No Setup Message', max_length=5000, null=True)),
                ('e_deposit', models.TextField(blank=True, default='No Setup Message', max_length=5000, null=True)),
                ('e_withdrawal', models.TextField(blank=True, default='No Setup Message', max_length=5000, null=True)),
                ('e_transfer', models.TextField(blank=True, default='No Setup Message', max_length=5000, null=True)),
                ('e_newgameid', models.TextField(blank=True, default='No Setup Message', max_length=5000, null=True)),
                ('e_lock', models.TextField(blank=True, default='No Setup Message', max_length=5000, null=True)),
                ('e_unlock', models.TextField(blank=True, default='No Setup Message', max_length=5000, null=True)),
                ('e_withdrawal_verify_bank', models.TextField(blank=True, default='No Setup Message', max_length=5000, null=True)),
                ('e_promotion_4d', models.TextField(blank=True, default='No Setup Message', max_length=5000, null=True)),
                ('admin', models.CharField(max_length=200)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('admin', models.CharField(max_length=200)),
                ('max_withdrawal', models.IntegerField(default=0)),
                ('last_topup', models.FloatField(default=0)),
                ('status', models.CharField(choices=[('Pending', 'Pending'), ('Approved', 'Approved'), ('Rejected', 'Rejected')], default='Pending', max_length=200)),
                ('completed', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], default='No', max_length=200)),
                ('tag', models.CharField(choices=[('Deposit', 'Deposit'), ('Free', 'Free'), ('Recommend', 'Recommend'), ('Lock', 'Lock'), ('Borrow', 'Borrow'), ('Withdrawal', 'Withdrawal'), ('Transfer', 'Transfer'), ('Add_Credit', 'Add Credit'), ('Deduct_Credit', 'Deduct Credit')], default='None', max_length=200)),
                ('remark', models.TextField(blank=True, max_length=254, null=True)),
                ('message', models.TextField(blank=True, max_length=254, null=True)),
                ('date', models.DateField(blank=True, null=True)),
                ('time', models.TimeField(blank=True, null=True)),
                ('amount', models.FloatField(default=0.0)),
                ('amount_free', models.FloatField(default=0.0)),
                ('amount_promo', models.FloatField(default=0.0)),
                ('amount_tip', models.FloatField(default=0.0)),
                ('amount_void', models.FloatField(default=0.0)),
                ('payback', models.FloatField(blank=True, default=0.0, null=True)),
                ('withdrawal_limit_min', models.FloatField(default=0.0)),
                ('withdrawal_limit_max', models.FloatField(blank=True, default=0.0, null=True)),
                ('action_approve', models.DateTimeField(blank=True, null=True)),
                ('action_reject', models.DateTimeField(blank=True, null=True)),
                ('action_complete', models.DateTimeField(blank=True, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('recommend_username', models.CharField(blank=True, max_length=254)),
                ('recommend_phone', models.CharField(blank=True, max_length=254)),
                ('bank', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.bank')),
                ('customer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.customer')),
                ('customer_bank', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.customerbank')),
                ('game', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='game', to='accounts.customergame')),
                ('game2', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='game2', to='accounts.customergame')),
                ('game_backend', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='game_backend', to='accounts.game')),
                ('promotion', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.promotion')),
            ],
        ),
        migrations.AddField(
            model_name='customergame',
            name='game_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.game'),
        ),
        migrations.AddField(
            model_name='customer',
            name='referral',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.referral'),
        ),
    ]
