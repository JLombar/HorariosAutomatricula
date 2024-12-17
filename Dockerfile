FROM ghcr.io/astral-sh/uv:python3.13-alpine

RUN apk add --no-cache make

WORKDIR /app/test

RUN mkdir -p /app/test/.venv && \
    chmod -R a+w /app/test/.venv

RUN adduser -D -h /home/userTest userTest

USER userTest

ENV UV_CACHE_DIR=/home/userTest/.cache/uv

RUN --mount=type=bind,source=uv.lock,target=uv.lock \
    --mount=type=bind,source=pyproject.toml,target=pyproject.toml \
    uv sync --frozen --no-install-project --no-dev && \
    chmod -R a+w /home/userTest/.cache/

ENTRYPOINT ["make", "test"]