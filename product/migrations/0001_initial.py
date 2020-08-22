# Generated by Django 3.1 on 2020-08-22 12:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='Nom du produit')),
                ('brands', models.CharField(max_length=100, verbose_name='Marques du produit')),
                ('link', models.URLField(unique=True)),
                ('nutriscore', models.CharField(max_length=1)),
                ('image', models.URLField()),
                ('fat', models.FloatField()),
                ('saturated_fat', models.FloatField()),
                ('sugars', models.FloatField()),
                ('salt', models.FloatField()),
            ],
            options={
                'verbose_name': 'Produit',
                'verbose_name_plural': 'Produits',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Favorite',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prod', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='prods', to='product.product')),
                ('sub', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subs', to='product.product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='users', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Favori',
                'verbose_name_plural': 'Favoris',
                'ordering': ['user'],
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('products', models.ManyToManyField(related_name='categories', to='product.Product')),
            ],
            options={
                'verbose_name': 'Catégorie',
                'verbose_name_plural': 'Catégories',
                'ordering': ['name'],
            },
        ),
    ]
