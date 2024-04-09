FROM python:3.8-slim

RUN useradd -u 1000 -ms /bin/bash eureka
USER eureka
WORKDIR /home/eureka

COPY --chown=eureka:eureka a1.txt a1.txt
COPY --chown=eureka:eureka a2.txt a2.txt
COPY --chown=eureka:eureka b b
