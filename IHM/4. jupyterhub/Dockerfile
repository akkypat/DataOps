FROM python:3.12-slim

WORKDIR /srv/jupyterhub

RUN apt-get update --yes && \
    apt-get install -y --no-install-recommends \
    curl \
    ca-certificates \
    gnupg && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

RUN curl -fsSL https://deb.nodesource.com/setup_20.x | bash - && \
    apt-get update --yes && \
    apt-get install -y --no-install-recommends nodejs && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

RUN npm install -g configurable-http-proxy

RUN pip install --no-cache-dir \
    jupyterhub==4.0.2 \
    jupyterlab==4.0.10 \
    notebook==7.0.7 \
    lakefs-client

RUN useradd -m -s /bin/bash admin

EXPOSE 8000

CMD ["jupyterhub", "-f", "/srv/jupyterhub/jupyterhub_config.py"]
