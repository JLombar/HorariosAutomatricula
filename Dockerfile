FROM alpine:latest

RUN apk add --no-cache \
    make \
    curl \
    shadow \
    ca-certificates \
    gcc \
    g++ \
    musl-dev \
    openssl-dev \
    libffi-dev \
    zlib-dev

ENV PYTHON_VERSION=3.12.0

RUN curl -o /tmp/python.tar.xz https://www.python.org/ftp/python/${PYTHON_VERSION}/Python-${PYTHON_VERSION}.tar.xz && \
    mkdir -p /usr/src/python && \
    tar -xf /tmp/python.tar.xz -C /usr/src/python --strip-components=1 && \
    cd /usr/src/python && \
    ./configure --enable-optimizations && \
    make -j$(nproc) && \
    make altinstall && \
    cd / && \
    rm -rf /usr/src/python /tmp/python.tar.xz

RUN python3.12 --version

RUN mkdir -p /home/userTest /app/test /home/userTest/.cache/

WORKDIR /app/test

RUN groupadd groupTest && \
    useradd -g groupTest userTest && \
    mkdir -p /home/userTest /app/test /home/userTest/.cache/uv && \
    chown -R userTest:groupTest /home/userTest /app/test /home/userTest/.cache/uv

COPY Makefile pyproject.toml ./ 

USER userTest

ENV HOME=/home/userTest \
    PATH=/home/userTest/.local/bin:$PATH \
    UV_CACHE_DIR=/home/userTest/.cache/uv

RUN make install
ENTRYPOINT [ "make", "test" ]
