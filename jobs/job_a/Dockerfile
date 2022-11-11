FROM python:3.9-slim

LABEL org.opencontainers.image.source=https://github.com/gbto/pants-default-lock

COPY pex-binaries/job_a /bin

ENTRYPOINT ["/bin/job_a"]
