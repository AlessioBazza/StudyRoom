#Appunti sul Deployment

### Connessione al server remoto
1. Sono necessarie le chiavi ssh per accedere (`studyroom-keypair.pem`)
2. L'hostname è `ec2-54-148-53-189.us-west-2.compute.amazonaws.com` oppure, `studyroom.noip.me`
3. `ssh -i studyroom_keypair.pem studyroom.noip.me`
4. nome utente del server: `ubuntu`

### Clonare il repo
```
git clone https://ff1cc8bbc1a65f05fc6eca3a8492828d8a604153@github.com/mickfenneck/StudyRoom.git
```

### Procedura automatica per effettuare il deploy
Gli script appositi sono presenti in `/home/ubuntu/deploy-*`, per lanciarli da remoto:
 - Frontend: `ssh -i studyroom_keypair.pem ubuntu@studyroom.noip.me /home/ubuntu/deploy-frontend.sh`
 - Backend: `ssh -i studyroom_keypair.pem ubuntu@studyroom.noip.me /home/ubuntu/deploy-backend.sh`

#Varie
####Nginx
1. Fermare nginx: `sudo nginx -s stop`
2. Far partire nginx: `sudo nginx`
3. Ricaricare la configurazione di nginx: `sudo nginx -s reload`
4. File di configurazione: `/etc/nginx/nginx.conf`
5. File di log: `/tmp/nginx.access.log`, `/tmp/nginx.error.log`, `/tmp/nginx.pid`

####Supervisor
1. Stato del backend: `sudo supervisorctl status backend`
2. Fermare il backend: `sudo supervisorctl stop backend`
3. Far partire il backend: `sudo supervisorctl start backend`
4. File di configurazione del backend: `/etc/supervisor/conf.d/backend.conf `
5. File di log: `/var/log/supervisor/supervisord.log`

####Backend
1. Directory: `/var/www/backend`
2. File statici di django: `/var/www/django-static`
3. Attivare il virtualenv: `source /var/www/backend/bin/activate` (`deactivate` per uscire)
4. Fermare gunicorn: `kill -QUIT $(cat /tmp/gunicorn.pid)`
5. Lanciare gunicorn: `cd /var/www/backend/sito/ && /var/www/backend/bin/gunicorn sito.wsgi:application -c sito/gunicorn.conf.py`
6. File di log: `/tmp/gunicorn.access.log`, `/tmp/gunicorn.error.log`

####Frontend
1. Directory: `/var/www/frontend`
2. basta.
