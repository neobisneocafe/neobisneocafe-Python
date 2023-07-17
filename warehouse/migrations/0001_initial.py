# Generated by Django 4.2.2 on 2023-07-17 15:05

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Branches',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('address', models.CharField(max_length=255)),
                ('city', models.CharField(max_length=255)),
                ('country', models.CharField(max_length=255)),
                ('phone', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('opening_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('closing_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('manager_name', models.CharField(max_length=255)),
                ('location_url', models.URLField(blank=True, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('is_deleted', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Warehouse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_id', models.IntegerField(default=None)),
                ('quantity', models.IntegerField(default=None)),
                ('arrivalDate', models.DateTimeField(default=django.utils.timezone.now)),
                ('expirationDate', models.DateTimeField(default=django.utils.timezone.now)),
                ('supplier', models.CharField(max_length=100)),
                ('weight', models.CharField(max_length=100)),
                ('price', models.CharField(default='0', max_length=100)),
                ('isDeleted', models.BooleanField(default=False)),
                ('branches_id', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='warehouse.branches')),
                ('category_id', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='warehouse.category')),
            ],
        ),
    ]
