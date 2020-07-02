# Generated by Django 3.0.6 on 2020-06-29 15:58

from django.db import migrations, models
import django.db.models.deletion
import music_publisher.validators


class Migration(migrations.Migration):

    dependencies = [
        ('music_publisher', '0006_auto_20200615_1026'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='alternatetitle',
            options={'ordering': ('-suffix', 'title'), 'verbose_name': 'Alternative Title'},
        ),
        migrations.AlterModelOptions(
            name='commercialrelease',
            options={'verbose_name': 'Commercial Release', 'verbose_name_plural': 'Commercial Releases'},
        ),
        migrations.AlterModelOptions(
            name='cwrexport',
            options={'ordering': ('-id',), 'verbose_name': 'CWR Export', 'verbose_name_plural': 'CWR Exports'},
        ),
        migrations.AlterModelOptions(
            name='label',
            options={'verbose_name': 'Music Label'},
        ),
        migrations.AlterModelOptions(
            name='library',
            options={'ordering': ('name',), 'verbose_name': 'Music Libraries'},
        ),
        migrations.AlterModelOptions(
            name='libraryrelease',
            options={'verbose_name': 'Library Release', 'verbose_name_plural': 'Library Releases'},
        ),
        migrations.AlterModelOptions(
            name='recording',
            options={'ordering': ('-id',), 'verbose_name': 'Recording', 'verbose_name_plural': 'Recordings'},
        ),
        migrations.AlterModelOptions(
            name='release',
            options={'verbose_name': 'Release'},
        ),
        migrations.AlterModelOptions(
            name='track',
            options={'ordering': ('release', 'cut_number'), 'verbose_name': 'Track'},
        ),
        migrations.AlterModelOptions(
            name='writer',
            options={'ordering': ('last_name', 'first_name', 'ipi_name', '-id'), 'verbose_name': 'Writer', 'verbose_name_plural': 'Writers'},
        ),
        migrations.AlterModelOptions(
            name='writerinwork',
            options={'ordering': ('-controlled', 'writer__last_name', 'writer__first_name', '-id'), 'verbose_name': 'Writer in Work', 'verbose_name_plural': 'Writers in Work'},
        ),
        migrations.AlterField(
            model_name='work',
            name='library_release',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='works', to='music_publisher.LibraryRelease', verbose_name='Library release'),
        ),
        migrations.AlterField(
            model_name='work',
            name='original_title',
            field=models.CharField(blank=True, db_index=True, help_text='Use only for modification of existing works.', max_length=60, validators=[music_publisher.validators.CWRFieldValidator('work_title')], verbose_name='Title of original work'),
        ),
        migrations.AlterField(
            model_name='workacknowledgement',
            name='remote_work_id',
            field=models.CharField(blank=True, db_index=True, max_length=20, verbose_name='Remote work ID'),
        ),
        migrations.AlterField(
            model_name='writer',
            name='ipi_base',
            field=models.CharField(blank=True, max_length=15, null=True, validators=[music_publisher.validators.CWRFieldValidator('ipi_base')], verbose_name='IPI base #'),
        ),
        migrations.AlterField(
            model_name='writer',
            name='ipi_name',
            field=models.CharField(blank=True, max_length=11, null=True, unique=True, validators=[music_publisher.validators.CWRFieldValidator('ipi_name')], verbose_name='IPI name #'),
        ),
        migrations.AlterIndexTogether(
            name='workacknowledgement',
            index_together={('society_code', 'remote_work_id')},
        ),
    ]