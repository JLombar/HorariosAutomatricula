FROM ubuntu:latest

RUN apt-get update && apt-get install -y make curl

RUN mkdir -p /home/userTest /app/test /home/userTest/.cache/

WORKDIR /app/test

RUN groupadd groupTest && useradd -g groupTest userTest && \
    chown -R userTest:groupTest /app/test && \
    chown -R userTest:groupTest /home/userTest

COPY Makefile pyproject.toml ./ 

USER userTest

ENV HOME=/home/userTest \
    PATH=/home/userTest/.local/bin:$PATH \
    UV_CACHE_DIR=/home/userTest/.cache/uv

RUN make install
ENTRYPOINT [ "executable" ] [ "make", "test" ]
