supervisorctl stop backend

rm -rf /var/www/backend /var/www/django-static

mkdir /tmp/code /var/www/django-static
curl -H "Authorization: token ff1cc8bbc1a65f05fc6eca3a8492828d8a604153" \
    -L https://api.github.com/repos/mickfenneck/studyroom/tarball \
    | tar zxvf - --strip-components=1 --directory /tmp/code

mv /tmp/code/backend /var/www/backend
cd /var/www/backend && \
    virtualenv . && \
    /var/www/backend/bin/pip install -r requirements.txt;

cd /var/www/backend/sito && \
    echo "from prod import *; SECRET_KEY='temp'" > sito/settings/__init__.py && \
    /var/www/backend/bin/python manage.py syncdb --noinput && \
    /var/www/backend/bin/python manage.py populate && \
    /var/www/backend/bin/python manage.py collectstatic --noinput

rm -rf /tmp/code
chown -R ubuntu:ubuntu /var/www/backend

supervisorctl start backend

echo "****************"
echo "***  make sure to change the default secret key in sito/settings/__init__.py!!!"
echo "****************"
