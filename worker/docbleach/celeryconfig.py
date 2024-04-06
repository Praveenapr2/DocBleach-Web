# Same TTL as Plik
result_expires = 12 * 3600
task_reject_on_worker_lost = True
# celeryconfig.py
CELERY_RESULT_BACKEND  = 'redis://redis/'
CELERY_DEFAULT_EXCHANGE = 'reply.celery.pidbox'
CELERY_DEFAULT_ROUTING_KEY = '_kombu.binding.reply.celery.pidbox'
CELERY_BROKER_URL = 'redis://redis/'
