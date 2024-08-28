# FastAPI Passkey Example App

## Project Overview

This project implements a web application with a login using Corbado's passkey-first authentication service
integrated with a FastAPI backend. The application consists of two main pages: a login page and a home page. Once users
log in successfully via the Corbado on the login page, they are redirected to the home page where they can log
out and view protected content.

Please see the [full blog post](https://www.corbado.com/blog/passkeys-fastapi) to understand all the required steps to integrate passkeys into FastAPI apps.


## Tools and Technologies Used

- **FastAPI**: A full-featured Python web framework, used to build the backend of the application.
- **Corbado**: An authentication service used to handle passkey-first user authentication.
- **HTML & CSS**: Used to structure and style the frontend of the application.

## Features

- **Passkey-first Authentication**: Utilizes Corbado's authentication service for secure user login.
- **Session management**: Uses Corbado's session management to display content based on the user's authentication status.

## How to Use

### 1. File structure
```
├── .env                 # Contains all environment variables
├── main.py              # Contains our webapplication (Handles routes)
└── templates
    ├── index.html       # Login page
    └── profile.html     # Profile page
```

### 2. Setup
#### Step 2.1: Clone the Repository

Clone this repository to your local machine by running:

```sh
git clone https://github.com/corbado/example-passkeys-fastapi

```

#### Step 2.2: Create .env File

To configure the credentials, you will need to create a `.env` file with your Corbado `Project ID` and `API secret`:
To get your `Project ID` and `API secret`, visit the [Corbado developer panel](https://app.corbado.com/?technology=passkeys&framework=FastAPI#signup-init).

Please refer to the [Corbado docs](https://docs.corbado.com/overview/welcome) for more details on obtaining the
necessary credentials and integrating Corbado authentication in your application.

```sh
PROJECT_ID=<your-project-id>
API_SECRET=<your-api-secret>

```

#### Step 2.3: Configure Corbado project

In the Corbado developer panel, visit the [URLs settings](https://app.corbado.com/app/settings/general/urls) and enter the values shown in the image below:
![Corbado Developer Panel FastAPI URLs](https://github.com/user-attachments/assets/9fdc7edc-2bba-4a82-880b-27a931b84e03)


#### Step 2.4: Run the Project

Use the following command to run the project in a docker container:

```sh
docker compose up
```

### 3. Usage

After step [2.4](#step-24-run-the-project), your local server should be fully working.

If you now visit [http://localhost:8000](http://localhost:8000), you should be able to sign up using the Corbado UI component.

<img width="1177" alt="fastapi passkeys ui component" src="https://github.com/user-attachments/assets/287b8c4b-e18d-4d76-9ec0-0e86985d656b">


When authenticated you will be forwarded to the `/profile` page.

<img width="1434" alt="fastapi passkey list" src="https://github.com/user-attachments/assets/5479506e-6c70-4202-8174-9c5f2caea52e">



