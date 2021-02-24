# Python-Microservices
Microservice in Python using **Django**, **Flask** and multiples **MySQL** database. Significantly reduces time delay and load on the server, helping with larger applications.


Uses:

* Django 3.0
* Python 3.8
* Flask 1.1.2

## Backend apps

* **Main app**: Communicates with *Admin app* over rabbitmq service provider, in this case cloudamqp. Responsible for handling display functions through calls from Frontend *React-Typescript* app.

* **Admin app**: Handles admin functions and executions.
 
