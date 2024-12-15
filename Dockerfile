FROM ghcr.io/astral-sh/uv:python3.13-alpine

RUN apk add --no-cache make

WORKDIR /app/test

RUN --mount=type=bind,source=uv.lock,target=uv.lock \
    --mount=type=bind,source=pyproject.toml,target=pyproject.toml \
    uv sync --frozen --no-install-project --no-dev

COPY Makefile pyproject.toml uv.lock ./ 

RUN uv sync --frozen

ENV UV_CACHE_DIR=/home/userTest/.cache/uv

RUN mkdir -p /home/userTest/.cache/uv /app/test && \
    chmod -R a+w /home/userTest /app/test && \
    adduser -D -h /home/userTest userTest

USER userTest

ENTRYPOINT ["make", "test"]