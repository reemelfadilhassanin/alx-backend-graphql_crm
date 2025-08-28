#!/bin/bash
LOG_FILE="/tmp/customer_cleanup_log.txt"
TIMESTAMP=$(date +"%Y-%m-%d %H:%M:%S")

DELETED_COUNT=$(python3 manage.py shell <<EOF
from crm.models import Customer
from django.utils import timezone
from datetime import timedelta

one_year_ago = timezone.now() - timedelta(days=365)
inactive_customers = Customer.objects.filter(order__isnull=True, created_at__lt=one_year_ago)
count = inactive_customers.count()
inactive_customers.delete()
print(count)
EOF
)

echo "$TIMESTAMP - Deleted $DELETED_COUNT inactive customers" >> "$LOG_FILE"
