# Generated by Django 2.1.7 on 2019-07-11 12:20

from django.db import migrations, models
import django.db.models.deletion
import music_publisher.base

def move_key_to_work(apps, schema_editor):
    Work = apps.get_model('music_publisher', 'Work')
    for work in Work.objects.filter(recording__album_cd__cd_identifier__isnull = False):
        release = work.recording.album_cd
        work.library_release = release
        work.save()
        work.recording.album_cd = None
        work.recording.save()

def import_library_from_settings(apps, schema_edito):
    LibraryRelease = apps.get_model('music_publisher', 'LibraryRelease')
    Library = apps.get_model('music_publisher', 'Library')
    library_name = settings.MUSIC_PUBLISHER_SETTINGS.get('library')
    if not library_name:
        raise Exception()
    library, created = Library.objects.get_or_create(name=library_name)
    for release in LibraryRelease.objects.all():
        release.library = library
        release.save()

def release_labels_to_table(apps, schema_edito):
    Label = apps.get_model('music_publisher', 'Label')
    LibraryRelease = apps.get_model('music_publisher', 'LibraryRelease')
    for release in LibraryRelease.objects.all():
        if not release.release_label:
            continue
        label, created = Label.objects.get_or_create(
            name=release.release_label)
        release._release_label = label
        release.save()

# Functions from the following migrations need manual copying.
# Move them and any dependencies into this file, then update the
# RunPython operations to refer to the local versions:
# music_publisher.migrations.0004_auto_20190708_0933
# music_publisher.migrations.0012_release_library
# music_publisher.migrations.0013_auto_20190709_0854

