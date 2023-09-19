# Generated by Django 4.2.5 on 2023-09-10 22:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('debtors', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('payment_date', models.DateField()),
                ('payment_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('payment_status', models.CharField(choices=[('On time', 'On time'), ('Late', 'Late'), ('Missed', 'Missed')], max_length=50)),
                ('debtor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='debtors.debtor')),
            ],
            options={
                'db_table': 'payment',
            },
        ),
    ]