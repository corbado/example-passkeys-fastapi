# Passkey-First Authentication with FastAPI and Corbado

## Project Overview

This project implements a web application with a login system using Corbado' passkey-first authentication service
integrated with a FastAPI backend. The application consists of two main pages: a login page and a home page. Once users
log in successfully via the Corbado service on the login page, they are redirected to the home page where they can log
out and view protected content.

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
├── templates
|   ├── index.html       # Login page
|   └── profile.html     # Profile page

```

### 2. Setup
#### Step 2.1: Clone the Repository

Clone this repository to your local machine by running:

```sh
git clone https://github.com/corbado/example-passkeys-fastapi

```

#### Step 2.2: Create .env File

To configure the credentials, you will need to create a .env file with your project ID and API secret from Corbado:
To get your project ID and API secret visit your [Corbado developer panel](https://app.corbado.com/).

Please refer to the [Corbado docs](https://docs.corbado.com/overview/welcome) for more details on obtaining the
necessary credentials and integrating Corbado authentication in your application.

```sh
PROJECT_ID=<your-project-id>
API_SECRET=<your-api-secret>

```

#### Step 2.3: Configure Corbado project

In the Corbado developer Panel, visit the [URLs settings](https://app.corbado.com/app/settings/general/urls) and enter the values shown in the image below:
<img width="1242" alt="image" src="https://github.com/corbado/example-passkeys-fastapi/assets/23581140/46063cc3-c412-4e4e-8de2-ca1f53cd15c1">


#### Step 2.4: Run the Project

Use the following command to run the project in a docker container:

```sh
docker compose up
```

### 3. Usage

After step 2.4. your local server should be fully working.

If you now visit [http://localhost:8000](http://localhost:8000), you should be able to sign up using the Corbado web component.

<img width="1125" alt="webcomponent" src="https://github.com/corbado/example-passkeys-django/assets/23581140/1390088d-26bd-4a69-b8d8-d87334a5c9a6">


When authenticated you will be forwarded to the `/profile` page.

<img width="1125" alt="profile_page" src="https://github.com/corbado/example-passkeys-django/assets/23581140/340a7ec2-2e3a-44bb-b781-bbe42f215f0c">