class Migration(migrations.Migration):

    replaces = [('music_publisher', '0002_auto_20190708_0840'), ('music_publisher', '0003_auto_20190708_0843'), ('music_publisher', '0004_auto_20190708_0933'), ('music_publisher', '0005_auto_20190708_1044'), ('music_publisher', '0006_auto_20190708_1050'), ('music_publisher', '0007_auto_20190708_1221'), ('music_publisher', '0008_auto_20190708_1223'), ('music_publisher', '0009_auto_20190708_1235'), ('music_publisher', '0010_commercialrelease'), ('music_publisher', '0011_auto_20190709_0822'), ('music_publisher', '0012_release_library'), ('music_publisher', '0013_auto_20190709_0854'), ('music_publisher', '0014_remove_release_release_label'), ('music_publisher', '0015_auto_20190709_0855'), ('music_publisher', '0016_auto_20190709_1138'), ('music_publisher', '0017_remove_recording_record_label'), ('music_publisher', '0018_auto_20190709_1140'), ('music_publisher', '0019_auto_20190710_0958'), ('music_publisher', '0020_auto_20190710_0959'), ('music_publisher', '0021_auto_20190710_1135')]

    dependencies = [
        ('music_publisher', '0001_squashed_0023_auto_20190212_0907'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='FirstRecording',
            new_name='Recording',
        ),
        migrations.RenameModel(
            old_name='AlbumCD',
            new_name='Release',
        ),
        migrations.CreateModel(
            name='LibraryRelease',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
            },
            bases=('music_publisher.release',),
        ),
        migrations.AddField(
            model_name='work',
            name='library_release',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='music_publisher.Release', verbose_name='Library Release'),
        ),
        migrations.RunPython(
            code=move_key_to_work,
        ),
        migrations.AlterField(
            model_name='work',
            name='library_release',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='music_publisher.LibraryRelease', verbose_name='Library Release'),
        ),
        migrations.AlterField(
            model_name='recording',
            name='work',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='recordings', to='music_publisher.Work'),
        ),
        migrations.AlterField(
            model_name='release',
            name='album_label',
            field=models.CharField(blank=True, default='FOO BAR MUSIC', max_length=60, validators=[music_publisher.base.CWRFieldValidator('first_album_label')], verbose_name='Release (album) label'),
        ),
        migrations.AlterField(
            model_name='release',
            name='album_title',
            field=models.CharField(blank=True, max_length=60, null=True, unique=True, validators=[music_publisher.base.CWRFieldValidator('first_album_title')], verbose_name='Release (album) title '),
        ),
        migrations.AlterField(
            model_name='release',
            name='cd_identifier',
            field=models.CharField(blank=True, max_length=15, null=True, unique=True, validators=[music_publisher.base.CWRFieldValidator('cd_identifier')], verbose_name='Release (CD) identifier'),
        ),
        migrations.AlterModelOptions(
            name='release',
            options={'ordering': ('release_title', 'cd_identifier', '-id'), 'verbose_name': 'Album and/or Library CD', 'verbose_name_plural': ' Albums and Library CDs'},
        ),
        migrations.RenameField(
            model_name='release',
            old_name='album_label',
            new_name='release_label',
        ),
        migrations.RenameField(
            model_name='release',
            old_name='album_title',
            new_name='release_title',
        ),
        migrations.AlterField(
            model_name='release',
            name='ean',
            field=models.CharField(blank=True, max_length=13, null=True, unique=True, validators=[music_publisher.base.CWRFieldValidator('ean')], verbose_name='Release (album) EAN'),
        ),
        migrations.AlterField(
            model_name='release',
            name='cd_identifier',
            field=models.CharField(blank=True, max_length=15, null=True, unique=True, validators=[music_publisher.base.CWRFieldValidator('cd_identifier')], verbose_name='CD identifier'),
        ),
        migrations.CreateModel(
            name='CommercialRelease',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
            },
            bases=('music_publisher.release',),
        ),
        migrations.CreateModel(
            name='Label',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60, unique=True, validators=[music_publisher.base.CWRFieldValidator('label')])),
            ],
            options={
                'ordering': ('-id',),
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Library',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60, unique=True, validators=[music_publisher.base.CWRFieldValidator('library')])),
            ],
            options={
                'ordering': ('-id',),
                'abstract': False,
            },
        ),
        migrations.AlterModelOptions(
            name='artistinwork',
            options={'verbose_name': 'Performing artist', 'verbose_name_plural': 'Performing artists (not mentioned in recordings section)'},
        ),
        migrations.AlterModelOptions(
            name='recording',
            options={'ordering': ('-id',)},
        ),
        migrations.AlterField(
            model_name='recording',
            name='record_label',
            field=models.CharField(blank=True, max_length=60, validators=[music_publisher.base.CWRFieldValidator('first_album_label')]),
        ),
        migrations.AlterField(
            model_name='release',
            name='release_label',
            field=models.CharField(blank=True, max_length=60, validators=[music_publisher.base.CWRFieldValidator('first_album_label')], verbose_name='Release (album) label'),
        ),
        migrations.AddField(
            model_name='release',
            name='library',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='music_publisher.Library'),
        ),
        migrations.RunPython(
            code=import_library_from_settings,
        ),
        migrations.AddField(
            model_name='release',
            name='_release_label',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='music_publisher.Label', verbose_name='Release (album) label'),
        ),
        migrations.AlterField(
            model_name='release',
            name='release_title',
            field=models.CharField(blank=True, max_length=60, null=True, unique=True, validators=[music_publisher.base.CWRFieldValidator('release_title')], verbose_name='Release (album) title '),
        ),
        migrations.RunPython(
            code=release_labels_to_table,
        ),
        migrations.RemoveField(
            model_name='release',
            name='release_label',
        ),
        migrations.RenameField(
            model_name='release',
            old_name='_release_label',
            new_name='release_label',
        ),
        migrations.AlterModelOptions(
            name='label',
            options={'verbose_name_plural': 'Music Labels'},
        ),
        migrations.AlterModelOptions(
            name='library',
            options={'verbose_name_plural': 'Music Libraries'},
        ),
        migrations.AlterModelOptions(
            name='recording',
            options={'verbose_name_plural': '  Recordings'},
        ),
        migrations.AlterField(
            model_name='work',
            name='library_release',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='works', to='music_publisher.LibraryRelease', verbose_name='Library Release'),
        ),
        migrations.AlterModelOptions(
            name='release',
            options={'ordering': ('release_title', 'cd_identifier', '-id')},
        ),
        migrations.AlterModelOptions(
            name='work',
            options={'verbose_name_plural': '   Works'},
        ),
        migrations.AddField(
            model_name='recording',
            name='recording_title_suffix',
            field=models.BooleanField(default=False, help_text='A suffix to the WORK title.'),
        ),
        migrations.AddField(
            model_name='recording',
            name='recording_title',
            field=models.CharField(blank=True, max_length=60, validators=[music_publisher.base.CWRFieldValidator('work_title')]),
        ),
        migrations.AddField(
            model_name='recording',
            name='version_title',
            field=models.CharField(blank=True, max_length=60, validators=[music_publisher.base.CWRFieldValidator('work_title')]),
        ),
        migrations.AddField(
            model_name='recording',
            name='version_title_suffix',
            field=models.BooleanField(default=False, help_text='A suffix to the RECORDING title.'),
        ),
        migrations.AlterField(
            model_name='alternatetitle',
            name='suffix',
            field=models.BooleanField(default=False, help_text='Select if this title is only a suffix to the main title.'),
        ),
        migrations.AlterField(
            model_name='recording',
            name='record_label',
            field=models.ForeignKey(blank=True, null=True,
                                    on_delete=django.db.models.deletion.PROTECT,
                                    to='music_publisher.Label',
                                    verbose_name='Record label'),
        ),
    ]
