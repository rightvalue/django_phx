# Generated by Django 3.1.1 on 2021-01-25 16:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Positions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group', models.CharField(max_length=254)),
                ('name', models.CharField(max_length=254)),
            ],
        ),
        migrations.AlterField(
            model_name='game',
            name='category',
            field=models.CharField(blank=True, choices=[('Fish', 'Fish'), ('Sports', 'Sports'), ('7/11', '7/11'), ('Slot', 'Slot'), ('Casino', 'Casino')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='promotion',
            name='game_category',
            field=models.CharField(blank=True, choices=[('Fish', 'Fish'), ('Sports', 'Sports'), ('7/11', '7/11'), ('Slot', 'Slot'), ('Casino', 'Casino')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='promotion',
            name='restriction_category',
            field=models.CharField(blank=True, choices=[('Fish', 'Fish'), ('Sports', 'Sports'), ('7/11', '7/11'), ('Slot', 'Slot'), ('Casino', 'Casino')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='promotion',
            name='tag1',
            field=models.CharField(blank=True, choices=[('Borrow Credit', 'Borrow Credit'), ('Lock Credit', 'Lock Credit'), ('Promo', 'Promo'), ('Withdrawal', 'Withdrawal'), ('Void Credit', 'Void Credit'), ('Free Credit', 'Free Credit'), ('Recommend', 'Recommend')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='promotion',
            name='usage',
            field=models.CharField(blank=True, choices=[('Twice a Day', 'Twice a Day'), ('Monthly', 'Monthly'), ('One Time Only', 'One Time Only'), ('Thrice a Day', 'Thrice a Day'), ('Weekly', 'Weekly'), ('Unlimited', 'Unlimited'), ('Daily', 'Daily'), ('Yearly', 'Yearly')], max_length=200, null=True),
        ),
        migrations.CreateModel(
            name='User_Position',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.positions')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
