# Generated by Django 4.2.2 on 2023-08-04 11:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MenuCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='photos/menucategory')),
            ],
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('weight', models.IntegerField(default=0)),
                ('arrival_date', models.DateField()),
                ('quantity', models.DecimalField(decimal_places=0, default=1, max_digits=3)),
                ('min_limit', models.DecimalField(decimal_places=0, default=1, max_digits=3)),
            ],
        ),
        migrations.CreateModel(
            name='MenuItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('description', models.TextField(max_length=255)),
                ('price', models.DecimalField(decimal_places=0, default=0, max_digits=5)),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/menuitem/')),
                ('quantity', models.DecimalField(decimal_places=0, default=1, max_digits=3)),
                ('min_limit', models.DecimalField(decimal_places=0, default=1, max_digits=3)),
                ('arrivalDate', models.DateField()),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='menu.menucategory')),
                ('products', models.ManyToManyField(to='menu.products')),
            ],
        ),
    ]
