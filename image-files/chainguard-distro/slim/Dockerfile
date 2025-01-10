FROM python:latest as base
 
WORKDIR /dev-app
 
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY ./app ./app

# lint and test
# FROM base as lint-and-test

# RUN ""

# RUN ""

# build
# FROM test as build
# RUN ""

# prod package installations
FROM base as prod-dependency-installations

WORKDIR /prod-app

RUN python -m venv venv

COPY requirements.txt .
RUN ./venv/bin/pip install --no-cache-dir -r requirements.txt

FROM python:slim
WORKDIR /app

COPY --from=prod-dependency-installations /prod-app/venv ./venv

ENV PATH="/app/venv/bin:$PATH"

# Copy the application code
COPY ./app ./app
 
# Expose the application port
EXPOSE 8000

# Run the FastAPI app
ENTRYPOINT ["python3", "-m", "uvicorn", "app.main:app", "--host=0.0.0.0", "--port=8000"]