FROM python:3.9-slim

LABEL maintainer="gibboneto@gmail.com"
LABEL org.opencontainers.image.source=https://github.com/gbto/pants-default-lock

COPY jobs.job_b/main.pex /bin

ENTRYPOINT ["/bin/main.pex"]
