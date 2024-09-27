# Questify

**Questify** is a social media platform for questions and answers, where users can create groups, ask and answer questions, make friends, and chat. The platform allows users to engage in discussions, share knowledge, and connect with others. Built with Django using Function-Based Views (FBVs), the project offers a dynamic and user-friendly interface to facilitate communication and knowledge sharing.

## Features

- **Questions & Answers**: Users can ask and answer questions in various groups.
- **Groups**: Create, edit, and delete groups to manage topics of interest.
- **Friends**: Add friends, invite them to groups, and engage in private chats.
- **Chat**: Direct messaging functionality to communicate with friends.
- **Likes**: Like answers and questions to show support or appreciation.
- **Authentication**: Secure login and signup system with user profile management.
- **Profile Page**: Each user has a profile page displaying their activities, such as asked and answered questions.
- **Success Messages**: Feedback messages for actions like profile updates, sending friend requests, and posting questions.

## Technologies Used

- **Backend**: Django (Function-Based Views)
- **Frontend**: HTML, CSS, Bootstrap
- **Database**: SQLite (or any database supported by Django)
- **Version Control**: Git & GitHub

## Getting Started

To get a copy of the project up and running on your local machine, follow these steps:

### Prerequisites

- Python 3.x
- Django 4.x
- Git

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/AhmedHashim04/Questify.git
   
2. Navigate to the project directory:
   cd project
3. Create and activate a virtual environment:

   - On Windows:
         python -m venv env
         env\Scripts\activate
   - On macOS/Linux:
         python3 -m venv env
         source env/bin/activate
     - Install the project dependencies:
         pip install -r requirements.txt
4. Apply the database migrations:
   python manage.py migrate
5. Create a superuser to access the admin panel (optional but recommended):
   python manage.py createsuperuser

6. Run the development server:
   python manage.py runserver
7. Open your browser and navigate to:
   http://127.0.0.1:8000/


you should now be able to see the Questify platform running locally.

Usage
Admin Panel: If you created a superuser, you can access the Django admin panel at http://127.0.0.1:8000/admin/ to manage users, groups, questions, and more.
Profile Page: Users can view their profiles to see their questions, answers, and manage their accounts.


