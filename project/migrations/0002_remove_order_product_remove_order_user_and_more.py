# Generated by Django 5.1.4 on 2024-12-10 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='product',
        ),
        migrations.RemoveField(
            model_name='order',
            name='user',
        ),
        migrations.AddField(
            model_name='order',
            name='product_id',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='user_id',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='quantity',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=254),
        ),
        migrations.AlterField(
            model_name='user',
            name='name',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
