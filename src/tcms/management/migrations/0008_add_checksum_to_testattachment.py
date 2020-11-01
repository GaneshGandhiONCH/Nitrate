# Generated by Django 3.0.7 on 2020-10-31 08:42

import logging
import os

from django.db import migrations, models

from tcms.core.utils import checksum
from tcms.management.models import attachment_stored_filename

logger = logging.getLogger(__name__)


def calculate_uploaded_files_checksum(apps, schema_editor):
    TestAttachment = apps.get_model('management', 'TestAttachment')
    for attachment in TestAttachment.objects.all():
        stored_filename = attachment_stored_filename(attachment.stored_name)
        if not os.path.exists(stored_filename):
            logger.info('Server side stored file %s does not exist.',
                        stored_filename)
            continue
        with open(stored_filename, 'rb') as f:
            attachment.checksum = checksum(f.read())
        attachment.save(update_fields=['checksum'])


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0007_remove_max_length_from_authfield'),
    ]

    operations = [
        migrations.AddField(
            model_name='testattachment',
            name='checksum',
            field=models.CharField(default='', help_text='MD5 checksum of this uploaded file.', max_length=32),
            preserve_default=False,
        ),
        migrations.RunPython(
            calculate_uploaded_files_checksum,
            migrations.RunPython.noop
        )
    ]
