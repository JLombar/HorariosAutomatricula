FROM ghcr.io/astral-sh/uv:python3.13-alpine

RUN apk add --no-cache make

WORKDIR /app/test

RUN adduser -D -h /home/userTest userTest

USER userTest

RUN mkdir -p /home/userTest/.cache/ && \
    chmod -R a+w /home/userTest/.cache/

ENV UV_CACHE_DIR=/home/userTest/.cache/uv

ENTRYPOINT ["make", "test"]