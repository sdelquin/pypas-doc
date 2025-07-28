FROM python:3.13
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/
ADD . /code
WORKDIR /code
RUN uv sync
CMD ["mkdocs", "build"]
