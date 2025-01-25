FROM python:latest

# Set the working directory
WORKDIR /app

# Copy requirements-dev file and install dependencies
COPY requirements-dev.txt .
RUN pip install --no-cache-dir -r requirements-dev.txt

# Copy the application code
COPY ./app ./app

# Expose the application port
EXPOSE 8000

# Create group

ARG UID=1001
ARG GID=1001

# Create group and add GID
RUN addgroup --gid $GID pyappgroup

# Create user and add UID, link group, and assign shell
RUN adduser --uid $UID --ingroup pyappgroup --system pyappuser

# Change ownership of source directory.
RUN chown -R pyappuser:pyappgroup ./app

# Run the FastAPI app
ENTRYPOINT ["python3", "-m", "uvicorn", "app.main:app", "--host=0.0.0.0", "--port=8000"]