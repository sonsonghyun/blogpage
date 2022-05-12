FROM python:3.10.0

WORKDIR /home/

RUN git clone https://github.com/sonsonghyun/blog.git

WORKDIR /home/blog/

RUN pip install -r requirements.txt

RUN echo "SECRET_KEY = django-insecure-&d6=&*6@jcjr3fvns@h5rhi_lw)(ea(0t%tjmx)_484-vl#j&l" > .env

RUN python manage.py migrate

EXPOSE 8000

CMD ["python","manage.py","runserver","0.0.0.0:8000"]