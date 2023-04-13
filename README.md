# Django-ChatApp

In this project, we made a simple chat app App using Django.
We also use **websockets** and a package called: [Channels](https://pypi.org/project/channels/)

## Motivation

This project is part of a serie of projects we build to get dive into **Django web Framework**.
It was originally devoloped by [Code with Stein](https://www.youtube.com/watch?v=SF1k_Twr9cg)

## Keys Takeaways

Going through this projects helps us understands the use of a couple of tools including:
    - Websockets
    - [Channels Package](https://pypi.org/project/channels/)
    - Templates concept in Django


## Deployment

To launch this project after cloning it, run:

    - Create and activate a virtual environment:
        ```bash
        $ virtualenv <name>

        $ source <name>/bin/activate
        ```

    - Install dependencies:
        ```bash
        pip install -r requirements.txt
        ```
    - Run migrations:
        ```bash
        $ python manage.py makemigrations 

        $ python manage.py migrate 

        ```
    - Run server:
        ```bash
        python manage.py runserver
        ```