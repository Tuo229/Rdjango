# Generated by Django 3.0 on 2020-12-19 21:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('immob', '0003_auto_20201218_2234'),
    ]

    operations = [
        migrations.AddField(
            model_name='agence',
            name='Commune',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='immob.Ville', verbose_name='Ville ou commune'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='agence',
            name='num_cpte',
            field=models.CharField(default=1, max_length=50, verbose_name='Numero de compte contribiable'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='agence',
            name='regi_commerce',
            field=models.CharField(default=1, max_length=128, verbose_name='Regis de commerce'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='ag_admin',
            field=models.BooleanField(default=True, verbose_name='Administrateur agence'),
        ),
        migrations.AlterField(
            model_name='agence',
            name='localite',
            field=models.CharField(max_length=254, verbose_name='Adresse postale'),
        ),
        migrations.AlterField(
            model_name='agence',
            name='nom',
            field=models.CharField(max_length=128, verbose_name='Nom agence'),
        ),
        migrations.AlterField(
            model_name='agence',
            name='status',
            field=models.BooleanField(default=False, verbose_name='Aggréer ou non'),
        ),
        migrations.AlterField(
            model_name='besoins',
            name='commune',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='immob.Ville', verbose_name='Ville ou commune'),
        ),
        migrations.AlterField(
            model_name='immobilier',
            name='image_1',
            field=models.ImageField(default=1, upload_to='C:\\Users\\Tuo\\Desktop\\Projet\\django\\envs\\ndcimmob\\immbo/static/immob/'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='immobilier',
            name='image_2',
            field=models.ImageField(blank=True, null=True, upload_to='C:\\Users\\Tuo\\Desktop\\Projet\\django\\envs\\ndcimmob\\immbo/static/immob/'),
        ),
    ]
