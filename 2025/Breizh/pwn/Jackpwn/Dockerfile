# Build stage
FROM debian:bookworm AS builder

RUN apt-get update && apt-get install -y build-essential

COPY jackpwn.c /
RUN gcc -g /jackpwn.c -o /jackpwn


# Final stage
FROM registry.ctf.bzh/breizh/breizh-ctf-2025/challenge/docker/tcp

COPY --chown=root:root --chmod=0555 --from=builder /jackpwn /challenge/challenge

USER challenge
WORKDIR /challenge/

ENV FLAG=BZHCTF{fake_flag}
