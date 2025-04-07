# Blogify API

A robust blogging platform REST API built with Django Rest Framework and JWT authentication, allowing users to create, view, and comment on posts with proper access control for editing.

### You can find the API documentation in Postman here: [Blogify_API](https://documenter.getpostman.com/view/37742819/2sB2cVeMSP)

## Features

- **JWT Authentication**: Secure token-based authentication with refresh capabilities
- **Social Authentication**: Google OAuth2 integration for simplified login
- **Custom User Model**: Extended user model with additional fields like phone number
- **Post Management**: Create, read, update, and delete blog posts
- **Comment System**: Add and manage comments on posts
- **Permission Controls**: Author-based permissions for content modification
- **Egyptian Phone Validation**: Custom validator for Egyptian phone numbers
- **Slug Generation**: Auto-generated slugs for SEO-friendly URLs
- **Token Blacklisting**: Security feature for proper logout functionality

## Tech Stack

- **Django 5.1**: Web framework
- **Django REST Framework**: API toolkit
- **SimpleJWT**: JWT authentication
- **Social Auth**: Google OAuth2 integration via python-social-auth
- **SQLite**: Database (can be easily switched to other databases)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/Blogify_API.git
   cd Blogify_API
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up environment variables:
   Create a `.env` file in the project root with:
   ```
   SECRET_KEY=your_secret_key
   SOCIAL_AUTH_GOOGLE_OAUTH2_KEY=your_google_oauth_key
   SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET=your_google_oauth_secret
   ```

5. Run migrations:
   ```bash
   python manage.py migrate
   ```

6. Create a superuser:
   ```bash
   python manage.py createsuperuser
   ```

7. Run the development server:
   ```bash
   python manage.py runserver
   ```

## API Documentation

### Authentication Endpoints

| Endpoint | Method | Description | Request Body | Response |
|----------|--------|-------------|-------------|----------|
| `/auth/register/` | POST | Register a new user | `username`, `password`, `email`, `phone`, `first_name`, `last_name` | JWT tokens |
| `/auth/login/` | POST | Login existing user | `email`, `password` | JWT tokens |
| `/auth/logout/` | POST | Logout user | `refresh` token | Success message |
| `/auth/token/` | POST | Get JWT tokens | `email`, `password` | Access and refresh tokens |
| `/auth/token/refresh/` | POST | Refresh JWT token | `refresh` token | New access token |

### Social Authentication Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/auth/social/login/google-oauth2/` | GET | Initiate Google OAuth login flow |
| `/auth/social/complete/google-oauth2/` | GET | OAuth callback URL for Google |

For more fine-grained control:
- `/auth/google/login/` - Custom endpoint that redirects to Google auth
- `/auth/google/callback/` - Custom endpoint for handling Google callbacks

### Blog Endpoints

| Endpoint | Method | Description | Authentication | Permissions |
|----------|--------|-------------|----------------|------------|
| `/api/post/` | GET | List all posts | Optional | All users |
| `/api/post/` | POST | Create new post | Required | Authenticated users |
| `/api/post/{slug}/` | GET | Get post details | Optional | All users |
| `/api/post/{slug}/` | PUT/PATCH | Update post | Required | Post author only |
| `/api/post/{slug}/` | DELETE | Delete post | Required | Post author only |
| `/api/comment/` | GET | List all comments | Optional | All users |
| `/api/comment/` | POST | Create comment | Required | Authenticated users |
| `/api/comment/{id}/` | GET | Get comment details | Optional | All users |
| `/api/comment/{id}/` | PUT/PATCH | Update comment | Required | Comment author only |
| `/api/comment/{id}/` | DELETE | Delete comment | Required | Comment author only |

## URL Structure

The application uses a clean URL structure with route registration through Django's URL patterns:

```python
urlpatterns = [
    path('auth/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('auth/register/', RegisterView.as_view(), name='register'),
    path('auth/login/', LoginView.as_view(), name='login'),
    path('auth/logout/', LogoutView.as_view(), name='logout'),
    path('auth/social/', include('social_django.urls', namespace='social')),
    path('api/', include(route.urls)),
]
```

API routes are automatically registered using Django REST Framework's DefaultRouter:

```python
route = DefaultRouter()
route.register(r'post', PostsViewSet, basename="post")
route.register(r'comment', CommentsViewSet, basename="comment")
```

## Models

### CustomUser
- `username`: Username for the user
- `email`: Email address (used as login identifier)
- `first_name`: User's first name
- `last_name`: User's last name
- `phone`: Egyptian phone number with validator

### Post
- `title`: Post title
- `content`: Post content
- `created_at`: Creation timestamp
- `updated_at`: Last update timestamp
- `author`: User who created the post
- `slug`: SEO-friendly URL path (auto-generated)

### Comment
- `content`: Comment text
- `created_at`: Creation timestamp
- `updated_at`: Last update timestamp
- `author`: User who created the comment
- `post`: Associated post

## Authentication Flow

### Regular Authentication
1. Register with required user details
2. Login with email and password
3. Receive JWT access and refresh tokens
4. Use access token in Authorization header as "Bearer {token}"
5. Refresh token when expired

### Google OAuth Authentication

#### Method 1: Social Django Integration
1. Navigate to `/auth/social/login/google-oauth2/`
2. Complete Google authentication
3. Redirected back to your application
4. Authenticated session created

#### Method 2: Custom Integration
1. Call `/auth/google/login/` to get Google authorization URL
2. Redirect user to Google for authentication
3. Google redirects to your callback URL with authorization code
4. Call `/auth/google/callback/` with the code
5. Receive JWT tokens for authenticated session

##### Sample Social Auth Configuration:
```python
AUTHENTICATION_BACKENDS = (
    'social_core.backends.google.GoogleOAuth2',
    'django.contrib.auth.backends.ModelBackend',
)

SOCIAL_AUTH_GOOGLE_OAUTH2_SCOPE = [
    'https://www.googleapis.com/auth/userinfo.email',
    'https://www.googleapis.com/auth/userinfo.profile',
    'openid',
]
```

## Error Handling

The API returns appropriate HTTP status codes with error messages:
- `400 Bad Request`: Invalid input data
- `401 Unauthorized`: Authentication failure
- `403 Forbidden`: Permission denied
- `404 Not Found`: Resource not found



## Setting Up Google OAuth

1. Create a project in the [Google Developer Console](https://console.developers.google.com/)
2. Enable the Google+ API
3. Create OAuth credentials
4. Set authorized JavaScript origins to `http://localhost:8000`
5. Set authorized redirect URIs to `http://localhost:8000/auth/social/complete/google-oauth2/`
6. Add your client ID and secret to the `.env` file

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

