# Authentication API Documentation

**Base URL:** `https://blogifyapi-production.up.railway.app`

---

## Overview

This document outlines the authentication API endpoints, detailing request payloads, validations, and example requests/responses. It's tailored for Flutter developers to integrate smoothly with backend authentication.

---

## 1. Register User

**POST** `/auth/register/`

**Request Body:**

| Field       | Type   | Required | Validation Details                                                |
| ----------- | ------ | -------- | ----------------------------------------------------------------- |
| username    | String | Yes      | Unique, non-empty                                                 |
| password    | String | Yes      | Minimum 8 characters, must satisfy Django password strength rules |
| email       | String | Yes      | Unique, valid email format                                        |
| phone       | String | Yes      | Valid Egyptian phone number: `+201XXXXXXXX` or `01XXXXXXXX`       |
| first\_name | String | Yes      | Non-empty                                                         |
| last\_name  | String | Yes      | Non-empty                                                         |

**Example Request:**

```json
{
  "username": "john_doe",
  "password": "StrongPass123!",
  "email": "john@example.com",
  "phone": "01012345678",
  "first_name": "John",
  "last_name": "Doe"
}
```

**Success Response (200 OK):**

```json
{
  "message": "Account created successfully!",
  "access": "<JWT access token>",
  "refresh": "<JWT refresh token>"
}
```

**Errors:**

* `400 Bad Request` with detailed validation error messages.

---

## 2. User Login

**POST** `/auth/login/`

**Request Body:**

| Field    | Type   | Required | Validation                    |
| -------- | ------ | -------- | ----------------------------- |
| email    | String | Yes      | Must be registered            |
| password | String | Yes      | Must match registered account |

**Example Request:**

```json
{
  "email": "john@example.com",
  "password": "StrongPass123!"
}
```

**Success Response (200 OK):**

```json
{
  "message": "Login successful!",
  "access": "<JWT access token>",
  "refresh": "<JWT refresh token>"
}
```

**Errors:**

* `400 Bad Request` if required fields are missing.
* `401 Unauthorized` if credentials are invalid.

---

## 3. Logout

**POST** `/auth/logout/`

**Request Body:**

| Field   | Type   | Required | Validation              |
| ------- | ------ | -------- | ----------------------- |
| refresh | String | Yes      | Valid JWT refresh token |

**Example Request:**

```json
{
  "refresh": "<JWT refresh token>"
}
```

**Success Response (200 OK):**

```json
{
  "message": "Logout successful"
}
```

**Errors:**

* `400 Bad Request` if token is missing or invalid.

---

## 4. Generate Token Pair (Login Alternative)

**POST** `/auth/token/`

**Request Body:**

| Field    | Type   | Required | Validation                    |
| -------- | ------ | -------- | ----------------------------- |
| email    | String | Yes      | Must be registered            |
| password | String | Yes      | Must match registered account |

**Example Request:**

```json
{
  "email": "john@example.com",
  "password": "StrongPass123!"
}
```

**Success Response (200 OK):**

```json
{
  "refresh": "<JWT refresh token>",
  "access": "<JWT access token>"
}
```

**Errors:**

* `401 Unauthorized` if credentials are invalid.

---

## 5. Refresh Access Token

**POST** `/auth/token/refresh/`

**Request Body:**

| Field   | Type   | Required | Validation              |
| ------- | ------ | -------- | ----------------------- |
| refresh | String | Yes      | Valid JWT refresh token |

**Example Request:**

```json
{
  "refresh": "<JWT refresh token>"
}
```

**Success Response (200 OK):**

```json
{
  "access": "<new JWT access token>"
}
```
---

**Additional Details:**

* All fields are mandatory unless otherwise stated.
* Phone numbers must be valid Egyptian numbers (`+201XXXXXXXX` or `01XXXXXXXX`).
* Passwords comply with Django’s password validation criteria.
* API returns descriptive error messages with appropriate HTTP status codes for all validation failures.

---
