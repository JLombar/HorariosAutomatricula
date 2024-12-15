FROM python:3.13.1-alpine3.21

RUN apk add --no-cache make

WORKDIR /app/test

RUN adduser -D -h /home/userTest userTest && \
    chown userTest:userTest /app/test

USER userTest

COPY Makefile pyproject.toml ./

RUN mkdir -p /home/userTest/.cache/uv /app/test

ENV PATH=/home/userTest/.local/bin:$PATH \
    UV_CACHE_DIR=/home/userTest/.cache/uv

RUN make install && \
    chmod -R a+w /home/userTest/.cache/

ENTRYPOINT [ "make", "test" ]