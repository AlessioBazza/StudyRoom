Backend Guide
===

### Installation Guide
1.  Clone the repository
```
emilio@emilio-notebook:~$ git clone git@github.com:mickfenneck/StudyRoom.git
Cloning into 'StudyRoom'...
remote: Counting objects: 22, done.
remote: Compressing objects: 100% (16/16), done.
remote: Total 22 (delta 0), reused 19 (delta 0)
Receiving objects: 100% (22/22), done.
Checking connectivity... done.
emilio@emilio-notebook:~$ 
```

2. Create the virtualenv:
```
emilio@emilio-notebook:~$ cd StudyRoom/backend/
emilio@emilio-notebook:~/StudyRoom/backend$ virtualenv .
New python executable in ./bin/python
Installing setuptools, pip...done.
emilio@emilio-notebook:~/StudyRoom/backend$ 
```

3. Install the requirements:
```
emilio@emilio-notebook:~/StudyRoom/backend$ source bin/activate
emilio@emilio-notebook:~/StudyRoom/backend$ pip install -r requirements.txt 
Downloading/unpacking Django==1.7.1 (from -r requirements.txt (line 1))
Downloading Django-1.7.1-py2.py3-none-any.whl (7.4MB): 7.4MB downloaded
Requirement already satisfied (use --upgrade to upgrade): argparse==1.2.1 in /usr/lib/python2.7 (from -r requirements.txt (line 2))
Requirement already satisfied (use --upgrade to upgrade): wsgiref==0.1.2 in /usr/lib/python2.7 (from -r requirements.txt (line 3))
Installing collected packages: Django
Successfully installed Django
Cleaning up...
emilio@emilio-notebook:~/StudyRoom/backend$ 
```
