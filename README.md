# Medicine API (Flask)

A simple REST API for managing medicine data.

## Endpoints

- `GET /api/medicines` — Get all medicines
- `GET /api/medicines/<name>` — Get specific medicine
- `GET /api/search?q=...` — Search medicine by name
- `POST /api/medicines` — Add new medicine
- `PUT /api/medicines/<name>` — Update medicine info
- `DELETE /api/medicines/<name>` — Delete medicine

## Run the project
```bash
pip install -r requirements.txt
python run.py
```
