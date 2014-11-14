FROM ubuntu:14.04
RUN apt-get update && apt-get install -y supervisor python python-pip python-dev vim zip curl

RUN groupadd user && \
    useradd -ms /bin/bash -g user user && \
    mkdir -p /home/user/code && \
    chown -R user:user /home/user/code

RUN curl -H "Authorization: token ff1cc8bbc1a65f05fc6eca3a8492828d8a604153" \
    -L https://raw.githubusercontent.com/mickfenneck/StudyRoom/master/backend/requirements.txt \
    -o /tmp/requirements.txt && pip install -r /tmp/requirements.txt


RUN mkdir -p /var/log/supervisor
ADD web.conf /etc/supervisor/conf.d/web.conf
ADD startup.sh /opt/startup.sh

EXPOSE 8000
VOLUME ["/var/log/supervisor"]
CMD ["/bin/sh", "/opt/startup.sh"]
