# Generated by Django 2.2.1 on 2020-05-27 09:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('medicine', '0001_initial'),
        ('animal', '0001_initial'),
        ('people', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_opp', models.DateField(blank=True, default=None, null=True)),
                ('number_animal', models.IntegerField()),
                ('address', models.CharField(max_length=100)),
                ('total_price', models.DecimalField(decimal_places=2, default=None, max_digits=8, null=True)),
                ('invoice_number', models.CharField(blank=True, default=None, max_length=10, null=True)),
                ('animal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='animal.Animals')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='people.People')),
            ],
            options={
                'ordering': ('date_opp',),
            },
        ),
        migrations.CreateModel(
            name='MedicationBill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity_medicine', models.IntegerField()),
                ('sale_price', models.DecimalField(decimal_places=2, max_digits=8)),
                ('total_price', models.DecimalField(decimal_places=2, max_digits=8)),
                ('invoice', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='invoices', to='facture.Invoice')),
                ('medecine', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='medicine.Medicine')),
            ],
            options={
                'ordering': ('invoice',),
            },
        ),
    ]
