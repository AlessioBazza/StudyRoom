FROM ubuntu:14.04

RUN apt-get update && apt-get install -y -q python python-pip python-dev nginx supervisor

# backend setup
RUN mkdir -p /var/www/django-static /var/www/backend
ADD ./backend /var/www/backend
ADD ./settings.overrides.py /var/www/backend/sito/sito/settings/__init__.py
RUN mkdir -p /var/www/django-static
RUN pip install -r /var/www/backend/requirements.txt
RUN python /var/www/backend/sito/manage.py syncdb --noinput
RUN python /var/www/backend/sito/manage.py populate
RUN python /var/www/backend/sito/manage.py collectstatic --noinput

# frontend setup
ADD ./FontEnd /var/www/frontend

# gluing all together
ADD ./nginx.conf /etc/nginx/nginx.conf
ADD ./supervisor.conf /etc/supervisor/conf.d/supervisor.conf

RUN groupadd -r deploy && useradd -r -g deploy deploy
RUN chown -R deploy:deploy /var/www/frontend /var/www/backend \
    /var/www/django-static /var/lib/nginx

EXPOSE 8080
VOLUME ["/tmp"]

CMD ["/usr/bin/supervisord", "--nodaemon"]
