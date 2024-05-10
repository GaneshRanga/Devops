FROM postgres:12-alpine

# Environment variables
ENV POSTGRES_DB=psql_db
ENV POSTGRES_USER=granga401
ENV POSTGRES_PASSWORD=p@ssw0rd

COPY init.sql /docker-entrypoint-initdb.d/

# Expose the PostgreSQL port
EXPOSE 5432

RUN apk --no-cache add postgresql-client \
    && rm -rf /var/cache/apk/*
