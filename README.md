# Project 1 - Wiki

A Wikipedia-style online encyclopedia built as part of Harvard University's CS50 Web Programming with Python and JavaScript course.

## Overview

Wiki is a web application that allows users to browse, search, create, and edit encyclopedia entries. The project was built using Django and demonstrates server-side web development concepts, routing, templates, forms, and data management.

## Features

### Browse Entries

* View all encyclopedia entries from the homepage.
* Click any entry to view its content.

### Entry Pages

* Entries are written in Markdown format.
* Markdown content is converted to HTML for display.

### Search

* Search for encyclopedia entries.
* Exact matches redirect directly to the entry page.
* Partial matches display a list of related entries.

### Create New Entry

* Create new encyclopedia pages.
* Prevent duplicate entries from being created.

### Edit Entry

* Modify existing encyclopedia content.
* Save changes directly from the edit page.

### Random Entry

* Visit a randomly selected encyclopedia page.

## Technologies Used

* Python
* Django
* HTML5
* CSS3
* Markdown
* Git

## Project Structure

```text
wiki/
│
├── encyclopedia/
│   ├── templates/
│   ├── views.py
│   ├── urls.py
│   ├── util.py
│   └── forms.py
│
├── entries/
├── manage.py
└── README.md
```

## Installation

1. Clone the repository:

```bash
git clone https://github.com/yourusername/cs50w-project1-wiki.git
```

2. Navigate to the project directory:

```bash
cd cs50w-project1-wiki
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Start the development server:

```bash
python manage.py runserver
```

5. Open your browser and visit:

```text
http://127.0.0.1:8000
```

## Learning Outcomes

Through this project, I learned:

* Building web applications with Django
* URL routing and request handling
* Template rendering
* Form creation and validation
* Markdown processing
* CRUD operations
* Managing application data

## Screenshots

Add screenshots of:

* Homepage
* Entry Page
* Search Results
* Create Entry Form
* Edit Entry Page

## Course

This project was completed as part of:

**CS50's Web Programming with Python and JavaScript** by Harvard University.

## Author

Kunsang

---

*This project was developed for educational purposes as part of the CS50 Web Programming curriculum.*
