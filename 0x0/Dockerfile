FROM python:3.10

WORKDIR /app

COPY . /app

RUN apt-get update
RUN apt-get -y install cron

# Files cleanup cronjob
RUN crontab -l | { cat; echo "0 2 * * * /app/cleanup.py"; } | crontab -

RUN pip install --no-cache-dir -r requirements.txt

CMD flask db upgrade; \
	uwsgi --socket 0.0.0.0:8080 --wsgi-file fhost.py --callable app --processes 4 --threads 2
