# 🛒 Rubel Mart API

A modern, scalable, and production-ready E-Commerce Backend built with **FastAPI**, **PostgreSQL**, **SQLAlchemy**, and **Alembic**.

Rubel Mart is designed to power a complete online shopping platform with secure authentication, product management, order processing, payment integration, inventory management, and administrative tools.

---

## 🚀 Features

### Authentication & Authorization

- User Registration
- User Login
- JWT Authentication
- Role-Based Access Control (RBAC)
- Password Hashing with Bcrypt
- Email Verification
- Password Reset

### User Management

- User Profiles
- Address Management
- Account Verification
- Customer & Admin Roles

### Product Management

- Product Catalog
- Categories
- Brands
- Product Images
- Inventory Tracking
- Product Variants

### Order Management

- Shopping Cart
- Wishlist
- Order Placement
- Order Tracking
- Order History

### Reviews & Ratings

- Product Reviews
- Product Ratings
- Customer Feedback

### Administration

- Dashboard Analytics
- User Management
- Product Management
- Order Management
- Inventory Management

### Infrastructure

- FastAPI
- PostgreSQL
- SQLAlchemy ORM
- Alembic Database Migrations
- Docker Support
- Environment Configuration
- Structured Logging
- Global Exception Handling
- Request Validation
- CORS Configuration

---

## 🏗️ Project Structure

```bash
app/
├── api/
│   ├── router.py
│   └── v1/
│
├── core/
│   ├── config.py
│   ├── database.py
│   ├── lifespan.py
│   └── logger.py
│
├── exceptions/
│   ├── api_exception.py
│   ├── handlers.py
│   └── __init__.py
│
├── middleware/
│   └── cors.py
│
├── models/
├── repositories/
├── services/
├── schemas/
├── utils/
│
└── main.py
```

---

## ⚙️ Tech Stack

| Technology | Purpose            |
| ---------- | ------------------ |
| FastAPI    | Backend Framework  |
| PostgreSQL | Database           |
| SQLAlchemy | ORM                |
| Alembic    | Database Migration |
| Pydantic   | Data Validation    |
| JWT        | Authentication     |
| Docker     | Containerization   |
| Uvicorn    | ASGI Server        |

---

## 🔧 Environment Variables

Create a `.env` file:

```env
APP_NAME=Rubel Mart API
APP_VERSION=1.0.0
APP_ENV=development

HOST=0.0.0.0
PORT=5000

DATABASE_URL=postgresql://username:password@localhost:5432/rubel_mart_db

JWT_SECRET=your-secret-key

FRONTEND_URL=http://localhost:3000
```

---

## 🐳 Docker

Build Docker Image:

```bash
docker build -t rubel-mart-api .
```

Run Container:

```bash
docker run -p 5000:5000 rubel-mart-api
```

---

## 🗄️ Database Migration

Create Migration:

```bash
alembic revision --autogenerate -m "create users table"
```

Apply Migration:

```bash
alembic upgrade head
```

Rollback Migration:

```bash
alembic downgrade -1
```

---

## ▶️ Running Locally

Install Dependencies:

```bash
pip install -r requirements.txt
```

Run Development Server:

```bash
python run.py
```

API Documentation:

```text
http://localhost:5000/docs
```

ReDoc:

```text
http://localhost:5000/redoc
```

---

## 📡 API Response Format

### Success Response

```json
{
  "message": "Operation successful",
  "success": true,
  "status_code": 200,
  "data": {}
}
```

### Error Response

```json
{
  "message": "Validation failed",
  "success": false,
  "status_code": 422,
  "data": {
    "errors": [
      {
        "field": "email",
        "message": "Email is required"
      }
    ]
  }
}
```

---

## 🔒 Security

- Password Hashing (Bcrypt)
- JWT Authentication
- Input Validation
- CORS Protection
- Environment-Based Configuration
- Structured Exception Handling

---

## 👨‍💻 Author

**Md. Mohin Uddin Rubel**

Backend Developer | Full Stack Developer

Building scalable and production-ready web applications using modern technologies.

---

## 📄 License

This project is proprietary software. All rights reserved.
© Rubel Mart
