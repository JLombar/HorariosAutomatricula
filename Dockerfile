FROM bitnami/python:latest

RUN apt-get update

RUN groupadd -r test && \
    useradd -r -g test -m test

WORKDIR /app

COPY . /app

RUN chown -R test:test /app

USER test

ENV HOME=/home/test
ENV PATH="$HOME/.local/bin:$PATH"

RUN make install

CMD ["make", "test"]
