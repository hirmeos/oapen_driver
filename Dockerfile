FROM python:3.9

WORKDIR /usr/src/app
RUN mkdir output cache
VOLUME ["/usr/src/app/output", "/usr/src/app/cache"]

COPY ./src/* ./

CMD ["./run"]