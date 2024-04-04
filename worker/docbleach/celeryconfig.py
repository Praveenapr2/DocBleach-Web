# Same TTL as Plik
result_expires = 12 * 3600
task_reject_on_worker_lost = True
# celeryconfig.py
broker_url = 'redis://localhost:6379/0'
result_backend = 'redis://localhost:6379/0'
