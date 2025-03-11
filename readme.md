# RepaySync API Documentation

*March 10, 2025*

---

## Table of Contents
1. [Introduction](#1-introduction)
2. [Base URL](#2-base-url)
3. [Authentication Endpoints](#3-authentication-endpoints)
4. [Users Endpoints](#4-users-endpoints)
5. [Customers Endpoints](#5-customers-endpoints)
6. [Loans Endpoints](#6-loans-endpoints)
7. [Interactions Endpoints](#7-interactions-endpoints)
8. [Logs Endpoints](#8-logs-endpoints)
9. [Common Headers](#9-common-request-and-response-headers)
10. [Error Handling](#10-error-handling)
11. [Summary Table of Endpoints](#11-summary-table-of-endpoints)
12. [Additional Notes](#12-additional-notes)

---

## 1. Introduction
This document provides comprehensive documentation for the RepaySync backend API. The API includes endpoints for authentication, user management, customer management, loan management, interactions (field and calling), and logs. **All endpoints (except authentication and registration) require a valid JWT in the `Authorization` header.**

---

## 2. Base URL

http://127.0.0.1:8000/



## 3 Authentication Endpoints

### 3.1 Obtain JWT Tokens

*   **URL:** `/api/auth/token/`
*   **Method:** `POST`
*   **Description:** Authenticate with username and password to receive an access token and
    refresh token.
*   **Headers:**
    *   `Content-Type`: `application/json`
*   **Request Body:**

    ```json
    {
      "username": "your_username",
      "password": "your_password"
    }
    ```

*   **Response:**

    ```json
    {
      "access": "eyJ0eXAiOiJKV1QiLCJh...",
      "refresh": "eyJ0eXAiOiJKV1QiLCJh..."
    }
    ```

### 3.2 Refresh JWT Access Token

*   **URL:** `/api/auth/token/refresh/`
*   **Method:** `POST`
*   **Description:** Exchange a valid refresh token for a new access token.
*   **Headers:**
    *   `Content-Type`: `application/json`
*   **Request Body:**

    ```json
    {
      "refresh": "your_refresh_token"
    }
    ```

*   **Response:**

    ```json
    {
      "access": "new_access_token"
    }
    ```

## 4 Users Endpoints

### 4.1 Register New User

*   **URL:** `/api/users/register/`
*   **Method:** `POST`
*   **Description:** Register a new user (e.g., calling agent, collection officer, manager).
*   **Headers:**
    *   `Content-Type`: `application/json`
*   **Request Body:**

    ```json
    {
      "username": "johndoe",
      "email": "john@example.com",
      "role": "calling_agent",
      "manager": null,
      "password": "SomePassword123"
    }
    ```

*   **Response:** Returns the newly created user's details.

### 4.2 List All Users

*   **URL:** `/api/users/`
*   **Method:** `GET`
*   **Description:** Retrieve a list of all registered users.
*   **Headers:**
    *   `Authorization`: `Bearer <access_token>`
*   **Response:**

    ```json
    [
      {
        "id": 1,
        "username": "johndoe",
        "email": "john@example.com",
        "role": "calling_agent",
        "manager": null
      },
      {
        "id": 2,
        "username": "janedoe",
        "email": "jane@example.com",
        "role": "collection_officer",
        "manager": 1
      }
    ]
    ```

## 5 Customers Endpoints

### 5.1 List & Create Customers

*   **URL:** `/api/customers/`
*   **Methods:** `GET`, `POST`
*   **Description:**
    *   `GET`: List customers assigned to the logged-in user. (If the user is a calling agent, all
        customers are listed.)
    *   `POST`: Create a new customer.
*   **Headers:**
    *   `Authorization`: `Bearer <access_token>`
*   **GET Response:**

    ```json
    [
      {
        "id": 1,
        "customer_code": "A1B2C3D4",
        "name": "John Doe",
        "phone": "+91-9876543210",
        "email": "john@example.com",
        "assigned_collection_officer": 2,
        "address_line_1": "123 Main St",
        "address_line_2": "Apt 4B",
        "city": "Kolkata",
        "state": "WB",
        "pincode": "700001",
        "date_of_birth": "1990-01-01"
      }
    ]
    ```

*   **POST Request Body:**

    *Note: Set customer_code to null or omit it to auto-generate.*

    ```json
    {
      "customer_code": "OptionalValueOrNull",
      "name": "John Doe",
      "phone": "+91-9876543210",
      "email": "john@example.com",
      "assigned_collection_officer": 2,
      "address_line_1": "123 Main St",
      "address_line_2": "Apt 4B",
      "city": "Kolkata",
      "state": "WB",
      "pincode": "700001",
      "date_of_birth": "1990-01-01"
    }
    ```

*   **POST Response:** Returns the created customer details.

### 5.2 Create a Single Customer

*   **URL:** `/api/customers/create/`
*   **Method:** `POST`
*   **Description:** A dedicated endpoint for creating a single customer record.
*   **Headers:** Authorization header as above.
*   **Request Body:** Same as in Section 3.1.

### 5.3 Retrieve/Update/Delete Customer

*   **URL:** `/api/customers/<int:id>/`
*   **Methods:** `GET`, `PUT/PATCH`, `DELETE`
*   **Description:** Retrieve, update, or delete a specific customer.
*   **Headers:** Authorization header as above.
*   **Example Update Request Body:**

    ```json
    {
      "name": "John Doe Updated",
      "phone": "+91-9123456789"
    }
    ```

### 5.4 Bulk Upload Customers

*   **URL:** `/api/customers/bulk/upload/`
*   **Method:** `POST`
*   **Description:** Upload a CSV file to create multiple customers at once.
*   **Headers:**
    *   `Authorization`: `Bearer <access_token>`
    *   `Content-Type`: `multipart/form-data` (file field named `file`)
*   **CSV Requirements:** Columns: `customer_code` (optional), `name`, `phone`, `email`, `address_line_1`,
    `address_line_2`, `city`, `state`, `pincode`, `date_of_birth`.
*   **Response:**

    ```json
    {
      "records_created": 10,
      "errors": []
    }
    ```

## 6 Loans Endpoints

### 6.1 List & Create Loans

*   **URL:** `/api/loans/`
*   **Methods:** `GET`, `POST`
*   **Description:**
    *   `GET`: List all loans.
    *   `POST`: Create a new loan.
*   **Headers:** Authorization header as above.
*   **POST Request Body:**

    ```json
    {
      "loan_account_number": "LN12345",
      "principal_amount": "50000.00",
      "interest_rate": "10.50",
      "loan_type": "personal",
      "tenure_months": 12,
      "loan_date": "2025-03-09",
      "customer": 1
    }
    ```

*   **Response:** Returns the created loan object.

### 6.2 Retrieve/Update/Delete Loan

*   **URL:** `/api/loans/<int:id>/`
*   **Methods:** `GET`, `PUT/PATCH`, `DELETE`
*   **Headers:** Authorization header as above.
*   **Example Update Request Body:**

    ```json
    {
      "principal_amount": "75000.00",
      "tenure_months": 24
    }
    ```

### 6.3 Retrieve All Loans for a Particular Customer

*   **URL:** `/api/loans/customer/<int:customer_id>/`
*   **Method:** `GET`
*   **Description:** Retrieve all loans associated with a specific customer.
*   **Headers:** Authorization header as above.
*   **Response:**

    ```json
    [
      {
        "id": 1,
        "loan_account_number": "LN12345",
        "principal_amount": "50000.00",
        "interest_rate": "10.50",
        "loan_type": "personal",
        "tenure_months": 12,
        "loan_date": "2025-03-09",
        "customer": 1
      },
      {
        "id": 2,
        "loan_account_number": "LN67890",
        "principal_amount": "75000.00",
        "interest_rate": "11.00",
        "loan_type": "home",
        "tenure_months": 36,
        "loan_date": "2025-04-15",
        "customer": 1
      }
    ]
    ```

## 7 Interactions Endpoints

Interactions are divided into Field and Calling types.

### 7.1 Field Interactions

#### 7.1.1 Create Field Interaction

*   **URL:** `/api/interactions/field/create/`
*   **Method:** `POST`
*   **Description:** Create a new field interaction.
*   **Headers:** Authorization header as above.
*   **Request Body:**

    ```json
    {
      "loan": 1,
      "comment": "Visited customer; discussed repayment plan.",
      "disposition": "visited",
      "next_call_date": "2025-03-15"
    }
    ```

*   **Response:** Returns the created interaction.

#### 7.1.2 Retrieve/Update/Delete Field Interaction

*   **URL:** `/api/interactions/field/<int:id>/`
*   **Methods:** `GET`, `PUT/PATCH`, `DELETE`
*   **Headers:** Authorization header as above.

#### 7.1.3 List Field Interactions for a Loan

*   **URL:** `/api/interactions/field/loan/<int:loan_id>/`
*   **Method:** `GET`
*   **Response:**

    ```json
    [
      {
        "id": 1,
        "loan": 1,
        "comment": "Visited customer; discussed repayment plan.",
        "disposition": "visited",
        "timestamp": "2025-03-09T10:30:00Z",
        "next_call_date": "2025-03-15",
        "created_by": 2,
        "interaction_type": "field"
      }
    ]
    ```

### 7.2 Calling Interactions

#### 7.2.1 Create Calling Interaction

*   **URL:** `/api/interactions/calling/create/`
*   **Method:** `POST`
*   **Description:** Create a new calling interaction.
*   **Headers:** Authorization header as above.
*   **Request Body:**

    ```json
    {
      "loan": 1,
      "comment": "Called customer to remind about due payment.",
      "disposition": "called",
      "next_call_date": "2025-03-20"
    }
    ```

#### 7.2.2 Retrieve/Update/Delete Calling Interaction

*   **URL:** `/api/interactions/calling/<int:id>/`
*   **Methods:** `GET`, `PUT/PATCH`, `DELETE`
*   **Headers:** Authorization header as above.

#### 7.2.3 List Calling Interactions for a Loan

*   **URL:** `/api/interactions/calling/loan/<int:loan_id>/`
*   **Method:** `GET`
*   **Response:** An array of calling interactions.

### 7.3 Bulk Upload Interactions

*   **URL:** `/api/interactions/bulk/upload/`
*   **Method:** `POST`
*   **Description:** Upload a CSV file to create multiple interactions at once.
*   **Headers:**
    *   `Authorization`: `Bearer <access_token>`
    *   `Content-Type`: `multipart/form-data` (file field named `file`)
*   **CSV Requirements:** Columns: `loan_id`, `comment`, `disposition`, `next_call_date`, (optional) `interaction_type` (default is "field").
*   **Response:**

    ```json
    {
      "records_created": 5,
      "errors": []
    }
    ```

## 8 Logs Endpoints

### 8.1 List API Logs

*   **URL:** `/api/logs/`
*   **Method:** `GET`
*   **Description:** Retrieve a list of API logs (for monitoring and debugging).
*   **Headers:** `Authorization: Bearer <access_token>` (admin user only).
*   **Response:**

    ```json
    [
      {
        "id": 1,
        "user": 2,
        "method": "GET",
        "endpoint": "/api/customers/",
        "request_payload": "",
        "response_payload": "[{...}]",
        "status_code": 200,
        "created_at": "2025-03-09T10:45:00Z"
      }
    ]
    ```

## 9 Common Request and Response Headers

*   **Authentication Header**

    `Authorization`: `Bearer <access_token>`

*   **Content-Type**
    *   For JSON requests: `application/json`
    *   For CSV uploads: `multipart/form-data` (with a field named `file`)

## 10 Error Handling

**HTTP Status Codes**

*   `200 OK`: Successful GET, PUT/PATCH, DELETE operations.
*   `201 Created`: Successful POST operations.
*   `400 Bad Request`: Validation or parsing errors.
*   `401 Unauthorized`: Missing or invalid JWT.
*   `403 Forbidden`: Insufficient permissions.
*   `404 Not Found`: Resource does not exist.
*   `500 Internal Server Error`: Server-side issues.

**Error Response Format**

Errors are returned as JSON, for example:

```json
{
  "error": "No file provided."
}

 ```
or
```json
{
  "errors": {
    "name": ["This field is required."]
  }
}
 
```

## 11 Summary Table of Endpoints


| **Category**            | **Endpoint**                                 | **Method**              | **Description**                                         |
|-------------------------|----------------------------------------------|-------------------------|---------------------------------------------------------|
| Auth                    | `/api/auth/token/`                           | POST                    | Obtain JWT tokens                                       |
| Auth                    | `/api/auth/token/refresh/`                   | POST                    | Refresh JWT token                                       |
| Users                   | `/api/users/register/`                       | POST                    | Register a new user                                     |
| Users                   | `/api/users/`                                | GET                     | List all users                                          |
| Customers               | `/api/customers/`                            | GET, POST               | List (assigned) customers / Create a customer           |
| Customers               | `/api/customers/create/`                     | POST                    | Create a single customer                                |
| Customers               | `/api/customers/bulk/upload/`                | POST                    | Bulk upload customers via CSV                           |
| Customers               | `/api/customers/<int:id>/`                   | GET, PUT/PATCH, DELETE  | Retrieve/Update/Delete a customer                       |
| Loans                   | `/api/loans/`                                | GET, POST               | List all loans / Create a loan                          |
| Loans                   | `/api/loans/<int:id>/`                       | GET, PUT/PATCH, DELETE  | Retrieve/Update/Delete a loan                           |
| Loans                   | `/api/loans/customer/<int:customer_id>/`     | GET                     | List all loans for a specific customer                  |
| Interactions (Field)    | `/api/interactions/field/create/`            | POST                    | Create a field interaction                              |
| Interactions (Field)    | `/api/interactions/field/<int:id>/`          | GET, PUT/PATCH, DELETE  | Retrieve/Update/Delete a field interaction              |
| Interactions (Field)    | `/api/interactions/field/loan/<int:loan_id>/`| GET                     | List field interactions for a loan                      |
| Interactions (Calling)  | `/api/interactions/calling/create/`          | POST                    | Create a calling interaction                            |
| Interactions (Calling)  | `/api/interactions/calling/<int:id>/`        | GET, PUT/PATCH, DELETE  | Retrieve/Update/Delete a calling interaction            |
| Interactions (Calling)  | `/api/interactions/calling/loan/<int:loan_id>/` | GET                  | List calling interactions for a loan                    |
| Interactions (Bulk)     | `/api/interactions/bulk/upload/`             | POST                    | Bulk upload interactions via CSV                        |
| Logs                    | `/api/logs/`                                 | GET                     | List all API logs (admin only)                          |



## 12 Additional Notes

*   Most endpoints require an Authorization header: `Bearer <access_token>`.
*   For CSV uploads, use `multipart/form-data` with a file field named `file`.
*   Custom permissions are applied to restrict access based on user roles (e.g., calling agents vs. field officers).
*   Error responses are returned in JSON format with appropriate HTTP status codes.