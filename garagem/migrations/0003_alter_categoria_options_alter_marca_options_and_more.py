# Generated by Django 4.2.4 on 2023-08-28 19:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('uploader', '0001_initial'),
        ('garagem', '0002_veiculo_capa'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='categoria',
            options={'verbose_name': 'Categoria', 'verbose_name_plural': 'Categorias'},
        ),
        migrations.AlterModelOptions(
            name='marca',
            options={'verbose_name': 'Marca', 'verbose_name_plural': 'Marcas'},
        ),
        migrations.AlterModelOptions(
            name='veiculo',
            options={'verbose_name': 'veículo', 'verbose_name_plural': 'veículos'},
        ),
        migrations.RemoveField(
            model_name='marca',
            name='nacionalidade',
        ),
        migrations.RemoveField(
            model_name='veiculo',
            name='capa',
        ),
        migrations.RemoveField(
            model_name='veiculo',
            name='categoria',
        ),
        migrations.RemoveField(
            model_name='veiculo',
            name='marca',
        ),
        migrations.AddField(
            model_name='veiculo',
            name='acessorios',
            field=models.ManyToManyField(related_name='veiculos', to='garagem.acessorio'),
        ),
        migrations.AddField(
            model_name='veiculo',
            name='descricao',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='veiculo',
            name='imagem',
            field=models.ManyToManyField(related_name='+', to='uploader.image'),
        ),
        migrations.AlterField(
            model_name='marca',
            name='nome',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='veiculo',
            name='ano',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='veiculo',
            name='cor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='veiculos', to='garagem.cor'),
        ),
        migrations.CreateModel(
            name='Modelo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='modelos', to='garagem.categoria')),
                ('marca', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='modelos', to='garagem.marca')),
            ],
            options={
                'verbose_name': 'Modelo',
                'verbose_name_plural': 'Modelos',
            },
        ),
        migrations.AddField(
            model_name='veiculo',
            name='modelo',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, related_name='veiculos', to='garagem.modelo'),
            preserve_default=False,
        ),
    ]
