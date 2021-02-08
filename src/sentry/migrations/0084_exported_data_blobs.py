# Generated by Django 1.11.29 on 2020-06-03 01:15

from django.db import migrations
import django.db.models.deletion
import sentry.db.models.fields.bounded
import sentry.db.models.fields.foreignkey


class Migration(migrations.Migration):
    # This flag is used to mark that a migration shouldn't be automatically run in
    # production. We set this to True for operations that we think are risky and want
    # someone from ops to run manually and monitor.
    # General advice is that if in doubt, mark your migration as `is_dangerous`.
    # Some things you should always mark as dangerous:
    # - Large data migrations. Typically we want these to be run manually by ops so that
    #   they can be monitored. Since data migrations will now hold a transaction open
    #   this is even more important.
    # - Adding columns to highly active tables, even ones that are NULL.
    is_dangerous = False

    # This flag is used to decide whether to run this migration in a transaction or not.
    # By default we prefer to run in a transaction, but for migrations where you want
    # to `CREATE INDEX CONCURRENTLY` this needs to be set to False. Typically you'll
    # want to create an index concurrently when adding one to an existing table.
    atomic = True

    dependencies = [
        ("sentry", "0083_add_max_length_webhook_url"),
    ]

    operations = [
        migrations.CreateModel(
            name="ExportedDataBlob",
            fields=[
                (
                    "id",
                    sentry.db.models.fields.bounded.BoundedBigAutoField(
                        primary_key=True, serialize=False
                    ),
                ),
                ("offset", sentry.db.models.fields.bounded.BoundedBigIntegerField()),
                (
                    "blob",
                    sentry.db.models.fields.foreignkey.FlexibleForeignKey(
                        db_constraint=False,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="sentry.FileBlob",
                    ),
                ),
                (
                    "data_export",
                    sentry.db.models.fields.foreignkey.FlexibleForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="sentry.ExportedData"
                    ),
                ),
            ],
            options={
                "db_table": "sentry_exporteddatablob",
            },
        ),
        migrations.AlterUniqueTogether(
            name="exporteddatablob",
            unique_together={("data_export", "blob", "offset")},
        ),
    ]
