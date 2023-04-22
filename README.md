## UniShortener

simple Django powered url shortener

---

### Technologies
- `Django` 4.2
- `gunicorn` as wsgi
- `nginx` as reverse proxy and static files server

### Production Setup
1. Clone this repo.
2. Generate `.env` config file and change config values (`DB_PATH`).
```
python3 generate_dotenv.py
```
3. Run docker container.
```
sudo docker compose up -d
```

### Dev Setup
1. Clone this repo.
2. Generate `.env` config file.
```
python3 generate_dotenv.py
```
3. Change `DEBUG` in `.env` to `1`

### Commands
- enable / reset 2FA for user
```
python3 manage.py enable_2fa_for_user -u <username>
```
