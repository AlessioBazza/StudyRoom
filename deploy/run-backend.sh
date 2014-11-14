cd /var/www/backend && \
    source bin/activate && \
    cd /var/www/backend/sito && \
    gunicorn sito.wsgi:application -c sito/gunicorn.conf.py
