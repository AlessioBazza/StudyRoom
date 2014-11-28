FROM jmarin/supervisor
MAINTAINER Emilio Dorigatti <emilio.dorigatti@gmail.com>

RUN yum -y localinstall \
    http://yum.postgresql.org/9.3/redhat/rhel-7-x86_64/pgdg-centos93-9.3-1.noarch.rpm
RUN yum -y install postgis2_93 postgresql93-contrib postgresql93-server python \
    python-pip python-devel nginx supervisor gcc postgresql-libs postgresql-devel vim; \
    yum clean all

RUN rm -Rf /var/lib/pgsql/9.3/data

# database setup
ENV PGDATA /var/lib/pgsql/9.3/data
USER postgres
RUN /usr/pgsql-9.3/bin/initdb --encoding=utf8
RUN /usr/pgsql-9.3/bin/pg_ctl start && sleep 1 && \
    createuser -d -s -r -l django && \
    psql postgres -c "ALTER USER django WITH ENCRYPTED PASSWORD 'django'" && \
    createdb django -O django && \
    /usr/pgsql-9.3/bin/pg_ctl stop

USER root
RUN echo "host django  django    127.0.0.1/32  md5" >> /var/lib/pgsql/9.3/data/pg_hba.conf
RUN echo "listen_addresses = '127.0.0.1'"   >> /var/lib/pgsql/9.3/data/postgresql.conf
RUN echo "port = 5432"                      >> /var/lib/pgsql/9.3/data/postgresql.conf
RUN echo "log_statement='all'"              >> /var/lib/pgsql/9.3/data/postgresql.conf 
RUn echo "log_directory='/tmp/'"            >> /var/lib/pgsql/9.3/data/postgresql.conf

# backend setup
RUN mkdir -p /var/www/backend/static
ADD ./backend/sito /var/www/backend/sito
ADD ./backend/requirements.txt /var/www/backend/requirements.txt
RUN pip install -r /var/www/backend/requirements.txt
ADD ./settings.overrides.py /var/www/backend/sito/sito/settings/__init__.py
RUN python /var/www/backend/sito/manage.py collectstatic --noinput
RUN su postgres -c "/usr/pgsql-9.3/bin/pg_ctl start" && sleep 1 && \
    python /var/www/backend/sito/manage.py syncdb --noinput && \
    python /var/www/backend/sito/manage.py populate && \
    su postgres -c "/usr/pgsql-9.3/bin/pg_ctl stop"

RUN groupadd -r backend && useradd -r \
    -g backend \
    -d /var/www/backend \
    -s /sbin/nologin \
    backend

RUN chown -R backend:backend /var/www/backend

ADD ./nginx.conf /etc/nginx/nginx.conf
ADD ./supervisor.conf /etc/supervisor/conf.d/

EXPOSE 8080
VOLUME /var/lib/pgsql/9.3/data
CMD ["supervisord", "-c", "/etc/supervisor/supervisor.conf"]
