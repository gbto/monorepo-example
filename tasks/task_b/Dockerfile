FROM python:3.9-slim

LABEL maintainer="gibboneto@gmail.com"
LABEL org.opencontainers.image.source=https://github.com/gbto/monorepo-example

COPY pex-binaries/task_b /bin

ENTRYPOINT ["/bin/task_b"]
