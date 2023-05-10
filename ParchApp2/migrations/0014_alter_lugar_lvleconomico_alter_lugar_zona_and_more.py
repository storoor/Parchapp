# Generated by Django 4.1.6 on 2023-03-20 02:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ParchApp2', '0013_rename_lugares_lugar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lugar',
            name='LvlEconomico',
            field=models.CharField(blank=True, choices=[('menor que 50k', 'menor que 50k'), ('entre 50k y 150k', 'entre 50k y 150k'), ('mas de 150k', 'mas de 150k')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='lugar',
            name='Zona',
            field=models.CharField(blank=True, choices=[('Envigado', 'Envigado'), ('Poblado', 'Poblado')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='lugar',
            name='categoria',
            field=models.CharField(blank=True, choices=[('Discoteca', 'Discoteca'), ('Restaurante', 'Restaurante'), ('Mirador', 'Mirador')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='lugar',
            name='edad',
            field=models.CharField(blank=True, choices=[('menor de edad', 'menor de edad'), ('mayor de edad', 'mayor de edad')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='lugar',
            name='nombre',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
