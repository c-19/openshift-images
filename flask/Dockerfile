FROM alpine

RUN apk add --no-cache bash git nginx uwsgi uwsgi-python py2-pip \
	&& pip2 install --upgrade pip \
	&& pip2 install flask

ENV APP_DIR=/app

RUN mkdir ${APP_DIR} \
    && chown -R nginx:nginx ${APP_DIR} \
    && chmod -R 777 /run/ -R \
    && chmod -R 777 /root/ -R

VOLUME [${APP_DIR}]
WORKDIR ${APP_DIR}
COPY files/app.py /app

EXPOSE 5000

COPY files/nginx.conf /etc/nginx/nginx.conf
COPY files/app.ini /app.ini
COPY files/entrypoint.sh /entrypoint.sh
COPY files/app.py /app/app.py

#nginx && uwsgi --ini /app.ini

CMD ["/entrypoint.sh" ]




