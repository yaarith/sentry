import logging

from django.db import models
from sentry.db.models import (
    FlexibleForeignKey,
    DefaultFieldsModel,
    JSONField,
)

logger = logging.getLogger(__name__)


class ProjectCodeOwners(DefaultFieldsModel):
    __core__ = False

    project = FlexibleForeignKey("sentry.Project")
    organization_integration = FlexibleForeignKey("sentry.OrganizationIntegration", null=True)
    repository_project_path_config = FlexibleForeignKey("sentry.RepositoryProjectPathConfig")
    # raw ⇒ original CODEOWNERS file.
    raw = models.TextField(null=True)
    # schema ⇒ transformed into IssueOwner syntax
    schema = JSONField(null=True)

    class Meta:
        app_label = "sentry"
        db_table = "sentry_projectcodeowners"