# This is needed because we need to accept bytes objects we can be serialized by pickle only
CELERY_ACCEPT_CONTENT = ['pickle', 'json', 'msgpack', 'yaml']