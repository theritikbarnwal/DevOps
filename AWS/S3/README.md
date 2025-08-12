***

# R3cloud - A Personal Cloud Storage Platform

R3cloud is a web-based cloud storage application designed to provide a secure and scalable platform for file storage and management. Built with a Python Flask backend and integrated with Amazon Web Services (AWS), this project serves as a practical exploration of modern web development and cloud infrastructure.

The application allows users to register, log in, and upload files, which are securely stored in an AWS S3 bucket.

## Core Features

*   **Secure User Authentication:** Complete user registration, login, and logout functionality. Passwords are securely hashed using `pbkdf2:sha256`.
*   **Token-Based Password Reset:** A secure flow for users to reset forgotten passwords via temporary, expiring tokens.
*   **File Upload to S3:** Direct integration with AWS S3. Uploaded files are streamed from the user, through the Flask server, and into a designated S3 bucket.
*   **Dynamic Dashboard:** A user-facing dashboard that will display file information and storage metrics.
*   **Centralized Configuration:** All sensitive credentials (database URIs, AWS keys) are managed securely outside the source code using an `.env` file.

## Tech Stack

*   **Backend:** Python, Flask
*   **Database:** MongoDB
*   **Cloud Storage:** Amazon S3 (Simple Storage Service)
*   **AWS SDK:** Boto3 for Python
*   **Frontend:** HTML, CSS (with Jinja2 templating)
*   **Security:** Werkzeug for password hashing

## Current Status & Future Roadmap

This project is currently in active development as I continue to explore and learn more about AWS services.

### **What Works Now:**
*   A complete user authentication system is in place.
*   Any registered user can successfully upload files.
*   All uploaded files are saved directly to the configured AWS S3 bucket.

### **Limitations & Next Steps:**
The current implementation is a foundational proof-of-concept. The immediate next steps are focused on building out core user-centric features:

*   **User-Specific File Storage:** The highest priority is to implement logic that associates uploads with the specific user who uploaded them. This will involve creating user-specific folders or using metadata within S3 to ensure users can only access their own files.
*   **File Access & Management:** Add functionality for users to view, download, and delete their own files from the dashboard.
*   **Storage Metrics:** Enhance the dashboard to accurately reflect each user's personal storage usage.

This iterative development process is part of the journey of learning and mastering cloud services.

## Local Setup and Installation

To run this project locally, follow these steps:

1.  **Clone the repository:**
    ```bash
    git clone 
    cd 
    ```

2.  **Create a virtual environment:**
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Configure Environment Variables:**
    *   Create a file named `.env` in the root of the project.
    *   Populate it with your credentials as shown below.

5.  **Run the application:**
    ```bash
    python app.py
    ```

## Configuration

Create a `.env` file in the project's root directory and add the following configuration variables.

```
# Flask Secret Key for session management
FLASK_SECRET_KEY="your_strong_random_secret_key"

# MongoDB Credentials
MONGO_USERNAME="your_mongo_username"
MONGO_PASSWORD="your_mongo_password"
MONGO_CLUSTER="your_mongo_cluster_url"
MONGO_DATABASE="your_database_name"
MONGO_COLLECTION="your_collection_name"

# AWS S3 Credentials
AWS_ACCESS_KEY_ID="your_iam_access_key"
AWS_SECRET_ACCESS_KEY="your_iam_secret_key"
S3_BUCKET_NAME="your-s3-bucket-name"
AWS_REGION="your-aws-region" # e.g., eu-north-1
```