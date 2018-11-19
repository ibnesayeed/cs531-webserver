FROM    python:alpine

ENV     PYTHONUNBUFFERED=1

WORKDIR /app
COPY    . ./
RUN     chmod +x *.py *.sh
RUN     ./bootstrap.sh

CMD     ["./server.py", "0.0.0.0", "80"]
