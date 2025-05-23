# EZTest
****Overview****

This project implements a Secure File Sharing System designed to facilitate safe, controlled access and sharing of files between two user roles:

Ops User: Manages file uploads and permissions.

Client User: Accesses only files explicitly shared with them.

The system provides RESTful APIs to handle user authentication, file management, and secure downloads, ensuring strict access control and security compliance.

****Features****
Role-based access control:

Ops Users can upload files and share them with specific Client Users.

Client Users can download files only if shared with them.

Secure file storage and retrieval.

User authentication and authorization.

File metadata management.

Clear error responses for unauthorized or invalid operations.

****API Endpoints****

**User Authentication**
POST /auth/login
Login endpoint for both Ops and Client users.

**File Management (Ops User only)**
POST /files
Upload a new file.

POST /files/{file_id}/share
Share a file with specific Client Users.

GET /files
List files owned or uploaded by Ops User.

File Access (Client User only)
GET /files/shared
List files shared with the Client User.

GET /files/{file_id}/download
Download a file if shared with the requesting Client User.

****Installation****

Clone the repository:

git clone https://github.com/yourusername/secure-file-sharing.git
cd secure-file-sharing

Create and activate a virtual environment:

python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows

Install dependencies:

pip install -r requirements.txt

Configure environment variables (e.g., database URL, secret keys).

Run database migrations (if applicable):

# Example with Alembic or Django manage.py

Start the server:

python app.py

****Usage****
Use the login endpoint to authenticate as either Ops User or Client User.

Ops Users can upload files and share them with Client Users.

Client Users can view and download only files shared with them.

