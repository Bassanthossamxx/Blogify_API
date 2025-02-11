
**User Registration, Login, and Google Authentication Documentation**

1. **User Registration**
    - Endpoint: `/register/`
    - Method: `POST`
    - Description: Register a new user.
    - Request Body:
        - `username`: string, required
        - `password`: string, required
        - `email`: string, required
    - Response:
        - `201 Created`: User successfully registered.
        - `400 Bad Request`: Validation errors.

2. **User Login**
    - Endpoint: `/login/`
    - Method: `POST`
    - Description: Login a user.
    - Request Body:
        - `username`: string, required
        - `password`: string, required
    - Response:
        - `200 OK`: User successfully logged in.
        - `401 Unauthorized`: Invalid credentials.

3. **Google Authentication**
    - Endpoint: `/auth/login/google-oauth2/`
    - Method: `GET`
    - Description: Redirect to Google for authentication.
    - Response:
        - Redirects to Google login page.

4. **Google Callback**
    - Endpoint: `/auth/complete/google-oauth2/`
    - Method: `GET`
    - Description: Handle Google authentication callback.
    - Response:
        - `200 OK`: User successfully authenticated with Google.
        - `400 Bad Request`: Authentication failed.

---