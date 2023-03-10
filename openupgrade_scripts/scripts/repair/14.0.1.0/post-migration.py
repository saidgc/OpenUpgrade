# Copyright (C) 2021 Open Source Integrators
# Copyright 2021 ForgeFlow S.L.  <https://www.forgeflow.com>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
from openupgradelib import openupgrade


@openupgrade.migrate()
def migrate(env, version):
    # Load noupdate changes
    openupgrade.load_data(env.cr, "repair", "14.0.1.0/noupdate_changes.xml")
    openupgrade.delete_record_translations(
        env.cr, "repair", ["mail_template_repair_quotation"]
    )
