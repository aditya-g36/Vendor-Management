# Vendor Management system

## Installation

1. Clone the repository:
```
git clone https://github.com/aditya-g36/Vendor_Management-.git
```

2. Navigate to the project directory:
```
cd Vendor_Management--master
```

3. Create and activate a virtual environment :

```
python -m venv env
```

4. Activate the virtual environment:
```
. env/bin/activate
```
On Windows, use 
```env\Scripts\activate```

5. Install the required dependencies:
```
pip install -r requirements.txt
```

6. Set up the database:
```
python manage.py makemigrations

python manage.py migrate
```

7. Create a superuser:
```
python manage.py createsuperuser
```

8. Start the development server:
```
python manage.py runserver
```
# API Endpoints Documentation

## Vendor Management

### POST /api/vendors/
Create a new vendor.

**Example Request (Postman):**

- Method: POST
- URL: http://localhost:8000/api/vendors/
- Headers:
  - Content-Type: application/json
  - Authorization: Token [YOUR_TOKEN]
- Body (raw, JSON):
  ```json
  {
    "name": "Acme Inc.",
    "contact_details": "contact@acme.com, 555-1234",
    "address": "123 Main St, Anytown USA",
    "vendor_code": "ACME001"
  }
  ```

### GET /api/vendors/
List all vendors.

**Example Request (Postman):**

- Method: GET
- URL: http://localhost:8000/api/vendors/
- Headers:
  - Authorization: Token [YOUR_TOKEN]

### GET /api/vendors/{vendor_id}/
Retrieve details of a specific vendor.

**Example Request (Postman):**

- Method: GET
- URL: http://localhost:8000/api/vendors/1/
- Headers:
  - Authorization: Token [YOUR_TOKEN]

### PUT /api/vendors/{vendor_id}/
Update a vendor's details.

**Example Request (Postman):**

- Method: PUT
- URL: http://localhost:8000/api/vendors/1/
- Headers:
  - Content-Type: application/json
  - Authorization: Token [YOUR_TOKEN]
- Body (raw, JSON):
  ```json
  {
    "name": "Acme Inc. (Updated)",
    "contact_details": "updated@acme.com, 555-5678",
    "address": "456 Main St, Anytown USA",
    "vendor_code": "ACME001"
  }
  ```

### DELETE /api/vendors/{vendor_id}/
Delete a vendor.

**Example Request (Postman):**

- Method: DELETE
- URL: http://localhost:8000/api/vendors/1/
- Headers:
  - Authorization: Token [YOUR_TOKEN]

## Purchase Order Management

### POST /api/purchase_orders/
Create a new purchase order.

**Example Request (Postman):**

- Method: POST
- URL: http://localhost:8000/api/purchase_orders/
- Headers:
  - Content-Type: application/json
  - Authorization: Token [YOUR_TOKEN]
- Body (raw, JSON):
  ```json
  {
    "vendor": 1,
    "po_number": "PO001",
    "order_date": "2023-05-01T10:00:00Z",
    "expected_delivery_date": "2023-05-15T10:00:00Z",
    "items": "Product",
    "quantity": 15,
    "status": "Delivered",
    "issue_date": "2023-05-01T10:00:00Z",
    "quality_rating": 5,
    "acknowledgment_date":"2023-05-04T10:00:00Z"
  }
  ```

### GET /api/purchase_orders/
List all purchase orders, with an option to filter by vendor.

**Example Request (Postman):**

- Method: GET
- URL: http://localhost:8000/api/purchase_orders/
- Headers:
  - Authorization: Token [YOUR_TOKEN]
- Query Parameters (optional):
  - vendor=[vendor_id] to filter by vendor

### GET /api/purchase_orders/{po_id}/
Retrieve details of a specific purchase order.

**Example Request (Postman):**

- Method: GET
- URL: http://localhost:8000/api/purchase_orders/1/
- Headers:
  - Authorization: Token [YOUR_TOKEN]

### PUT /api/purchase_orders/{po_id}/
Update a purchase order.

**Example Request (Postman):**

- Method: PUT
- URL: http://localhost:8000/api/purchase_orders/1/
- Headers:
  - Content-Type: application/json
  - Authorization: Token [YOUR_TOKEN]
- Body (raw, JSON):
  ```json
  {
    "vendor": 1,
    "po_number": "PO001",
    "order_date": "2023-05-01T10:00:00Z",
    "expected_delivery_date": "2023-05-20T10:00:00Z",
    "items": "Product",
    "quantity": 25,
    "status": "pending",
    "issue_date": "2023-05-01T10:00:00Z",
    "quality_rating": 5,
    "acknowledgment_date":"2023-05-04T10:00:00Z"
  }
  ```

### DELETE /api/purchase_orders/{po_id}/
Delete a purchase order.

**Example Request (Postman):**

- Method: DELETE
- URL: http://localhost:8000/api/purchase_orders/1/
- Headers:
  - Authorization: Token [YOUR_TOKEN]

## Vendor Performance

### GET /api/vendors/{vendor_id}/performance
Retrieve a vendor's performance metrics.

**Example Request (Postman):**

- Method: GET
- URL: http://localhost:8000/api/vendors/1/performance/
- Headers:
  - Authorization: Token [YOUR_TOKEN]

## Purchase Order Acknowledgment

### POST /api/purchase_orders/{po_id}/acknowledge
Acknowledge a purchase order, updating the acknowledgment_date and triggering the recalculation of average_response_time.

**Example Request (Postman):**

- Method: POST
- URL: http://localhost:8000/api/purchase_orders/1/acknowledge/
- Headers:
  - Authorization: Token [YOUR_TOKEN]

## User Registration and Authentication

### POST /register/
Register a new user and obtain an authentication token.

**Example Request (Postman):**

- Method: POST
- URL: http://localhost:8000/register/
- Headers:
  - Content-Type: application/json
- Body (raw, JSON):
  ```json
  {
    "username": "your_username",
    "password": "your_password"
  }
  ```

**Response:**

```json
{
  "status": 200,
  "payload": {
    "username": "your_username"
  },
  "token": "YOUR_TOKEN",
  "message": "your data is saved"
}
```

#Running Test Suites
To run the test suites for this project, follow these steps:

Activate the virtual environment if not already activated:
bash
Copy code
```source env/bin/activate```  # On Unix/Mac
On Windows, use: ```.\env\Scripts\activate```
Navigate to the project directory containing the manage.py file:
```
cd /path/to/Vendor_Management--master
```
Run the test command:
```
python manage.py test
```

