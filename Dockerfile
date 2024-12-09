FROM bitnami/python:latest

RUN apt-get update && apt-get install -y curl make

RUN groupadd -r test && \
    useradd -r -g test -m test

WORKDIR /app

COPY . /app

RUN find /app/docs -type f -name "*.md" -delete
RUN rm /app/README.md /app/.gitignore /app/.python-version /app/iv.yaml /app/LICENSE /app/Dockerfile

RUN chown -R test:test /app

USER test

ENV HOME=/home/test
ENV PATH="$HOME/.local/bin:$PATH"

RUN make install

CMD ["make", "test"]