### Example .env for Development

```ini
APIKEY="SOME SECRET"
```

### In Bash to Set Variable to Environment

```bash
set -a; source .env; set +a
```

## Production Run

```bash
gunicorn -w 4 --bind 0.0.0.0:5000 wsgi:app
```

## Development Run

```bash
python app.py
```

## Build Docker Image

```bash
sudo docker build -t <account>/<repository>:<tag> .
sudo docker push <account>/<repository>:<tag>
```
