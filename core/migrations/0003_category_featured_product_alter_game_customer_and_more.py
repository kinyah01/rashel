# Generated by Django 4.1.7 on 2023-02-14 17:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_rename_bet_game'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='featured_product',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='categorys', to='core.product'),
        ),
        migrations.AlterField(
            model_name='game',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='games', to='core.customer'),
        ),
        migrations.AlterField(
            model_name='game',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='games', to='core.product'),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='core.category'),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='wallet',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='transactions', to='core.wallet'),
        ),
        migrations.AlterField(
            model_name='wallet',
            name='customer',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='wallet', to='core.customer'),
        ),
    ]
