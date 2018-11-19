FROM python:alpine

ENV  PYTHONUNBUFFERED=1

COPY server.py bootstrap.sh /
RUN  chmod +x /server.py /bootstrap.sh
RUN  /bootstrap.sh

CMD ["/server.py", "0.0.0.0", "80"]
