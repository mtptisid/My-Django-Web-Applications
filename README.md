# Django Installation Guide and Sample Login Page

## Installation Guide for Django

### 1. Install Python:

- Download and install Python from the [official Python website](https://www.python.org/downloads/).
- During installation, make sure to check the box that adds Python to your system's PATH.

### 2. Install pip:

- Pip is Python's package installer. It usually comes pre-installed with Python. You can check if pip is installed by running the following command in the command line:

```bash
pip --version
```
# Django Installation Guide for Linux and Windows Servers

## Installing Python

### Linux
1. Open terminal.
2. Update package index:
```sudo apt update`.
3. Install Python: `sudo apt install python3 python3-pip`.

### Windows
1. Download Python installer from [Python.org](https://www.python.org/downloads/).
2. Run the installer, ensure "Add Python to PATH" is checked, and proceed with installation.
   
## Creating a Virtual Environment

### Linux
1. Open terminal.
2. Navigate to the directory where you want to create your project.
3. Install virtualenv if you haven't already: `sudo apt install python3-venv`.
4. Create a new directory for your virtual environment: `mkdir myenv`.
5. Navigate into the newly created directory: `cd myenv`.
6. Create a virtual environment named `venv`: `python3 -m venv venv`.
7. Activate the virtual environment:

```bash
$ source venv/bin/activate
```

## Installing Django

### Both Linux and Windows
1. Open terminal (Linux) or command prompt (Windows).
2. Install Django using pip:

   `pip install django`.

## Setting up a Django Project

### Both Linux and Windows
1. Create a directory for your project: `mkdir myproject`.
2. Navigate into the project directory: `cd myproject`.
3. Initialize Django project:
   
   `django-admin startproject myproject`.


## Creating a Simple HTML and CSS File

1. Inside your project directory, create a new directory called `templates`.
2. Inside the `templates` directory, create a new file called `index.html` with the following content:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>My Django Website</title>
    <link rel="stylesheet" href="{% static 'styles.css' %}">
</head>
<body>
    <div class="container">
        <h1>Welcome to My Django Website!</h1>
        <p>This is a simple Django website.</p>
    </div>
</body>
</html>
```
3. Inside the `static` directory, create a new file called `style.css` with the following content:
```css
.container {
    max-width: 800px;
    margin: 0 auto;
    padding: 20px;
    text-align: center;
    font-family: Arial, sans-serif;
}
```
# creating View.py

```
from django.shortcuts import render

def Home(request):

    return render(request, 'myapp/home.html', context)

```

# creating urls.py

```
from django.urls import path
from . import views

urlpatterns = [
    path("", views.Home, name="home")]
```




## Running Django Server

### Both Linux and Windows
1. Navigate into your project directory if you're not already there.
2. Run the development server: `python manage.py runserver`.

```bash
$ python manage.py runserver

```
# run existing project from git

## install git

```
pip install git
```

## cone the project from git

```
git clone https://github.com/mtptisid/DjangoProject/
```

### go to the project directory
```
cd DjangoProject
```

### run the server

```
python manage.py runserver
```

# Notes for Python and Django


http://35.173.122.68:8080/


http://35.173.122.68:8080/about

# Contact us 

## Contact me for any query related to django or python projects.

[Instagram](https://www.instagram.com/its_5iD/)

[WhatsApp](https://wa.me/9740671620)
