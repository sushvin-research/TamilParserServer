### Tamil Parser Server

#### Requirements

- Python >= 3.10

#### Installation

```bash
pip install -r requirements.py
```

#### Production

```bash
uvicorn main:app --host 0.0.0.0 --port 8000 --reload 
```

Open [http://localhost:8000](http://localhost:8000) with your browser to see the result.

#### PM2 Host

```shell
pm2 start "gunicorn -w 4 -k uvicorn.workers.UvicornWorker main:app" --name TamilParserServer
```

```shell
pm2 start "uvicorn main:app --host 0.0.0.0 --port 8000 --workers 4" --name TamilParserServer
```