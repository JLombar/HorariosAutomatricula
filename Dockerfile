FROM python:3.12-alpine3.20

RUN apk add --no-cache make curl

RUN addgroup -S groupTest && \
    adduser -D -h /home/userTest -G groupTest userTest && \
    mkdir -p /home/userTest/.cache/uv /app/test && \
    chown -R userTest:groupTest /home/userTest /app/test

WORKDIR /app/test

COPY Makefile pyproject.toml ./

USER userTest

ENV HOME=/home/userTest \
    PATH=/home/userTest/.local/bin:$PATH \
    UV_CACHE_DIR=/home/userTest/.cache/uv

RUN make install

ENTRYPOINT [ "make", "test" ]
