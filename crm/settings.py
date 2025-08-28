INSTALLED_APPS += ['django_crontab']

CRONJOBS = [
    ('*/5 * * * *', 'crm.cron.log_crm_heartbeat'),
]
INSTALLED_APPS = [
    # ...
    'django_crontab',
]
CRONJOBS = [
    ('*/5 * * * *', 'crm.cron.log_crm_heartbeat'),
]
CRONJOBS = [
    ('0 */12 * * *', 'crm.cron.update_low_stock'),
]
CRONJOBS = [
    ('*/5 * * * *', 'crm.cron.log_crm_heartbeat'),  # existing heartbeat job
    ('0 */12 * * *', 'crm.cron.update_low_stock'),
]
