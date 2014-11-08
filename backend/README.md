Backend Guide
===

### Installation Guide
1.  Clone the repository
  ```
~$ git clone git@github.com:mickfenneck/StudyRoom.git
  ```

2. Create the virtualenv:
  ```
~$ cd StudyRoom/backend/
~/StudyRoom/backend$ virtualenv .
  ```

3. Install the requirements:
  ```
~/StudyRoom/backend$ source bin/activate
~/StudyRoom/backend$ pip install -r requirements.txt 
  ```

4. Create the database and load developement data (optional)
  ```
~/StudyRoom/backend$ cd sito/
~/StudyRoom/backend/sito$ python manage.py syncdb
~/StudyRoom/backend/sito$ python manage.py popolate
  ```
