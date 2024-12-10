FROM bitnami/python:latest

WORKDIR /app/test

COPY Makefile pyproject.toml /app/test

ENV HOME=/home/test
ENV PATH="$HOME/.local/bin:$PATH"

RUN make install

RUN groupadd -r test && \
    useradd -r -g test -m test

USER test

ENTRYPOINT ["make", "test"]
