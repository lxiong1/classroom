FROM python:3.10

COPY . .

RUN ./scripts/install_deps.sh

ENTRYPOINT ./scripts/run_server.sh
