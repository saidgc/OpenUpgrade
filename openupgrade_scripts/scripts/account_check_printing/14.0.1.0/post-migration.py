from openupgradelib import openupgrade


@openupgrade.migrate()
def migrate(env, version):
    openupgrade.load_data(
        env.cr, "account_check_printing", "14.0.1.0/noupdate_changes.xml"
    )
