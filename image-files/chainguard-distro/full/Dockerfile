FROM cgr.dev/chainguard/python:latest-dev

# Set the working directory
WORKDIR /app

# Copy requirements-dev file and install dependencies
COPY requirements-dev.txt .
RUN pip install --no-cache-dir -r requirements-dev.txt

# Copy the application code
COPY ./app ./app

# Expose the application port
EXPOSE 8000

# Run the FastAPI app
ENTRYPOINT ["python3", "-m", "uvicorn", "app.main:app", "--host=0.0.0.0", "--port=8000"]