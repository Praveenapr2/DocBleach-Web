# Same TTL as Plik
result_expires = 12 * 3600
task_reject_on_worker_lost = True
# celeryconfig.py
result_backend = 'redis://172.19.0.2:6379/0'
CELERY_DEFAULT_EXCHANGE = 'reply.celery.pidbox'
CELERY_DEFAULT_ROUTING_KEY = '_kombu.binding.reply.celery.pidbox'
CELERY_BROKER_URL = 'redis://172.19.0.2:6379/0'
