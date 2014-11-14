rm -rf /var/www/frontend

mkdir /tmp/code
curl -H "Authorization: token ff1cc8bbc1a65f05fc6eca3a8492828d8a604153" \
    -L https://api.github.com/repos/mickfenneck/studyroom/tarball \
    | tar zxvf - --strip-components=1 --directory /tmp/code

sudo mv /tmp/code/FontEnd /var/www/frontend
rm -rf /tmp/code
