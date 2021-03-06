# Generated by Django 2.1.5 on 2019-03-09 21:52

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('glasses', '0002_auto_20190309_1523'),
    ]

    operations = [
        migrations.CreateModel(
            name='Response',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('needs_clarification', models.BooleanField(default=False)),
                ('in_progresss', models.BooleanField(default=False)),
                ('check_again', models.BooleanField(default=False)),
                ('fixed', models.BooleanField(default=False)),
                ('note', models.CharField(max_length=200)),
            ],
        ),
        migrations.RenameField(
            model_name='supposition',
            old_name='response',
            new_name='details',
        ),
        migrations.AddField(
            model_name='supposition',
            name='importance',
            field=models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(10), django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AddField(
            model_name='supposition',
            name='screenshot',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
        migrations.AddField(
            model_name='supposition',
            name='steps_to_manifest',
            field=jsonfield.fields.JSONField(default=[]),
        ),
        migrations.AddField(
            model_name='response',
            name='supposition',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='glasses.Supposition'),
        ),
    ]
