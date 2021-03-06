# Django-blog-example

## Inroduction 

- [Django](https://www.djangoproject.com/)
- [PostgreSQL](https://www.postgresql.org/)
- [Bootstrap](https://getbootstrap.com/)
- [Editor.js](https://editorjs.io/) : Block styled editor
- [django-editorjs-fields](https://github.com/2ik/django-editorjs-fields) : Django plugin for using Editor.js
- [DISQUS](https://disqus.com/)

위의 사항들을 이용해서 블로그를 만들었습니다. 글 작성은 admin페이지에서 가능하도록 django-editorjs-fields 플러그 인을 사용했습니다. JSON으로 표현된 글을 HTML로 바꾸기 위해서는 Javascript를 사용했습니다. 현재 변환이 가능한 타입은 

- paragraph
- Image
- Header
- List

입니다. 파일 `/mysite/blog/templates/blog/post_detail.html`을 확인하면 자세한 구현을 확인할 수 있습니다. nginx,gunicorn,aws lightsail을 사용해서 배포했습니다. ([참고 자료 링크](https://www.digitalocean.com/community/tutorials/how-to-set-up-django-with-postgres-nginx-and-gunicorn-on-ubuntu-18-04))

```
http://15.164.135.64/
```

## Installing Dependencies

### Virtual Enviornment

We recommend working within a virtual environment. Instructions for setting up a virtual enviornment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/).

On macOS and Linux:

```bash
python3 -m pip install --user virtualenv
python3 -m venv env
source env/bin/activate
```

On Windows:

```
py -m pip install --user virtualenv
py -m venv env
.\env\Scripts\activate
```

### PIP Dependencies

Once you have your virtual environment setup and running, install dependencies by running:

```bash
pip install -r requirements.txt
```

This will install all of the required packages we selected within the `requirements.txt` file.

## Database Setup

From the folder in terminal run

On macOS and Linux:

```bash
export SECRET_KEY='secret_key'
export DEBUG=True
export DATABASE_NAME='database_name'
export DATABASE_USER='database_user'
export DATABASE_PASSWORD='database_password'
export DATABASE_HOST='localhost'
export DISQUS_SHORTNAME='disqus_shortname'
export DISQUS_MY_DOMAIN='disqus_my_domain'
python3 manage.py migrate
```

## Running the server

From within the app directory first ensure you are working using your created virtual environment.

To run the server, execute:

```bash
export SECRET_KEY='secret_key'
export DEBUG=True
export DATABASE_NAME='database_name'
export DATABASE_USER='database_user'
export DATABASE_PASSWORD='database_password'
export DATABASE_HOST='localhost'
export DISQUS_SHORTNAME='disqus_shortname'
export DISQUS_MY_DOMAIN='disqus_my_domain'
python3 manage.py runserver
```