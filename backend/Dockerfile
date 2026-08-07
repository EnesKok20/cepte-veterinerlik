# ---- builder: bağımlılıkları uv ile çöz ve kur ----
FROM python:3.12-slim AS builder

RUN pip install --no-cache-dir uv==0.12.2

WORKDIR /app

ENV UV_COMPILE_BYTECODE=1 \
    UV_LINK_MODE=copy

# Önce sadece lock dosyalarını kopyalayıp bağımlılıkları kur — app kodu
# değiştiğinde bu katman cache'ten gelsin diye (Docker layer caching)
COPY pyproject.toml uv.lock ./
RUN uv sync --frozen --no-dev --no-install-project

COPY app ./app
RUN uv sync --frozen --no-dev

# ---- runtime: sadece çalışması için gerekenler ----
FROM python:3.12-slim AS runtime

RUN groupadd --system appuser && \
    useradd --system --gid appuser --no-create-home --shell /usr/sbin/nologin appuser

WORKDIR /app

COPY --from=builder /app/.venv /app/.venv
COPY --from=builder /app/app /app/app

ENV PATH="/app/.venv/bin:$PATH" \
    PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1

USER appuser

EXPOSE 8000

HEALTHCHECK --interval=30s --timeout=5s --start-period=10s --retries=3 \
    CMD python -c "import urllib.request; urllib.request.urlopen('http://127.0.0.1:8000/')" || exit 1

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
