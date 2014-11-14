curl -H "Authorization: token ff1cc8bbc1a65f05fc6eca3a8492828d8a604153" \
    -L https://api.github.com/repos/mickfenneck/studyroom/tarball \
    | tar zxvf - --strip-components=1 --directory /home/user/code

chown -R user:user /home/user/code/
su -c "cd /home/user/code/backend/sito && \
    python manage.py syncdb --noinput && \
    python manage.py populate" user

/usr/bin/supervisord --nodaemon
