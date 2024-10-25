# Puddle - E-commerce for Digital Products

## Description

Puddle is a web-based e-commerce platform that allows users to buy and sell digital products, including software and hardware. The application is designed to provide a seamless user experience with features for user authentication, product listings, and community discussions. Built using Django for the backend and Tailwind CSS for the frontend, Puddle is responsive and user-friendly.

## Features

- **User  Authentication**: Users can register, log in, and manage their profiles.
- **Product Listings**: Users can browse and search for digital products.
- **Community Discussions**: Users can engage in discussions about products, share feedback, and post images.
- **Responsive Design**: The application is fully responsive, ensuring a great experience on both desktop and mobile devices.
- **Dynamic Categories**: Users can explore different categories of products.

## Technologies Used

- **Backend**: Django
- **Frontend**: HTML, CSS (Tailwind CSS)
- **Database**: SQLite (or any other database of your choice)
- **Version Control**: Git

## Installation

Follow these steps to set up the project locally:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/MustcodeQ/Puddle---E-commerce-for-Digital-Products.git
   cd puddle


##Create a virtual environment:
  python -m venv venv
  source venv/bin/activate  # On Windows use `venv\Scripts\activate`
##Install dependencies:
  pip install -r requirements.txt
##Run migrations:
  python manage.py migrate
##Create a superuser (optional):
  python manage.py createsuperuser
##Run the development server:
  python manage.py runserver
  
