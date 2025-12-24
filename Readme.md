# Company & Employee Management API

A robust RESTful API built with **Django** and **Django REST Framework (DRF)** to manage corporate entities and their workforce efficiently.

## 🚀 Features
* **Company Management:** Create, Update, and View company profiles with categorized types (IT, Non-IT, Mobile).
* **Workforce Tracking:** Manage employee records linked to specific companies via Foreign Key relationships.
* **Custom Endpoints:** Specific route to fetch all employees belonging to a single company.
* **Standardized Responses:** API configured to deliver high-performance **JSON** payloads.

## 🛠️ Tech Stack
* **Framework:** Django 5.2
* **API Toolkit:** Django REST Framework (DRF)
* **Database:** SQLite3
* **Language:** Python 3.x

## 🛣️ API Endpoints
| Endpoint | Method | Description |
| :--- | :--- | :--- |
| `/companies/` | `GET` / `POST` | List all companies or create a new one. |
| `/companies/{id}/` | `GET` / `PUT` | Retrieve or update a specific company. |
| `/companies/{id}/employees/` | `GET` | **Custom:** List all employees of a specific company. |
| `/employees/` | `GET` / `POST` | List all employees or create a new one. |

## ⚙️ Installation & Setup
1. **Clone the repository:**
   ```bash
   git clone [https://github.com/Vaibhav0117/companyAPI.git](https://github.com/Vaibhav0117/companyAPI.git)
   cd companyAPI

2. Create a Virtual Environment:

Bash

python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
Install Dependencies:

Bash

pip install django djangorestframework
Apply Migrations:

Bash

python manage.py makemigrations
python manage.py migrate
Run the Server:

Bash

python manage.py runserver