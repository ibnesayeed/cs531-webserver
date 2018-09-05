FROM python:alpine

COPY server.py /
RUN  chmod a+x /server.py

CMD ["/server.py", "0.0.0.0", "80"]
