
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('case', '0003_alter_case_case_status'),
    ]

    operations = [
        migrations.RunSQL(
            """
            CREATE OR REPLACE VIEW case_view AS
            SELECT
                c.id as id,
                c.assigned_worker_id,
                w.name AS assigned_worker_name,
                c.debtor_id,
                d.name AS debtor_name,
                c.case_status,
                c.borrowed_amount,
                c.payment_frequency,
                c.interest_rate,
                c.amortization_period,
                c.created_at
            FROM debtors.case c
            LEFT JOIN worker w ON c.assigned_worker_id = w.id
            LEFT JOIN worker d ON c.debtor_id = d.id;
            """
        ),
    ]
