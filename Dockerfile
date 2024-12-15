FROM ghcr.io/astral-sh/uv:python3.13-alpine

RUN apk add --no-cache make

WORKDIR /app/test

RUN --mount=type=bind,source=uv.lock,target=uv.lock \
    --mount=type=bind,source=pyproject.toml,target=pyproject.toml \
    uv sync --frozen --no-install-project --no-dev

RUN adduser -D -h /home/userTest userTest

USER userTest

COPY Makefile pyproject.toml uv.lock ./ 

ENV UV_CACHE_DIR=/home/userTest/.cache/uv

RUN uv sync --frozen && \
    chmod -R a+w /home/userTest/.cache/

ENTRYPOINT ["make", "test"]