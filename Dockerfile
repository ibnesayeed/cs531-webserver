FROM    python:alpine

ENV     PYTHONUNBUFFERED=1

WORKDIR /app
ADD     sample/* ./public/

COPY    src/* ./
RUN     chmod +x *.py

CMD     ["./server.py", "0.0.0.0", "80"]
