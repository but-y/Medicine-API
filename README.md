# Medicine API (Flask)
![Language](https://img.shields.io/badge/Language-Python-blue)
![Platform](https://img.shields.io/badge/Platform-Android-a4c639)
![Format](https://img.shields.io/badge/Data-JSON-orange)
![Status](https://img.shields.io/badge/Status-Active-brightgreen)


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
