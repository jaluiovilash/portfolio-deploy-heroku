# Personal Portfolio Website

## Overview

Welcome to my personal portfolio repository! This project showcases my work and skills as a full stack web developer. I have used a Bootstrap template for the frontend and Django for the backend, making the website dynamic, easy to handle, and use. The website is also deployed online using Heroku.

## Features

- **Dynamic Website:** The website is built to be fully dynamic, allowing for easy updates and management of content.
- **Authentication System:** A robust authentication system is implemented to manage user access and security.
- **Blog Section:** A dedicated section to showcase blog posts.
- **Contact Section:** A functional contact form for visitors to reach out.
- **Registration Form:** User registration is enabled for enhanced interactivity.
- **Deployment:** The website is deployed on Heroku, making it accessible online.

## Getting Started

### Prerequisites

- Python 3.x
- Django
- Bootstrap
- Heroku account

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/jaluiovilash/portfolio-deploy-heroku.git
   cd portfolio
   ```

2. Create a virtual environment and activate it:
   ```bash
   python -m venv env
   source env/bin/activate  # On Windows use `env\Scripts\activate`
   ```

3. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

4. Apply migrations and run the development server:
   ```bash
   python manage.py migrate
   python manage.py runserver
   ```

5. Open your browser and navigate to `http://127.0.0.1:8000` to see the website in action.

### Deployment

To deploy the project on Heroku:

1. Login to Heroku:
   ```bash
   heroku login
   ```

2. Create a new Heroku app:
   ```bash
   heroku create jaluiovilash
   ```

3. Push the code to Heroku:
   ```bash
   git push heroku main
   ```

4. Run the database migrations on Heroku:
   ```bash
   heroku run python manage.py migrate
   ```

5. Open your deployed app in the browser:
   ```bash
   heroku open
   ```

## Video Overview

Hey all! I have described an overview of full stack web development in this entire video. From scratch, I have shown how to build a complete dynamic website that's very easy to understand for beginners. The video covers:

- Building a dynamic website
- Implementing an authentication system
- Creating a blog section
- Developing a contact section
- Setting up a registration form
- Hosting the website on Heroku

## Contributing

Feel free to fork this repository and make your own contributions. Pull requests are welcome!

## License

This project is licensed under the MIT License.

## Contact

If you have any questions or suggestions, feel free to reach out!
