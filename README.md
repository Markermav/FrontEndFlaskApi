# Frontend Flask API for Library Management 📚🌐

Welcome to the Frontend Flask API for Library Management repository! This project provides a simple yet efficient way to manage a library using Flask. Users can view books in the library, fetch all available books, and even post their own books for lending.

## Project Overview

The Flask API consists of three main routes:
- **Home Route:** Users can access the home page, where they can see books or fetch all books in the library.
- **Library Route:** This route allows users to view all available books in the library.
- **Post Route:** Users can post their own books to lend them out to others.

## Setup Instructions

Follow these steps to set up the Flask API:

1. **Clone the Repository:**
   ```bash
   git clone <repository_url>
   ```

2. **Install Dependencies:**
   Navigate to the project directory and install dependencies:
   ```bash
   cd Frontend-Flask-API
   pip install -r requirements.txt
   ```

3. **Run the Flask App:**
   Start the Flask app:
   ```bash
   python app.py
   ```

4. **Access the API:**
   Open your web browser and navigate to `http://localhost:5000` to access the API endpoints.

## Routes

### Home Route

- **Description:** Allows users to access the home page.
- **URL:** `/`
- **Method:** GET
- **Response:** Renders the home page template.

### Library Route

- **Description:** Displays all available books in the library.
- **URL:** `/library`
- **Method:** GET
- **Response:** Renders the library page template with a list of books.

### Post Route

- **Description:** Allows users to post their own books for lending.
- **URL:** `/postbook`
- **Methods:** GET, POST
- **Request Parameters:**
  - `name`: Name of the book (string)
  - `price`: Price of the book (integer)
  - `image`: Image URL of the book (string)
- **Response:** Renders the post book page template.

## 📚 Happy Reading!

Congratulations! You now have a functional Flask API for managing a library. Explore the routes, view available books, and even post your own books for lending. Enjoy the reading experience! 🌟📖
