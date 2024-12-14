FROM alpine:latest

RUN apk add --no-cache \
    make \
    curl \
    gcc \
    g++ \
    musl-dev \
    openssl-dev \
    libffi-dev \
    zlib-dev

ENV PYTHON_VERSION=3.13.1

RUN curl -o /tmp/python.tar.xz https://www.python.org/ftp/python/${PYTHON_VERSION}/Python-${PYTHON_VERSION}.tar.xz && \
    mkdir -p /usr/src/python && \
    tar -xf /tmp/python.tar.xz -C /usr/src/python --strip-components=1 && \
    cd /usr/src/python && \
    ./configure && \
    make -j$(nproc) && \
    make altinstall && \
    ln -s /usr/local/bin/python3.13 /usr/local/bin/python3 && \
    ln -s /usr/local/bin/python3.13 /usr/local/bin/python && \
    cd / && \
    rm -rf /usr/src/python /tmp/python.tar.xz

RUN adduser -D -h /home/userTest  userTest && \
    mkdir -p /home/userTest/.cache/uv /app/test && \
    chown -R userTest /home/userTest /app/test

WORKDIR /app/test

COPY Makefile pyproject.toml ./ 

USER userTest

ENV HOME=/home/userTest \
    PATH=/home/userTest/.local/bin:$PATH \
    UV_CACHE_DIR=/home/userTest/.cache/uv

RUN make install
RUN chmod -R a+w /home/userTest/.cache/ && \
    chmod -R a+w /home/userTest/.local

ENTRYPOINT [ "make", "test" ]