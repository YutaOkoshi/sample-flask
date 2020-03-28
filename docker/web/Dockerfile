FROM python:3.7.5

ARG app_dir=/app/

# ADD requirements.txt $app_dir

WORKDIR $app_dir

RUN pip install --upgrade pip

COPY flask/requirements.txt .

# 利用するパッケージがかたまるまでコメントアウト
RUN pip install -r requirements.txt

# WSGI HTTP Server ひとまずまGunicornで
CMD ["gunicorn", "main:app", "--config /etc/guni/guniconf.py", "-b", "0.0.0.0:5000"]
