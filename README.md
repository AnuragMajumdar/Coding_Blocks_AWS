**CodingBlocks_Blog**



**Mentioning important deliverables** : 

### AWS Live Deployment link: 
[http://13.60.169.195:8000/](http://13.60.169.195:8000/)
( **Server Session is already running on my EC2 instance you can directly open the link**)


### Steps to run the server: (*If you want to run it on your server*)

1. **Clone the repository to your local machine**:
   - Clone the repository by running:
     ```bash
     git clone <repository_url>
     ```

2. **Establish virtual environment**:
   a. `python -m venv env`
   
   b. `venv\Scripts\activate`

3. **For local server running**: 
   - Run the following command:
     ```bash
     ENV_FILE=.env.development docker-compose up --build
     ```
   a. Click on this for local [http://0.0.0.0:8000/](http://0.0.0.0:8000/)

4. **For Production server running**: 
   - Run the following command:
     ```bash
     ENV_FILE=.env.production docker-compose up --build
     ```
   a. Click on this for AWS hosted link [http://13.60.169.195:8000/](http://13.60.169.195:8000/)

---

**Technologies Used**
- **Backend**: Implemented with RESTful APIs for all three services i.e User Service, Blog Service, Comment Service.
- **Authentication**: Secured using JWT.
- **Password Hashing**: Secure password storage (Django includes inbuilt support for secure password storage).
- **Database**: PostgreSQL for structured and efficient data management.
- **Containerization**: All Services are containerized using Docker and Created a docker-compose.yml file to define and orchestrate the services.
- **Environment Management**: Provided separate .env files for local development and production environments i.e .env.development and .env.production respectively.

---

**Docker Volumes in Use**

This setup uses Docker volumes for persistent and shared data storage:

1. **postgres_data Volume**:
   
   o Service: db

   o Purpose: Stores PostgreSQL database files at /var/lib/postgresql/data to ensure database persistence.

3. **Bind-Mounted Volumes (.:/app)**:
   
   o Services: migration, users, blogs, comments

   o Purpose: Shares application code between the host and containers for development convenience.

---
## API Endpoints Used in My Project 

### User Service  

- **POST** `/register/`: Register a new user.  
- **POST** `/login/`: Authenticate a user.  
- **GET** `/users/<id>`: Retrieve user details.  
- **PUT** `/users/<id>`: Edit user details.  
- **DELETE** `/users/<id>`: Delete a user.  

### Blog Service  

- **POST** `/blogs/`: Create a new blog post.  
- **GET** `/blogs/`: List all blog posts.  
- **GET** `/blogs/<id>`: Fetch a specific blog post.  
- **PUT** `/blogs/<id>`: Edit an existing blog post.  
- **DELETE** `/blogs/<id>`: Delete a specific blog post.  

### Comment Service  

- **POST** `/comments/`: Add a comment to a blog post.  
- **GET** `/comments?post_id=<id>`: List comments for a specific blog post.  


---

**User Service**

**Endpoints** : http://13.60.169.195:8000/users/signup/

**POST /register/**

- **Description**: Register a new user.
- **Request Body**: 
  ```json
  {
    "username": "string",
    "email": "string",
    "Bio" : "string",
    "password": "string"
  }
  ```
- **Response**: 
  ```json
  {
    "message": "User registered successfully",
    "user_id": "integer"
  }
  ```
![image](https://github.com/user-attachments/assets/4ea53425-8ef7-4c3c-9d5a-8cd35405b7d0)

---

**POST /login/**
**Endpoints** : http://13.60.169.195:8000/users/login/

- **Description**: Authenticate a user.
- **Request Body**: 
  ```json
  {
    "email": "string",
    "password": "string"
  }
  ```
- **Response**: 
  ```json
  {
    "token": "string",
    "message": "Login successful"
  }
  ```
![image](https://github.com/user-attachments/assets/f86086d9-1011-4b6c-9be8-2b7037a3911d)


---

**GET /users/<id>**
**Endpoints** : http://13.60.169.195:8000/users/profile/

- **Description**: Retrieve the details of a specific user by their unique identifier.

- **Request Parameters**:  
  The endpoint requires the <id> parameter in the URL path.

- **Response**:  
  - On success:
    ```json
    {
      "id": "integer",
      "username": "string",
      "email": "string",
      "bio": "string",
      "created_at": "string",
    }
    ```
![image](https://github.com/user-attachments/assets/0bab2a5d-a1ef-4be3-8418-b386cc394493)

---

**Blog Service**

**Endpoints** : http://13.60.169.195:8000/blogs/new/

**POST /blogs/**

- **Description**: Create a new blog post.
- **Request Body**: 
  ```json
  {
    "title": "string",
    "content": "string",
    "author_id": "integer"
  }
  ```
- **Response**: 
  ```json
  {
    "message": "Blog post created successfully",
    "blog_id": "integer"
  }
  ```
![image](https://github.com/user-attachments/assets/475df841-ceb3-477f-9968-265c648a6794)


**GET /blogs/<id>**

**Endpoints** : http://13.60.169.195:8000/?search_query=Anurag+Project

- **Description**: Fetch a specific blog post by its unique identifier.

- **Request Parameters**:  
  The endpoint takes a single parameter in the URL path:
  - `<id>`: The Title of the Blog.

- **Response**:  
  - On success:
    ```json
    {
      "id": "integer",
      "title": "string",
      "content": "string",
      "author": "string",
      "created_at": "string",
    }
    ```
  ![image](https://github.com/user-attachments/assets/c500f7f8-7238-479d-8036-ebf084c80658)


**GET /blogs/**


**Endpoints** : http://13.60.169.195:8000/
- **Description**: List all blog posts (supports pagination).
- **Query Parameters**: 
  - `page`: Page number (default: 1).
  - `size`: Number of posts per page (default: 10).
- **Response**: 
  ```json
  [
    {
      "id": "integer",
      "title": "string",
      "author": "string",
      "created_at": "datetime"
    }
  ]
  ```
![image](https://github.com/user-attachments/assets/f3fbb155-a917-46c2-936f-532ad2d309e7)


**PUT /blogs/<id>**

**Endpoints** : http://13.60.169.195:8000/blogs/blog/8/edit/
- **Description**: Edit an existing blog post.
- **Request Body**: 
  ```json
  {
    "title": "string",
    "content": "string"
  }
  ```
- **Response**: 
  ```json
  {
    "message": "Blog post updated successfully"
  }
  ```
![image](https://github.com/user-attachments/assets/b2f3d56b-b015-4810-9e4d-b33c7c00891f)


**DELETE /blogs/<id>**

**Endpoints** : http://13.60.169.195:8000/blogs/blog/8/delete/
- **Description**: Delete a blog post.
- **Response**: 
  ```json
  {
    "message": "Blog post deleted successfully"
  }
  ```
![image](https://github.com/user-attachments/assets/27ed7457-bdfa-4cf9-8812-e5ab12d5f250)


---

**Comment Service**

**Endpoints** : http://13.60.169.195:8000/comments/blog/5/comment/

**POST /comments/**

- **Description**: Add a comment to a blog post.
- **Request Body**: 
  ```json
  {
    "post_id": "integer",
    "content": "string",
    "author_id": "integer"
  }
  ```
- **Response**: 
  ```json
  {
    "message": "Comment added successfully",
    "comment_id": "integer"
  }
  ```
![image](https://github.com/user-attachments/assets/ed7d89bc-a64d-488d-8e73-2be08d76d399)


---

**Database Design**

- **User Schema**: Stores user data.
- **Blog Schema**: Stores blog post data.
- **Comment Schema**: Stores comments for blog posts.

---

**Design Decisions and Trade-offs**

- **Authentication**: JWT was chosen for its stateless nature and scalability.
- **Password Security**: Used Inbuild Authorization for password security.
- **Pagination**: Improves performance for listing blog posts.
- **Flat Comment Structure**: Simplifies initial implementation with the potential to extend for nested comments.

---

**Setup and local launch**

1. Clone the repository.
2. Install dependencies using `pip install -r requirements.txt`.
3. Set up the PostgreSQL database with schemas for users, blogs, and comments.
4. Configure environment variables for database and JWT secrets.
5. Run migrations to initialize the database.
6. Start the application using `python manage.py runserver`.

---

**Example Logs**

```text
[04/Jan/2025 18:34:36] "GET / HTTP/1.1" 200 1452
[04/Jan/2025 18:34:43] "GET /users/login/ HTTP/1.1" 200 2022
[04/Jan/2025 18:34:57] "GET /users/signup/ HTTP/1.1" 200 3101
[04/Jan/2025 18:37:15] "POST /users/signup/ HTTP/1.1" 302 0
[04/Jan/2025 18:37:25] "POST /users/login/ HTTP/1.1" 302 0
[04/Jan/2025 18:37:48] "POST /blogs/new/ HTTP/1.1" 302 0
[04/Jan/2025 18:38:09] "GET /blogs/1/ HTTP/1.1" 200 2650
```
________________________________________
![WhatsApp Image 2025-01-05 at 13 03 03_a7a26ddb](https://github.com/user-attachments/assets/289cf9a2-7092-49f2-a319-28e069ae64c3)

_________________________________________

*Clear instructions for AWS deployment :*

---

### **Final Deployment Documentation for Django Blog Platform on AWS (Using EC2 and RDS)**

---

### **Prerequisites**
Before starting the deployment, ensure the following:

1. **AWS Account**: Ensure you have an active AWS account.
2. **GitHub Repository**: Ensure your Django project is pushed to GitHub.
3. **Docker & Docker Compose**: Install Docker and Docker Compose on your EC2 instance to run the application in containers.

---

### **Step-by-Step Deployment Guide**
   
---

### **Part 1: Set Up Amazon RDS (PostgreSQL) Database**

#### 1. **Create RDS Instance**
   - **Login to AWS Console**:
     - Go to the [AWS Management Console](https://aws.amazon.com/console/).
   
   - **Navigate to RDS**:
     - In the search bar, type “RDS” and click on **RDS** to go to the RDS Dashboard.

   - **Create a New PostgreSQL Database**:
     - Click on **Create database**.
     - Choose **Standard Create**.
     - Under **Engine options**, select **PostgreSQL**.
     - Choose your preferred version.
     - Set **DB instance identifier** (e.g., `your-db-name`).
     - Set the **Master username** (e.g., `admin`).
     - Set the **Master password** and confirm it.
   
   - **Choose Instance Type**:
     - Select the instance type (e.g., `db.t3.micro` for the free tier).

   - **VPC & Networking**:
     - Leave the default VPC or choose an existing VPC.
     - Ensure **Public accessibility** is set to **Yes** for your database to be accessible externally.

   - **Database Settings**:
     - Set the **Database name** (e.g., `blog_db`).
   
   - **Create the Database**:
     - Click **Create database** to start the process.

#### 2. **Obtain the RDS Endpoint**
   - After the database is created, go to the RDS dashboard, click on your RDS instance, and find the **Endpoint** under the **Connectivity & security** tab. This will be in the form `your-db-name.cxj7i7zvdsrb.us-west-2.rds.amazonaws.com`.
   - Keep the **Endpoint**, **Master username**, and **Password** for later use in the application.

---
Image of my AWS account RDS :
![WhatsApp Image 2025-01-05 at 13 03 03_ac084e59](https://github.com/user-attachments/assets/a22830eb-6654-4578-b0ed-70dd9f6080b6)


### **Part 2: Set Up EC2 Instance**

#### 1. **Create EC2 Instance**
   - **Login to AWS Console**:
     - Go to the [AWS Management Console](https://aws.amazon.com/console/).
   
   - **Navigate to EC2**:
     - In the search bar, type “EC2” and click on **EC2** to go to the EC2 Dashboard.

   - **Launch Instance**:
     - Click **Launch Instance**.
     - Choose an **Amazon Linux 2 AMI** for simplicity (or another AMI of your choice).
     - Select **t2.micro** (eligible for the free tier).
     - Set **Key pair**: Select an existing SSH key pair or create a new one.
     - Choose **Security group**: Ensure that the security group allows inbound traffic on the following ports:
       - 22 (SSH)
       - 80 (HTTP)
       - 443 (HTTPS) if you plan to use SSL later.
   
   - **Launch the Instance**:
     - Click **Launch**.

#### 2. **SSH into EC2 Instance**
   - After the EC2 instance is running, connect to it using SSH:
   ```bash
   ssh -i /path/to/your-key.pem ec2-user@<EC2_PUBLIC_IP>
   ```

---
Image of my Account EC2 Instance:
![WhatsApp Image 2025-01-05 at 13 03 03_94d80e62](https://github.com/user-attachments/assets/e7c00540-c2bf-4a40-8e43-50d9d207aab1)


### **Part 3: Clone the Repository and Set Up Docker**

#### 1. **Clone Your GitHub Repository**
   - Install Git if it's not already installed:
   ```bash
   sudo yum install git
   ```

   - Clone your project repository:
   ```bash
   git clone https://github.com/yourusername/your-repo-name.git
   cd your-repo-name
   ```

#### 2. **Install Docker and Docker Compose**
   - **Install Docker**:
   ```bash
   sudo amazon-linux-extras install docker
   sudo service docker start
   sudo usermod -a -G docker ec2-user
   ```
   - Log out and back in to refresh group membership.

   - **Install Docker Compose**:
   ```bash
   sudo curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
   sudo chmod +x /usr/local/bin/docker-compose
   ```

---

### **Part 4: Configure Your Django Project**

#### 1. **Update `.env.production` File**
   - Modify the `.env.production` file in your project to include the database connection information:
     ```bash
     DB_HOST=your-db-name.cxj7i7zvdsrb.us-west-2.rds.amazonaws.com
     DB_PORT=5432
     DB_NAME=blog_db
     DB_USER=admin
     DB_PASSWORD=your-db-password
     ```

#### 2. **Update Django Settings**
   - In your `settings.py` file, update the database configuration:
     ```python
     DATABASES = {
         'default': {
             'ENGINE': 'django.db.backends.postgresql',
             'NAME': os.environ.get('DB_NAME'),
             'USER': os.environ.get('DB_USER'),
             'PASSWORD': os.environ.get('DB_PASSWORD'),
             'HOST': os.environ.get('DB_HOST'),
             'PORT': os.environ.get('DB_PORT'),
         }
     }
     ```

---

### **Part 5: Deploy the Django Application**

#### 1. **Build and Run the Application with Docker Compose**
   - Since you have separate `.env.production` and `.env.development` files, you will run the application with the production environment when deploying on AWS:
   ```bash
   ENV_FILE=.env.production docker-compose up --build
   ```

   - This command will:
     - Set the environment to `production`.
     - Build the Docker containers and start the application.
   
   - If you want to run the application in development mode on your local machine, use:
   ```bash
   ENV_FILE=.env.development docker-compose up --build
   ```

#### 2. **Access Your Application**
   - Open a browser and go to:
   ```text
   http://<EC2_PUBLIC_IP>:8000
   ```
   - You should now see your Django blog platform running.

---

### **Part 6: Configure EC2 and RDS Security Groups**

#### 1. **Configure EC2 Security Group for Application Ports**
   - In the **EC2 Dashboard**, click on **Security Groups**.
   - **Edit the Inbound Rules** of your EC2 security group to allow inbound traffic on the following ports:
     - **Port 22** (for SSH access).
     - **Port 80** (for HTTP traffic).
     - **Port 443** (for HTTPS traffic if you intend to use SSL).
     - **Port 8000-8002** (for Django application):
       - Select **Custom TCP Rule** and set the **Port Range** as `8000-8002`.
     - **Port 5432** (for PostgreSQL database access from local machine if needed):
       - Select **Custom TCP Rule** and set the **Port Range** as `5432`.
     - Allow connections from your local IP or open to all IPs (0.0.0.0/0) if needed.

   - **Save the Inbound Rules**.

#### 2. **Configure RDS Security Group**
   - In the **RDS Dashboard**, go to your **RDS instance**.
   - **Edit the Inbound Rules** for the RDS security group:
     - Allow inbound connections from your EC2 instance's security group on port **5432** (PostgreSQL).

---

### **Resources Used in This Deployment**
Here is a list of the resources involved in the deployment process:

1. **EC2 Instance**:
   - Used to host and run the Django application in Docker containers.
   
2. **RDS (Relational Database Service)**:
   - Used for hosting the PostgreSQL database for your Django project.

3. **Docker**:
   - Used to containerize the Django application and ensure a consistent environment.

4. **Docker Compose**:
   - Used to define and manage the multi-container Docker application for Django.

---

### **Additional Notes**
1. **Database Setup**: 
   - Your Django project will now use PostgreSQL hosted on RDS. Ensure that the RDS instance is accessible from your EC2 instance, and you’ve updated the connection settings properly in the `.env.production` file.
   
2. **.env Files**:
   - The `.env.production` file contains sensitive information like database credentials. Ensure that it is kept secure and not exposed in version control (use `.gitignore` to ignore `.env` files).

3. **Docker Compose Logs**:
   - If you encounter any issues, you can check the logs of your application by running:
   ```bash
   docker-compose logs
   ```

---
!

