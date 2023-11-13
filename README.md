# learn-fastAPI-user-service
Repository for the User Service of the Online Marketplace project. This service is primarily aimed at exploring the capabilities of FastAPI, along with pytest for testing, and understanding microservices architecture. The service may contain dummy data and is not intended for production use.

# Basic Requirements
1. **User Registration**:
    - Allow new users to create an account using their email/username and password.
    - Validate email addresses to ensure they are in the correct format and are unique.
    - Send a confirmation email upon successful registration.
2. **Authentication**:
    - Enable users to log in and log out.
    - Implement JWT (JSON Web Tokens) for secure, token-based user authentication.
    - Provide password recovery and reset functionality.
3. **Profile Management**:
    - Allow users to view and update their profile information.
    - Include an endpoint to allow users to view their purchase history. [order service]

# Tech Used
- DataBase : Postgres 
- ORM : Tortoise
- JWT : pyjwt
- Framework : fastAPI
