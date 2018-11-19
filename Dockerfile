FROM python:alpine

ENV  PYTHONUNBUFFERED=1

COPY server.py /
RUN  chmod a+x /server.py

CMD ["/server.py", "0.0.0.0", "80"]
