# Product Management

Django product management app with full CRUD (add, view, edit, delete), Django templates, image uploads, and a REST API built with Django REST Framework.

## Features

| Feature | Page | API |
|---|---|---|
| List products | `/products/` | `GET /api/products/` |
| Add product | `/products/add/` | `POST /api/products/` |
| View product | `/products/<id>/` | `GET /api/products/<id>/` |
| Edit product | `/products/<id>/edit/` | `PUT` / `PATCH /api/products/<id>/` |
| Delete product | `/products/<id>/delete/` | `DELETE /api/products/<id>/` |

## Product model

| Field | Type |
|---|---|
| name | CharField |
| image | ImageField |
| description | TextField |
| price | DecimalField |
| created_at | DateTimeField |
| updated_at | DateTimeField |

## Setup

```bash
git clone https://github.com/kingdamie/product-management.git
cd product-management
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Open http://127.0.0.1:8000/products/

Optional: `python manage.py createsuperuser` to use the admin at `/admin/`.

## Notes

- Uploaded images are stored in `media/` (ignored by git).
- Prices are formatted in naira (e.g. ₦30,000) by `products/static/products/js/main.js`.
- When uploading through the API, send `multipart/form-data`, not JSON.
