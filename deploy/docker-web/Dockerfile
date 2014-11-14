FROM ubuntu:14.04
RUN apt-get update && apt-get install -y supervisor python python-pip python-dev vim zip curl

RUN groupadd user && useradd -ms /bin/bash -g user user && mkdir -p /home/user/code

RUN curl -H "Authorization: token ff1cc8bbc1a65f05fc6eca3a8492828d8a604153" \
    -L https://api.github.com/repos/mickfenneck/studyroom/tarball \
    | tar zxvf - --strip-components=1 --directory /home/user/code

RUN pip install -r /home/user/code/backend/requirements.txt
RUN cd /home/user/code/backend/sito && \
    python manage.py syncdb --noinput && \
    python manage.py populate
RUN chown -R user:user /home/user/code

RUN mkdir -p /var/log/supervisor
ADD web.conf /etc/supervisor/conf.d/web.conf

EXPOSE 8000
VOLUME ["/var/log/supervisor"]
CMD ["/usr/bin/supervisord", "--nodaemon"]
