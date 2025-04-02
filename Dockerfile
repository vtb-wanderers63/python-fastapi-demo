FROM python:latest as base
WORKDIR /base
COPY ./requirements.txt .
RUN python -m venv venv
ENV PATH='/base/venv/bin:$PATH'
RUN pip install --no-cache-dir -r requirements.txt
####
FROM python:slim
WORKDIR /app
RUN apt-get update && apt-get install -y --no-install-recommends \
    bash \
    && rm -rf /var/lib/apt/lists/*
ARG UID=1001
ARG GID=1001
RUN addgroup --gid $GID pyappgroup && adduser --uid $UID --ingroup pyappgroup --system pyappuser
COPY --from=base /base/venv ./venv
ENV PATH='/app/venv/bin:$PATH'
COPY --chown=pyappuser:pyappgroup app app
####
ENV PORT=8080
EXPOSE 8080
####
ENTRYPOINT ["python","-m","uvicorn" ,"app.main:app" ,"--host", "0.0.0.0", "--port", "8000", "--workers", "4"]