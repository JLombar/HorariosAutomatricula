FROM bitnami/python:latest

RUN groupadd -r test && \
    useradd -r -g test -m test

USER test

ENV HOME=/home/test
ENV PATH="$HOME/.local/bin:$PATH"

CMD ["make", "test"]
