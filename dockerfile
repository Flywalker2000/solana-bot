FROM python:3.11-slim-bookworm

WORKDIR /app

# Install runtime deps
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    libgomp1 \
    ca-certificates \
    && rm -rf /var/lib/apt/lists/*

# Build deps pattern
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    gcc \
    python3-dev \
    libssl-dev \
    && pip install --no-cache-dir -r requirements.txt \
    && apt-get remove -y gcc \
    && apt-get autoremove -y \
    && rm -rf /var/lib/apt/lists/*

COPY . .

# Security hardening
RUN useradd -m -d /home/trader trader \
    && chown -R trader:trader /app \
    && chmod 755 docker/entrypoint.sh

USER trader

ENTRYPOINT ["/app/docker/entrypoint.sh"]
