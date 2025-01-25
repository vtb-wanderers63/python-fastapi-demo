# python-fast-api-template

This is a basic fastapi Rest API service template

## Create python environment:

```
python3 -m venv venv
```

## Activate environment:

```
source venv/bin/activate
```

## Install dependencies:

```
pip install -r requirements.txt
```

## Githooks

```
python -m python_githooks
```

## Start app

```
fastapi dev app/main.py
```

## Deactivate environment:

```
deactivate
```

Slim python image:

```
docker build -t slim-python-test:v1 -f image-files/normal-distro/slim/Dockerfile .
```

Full python image:

```
docker build -t full-python-test:v1 -f image-files/normal-distro/full/Dockerfile .
```
