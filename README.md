# Resume Submission Web App

This repository contains files for a simple web application built with Flask, HTML, and deployed on AWS S3.

## Overview

The web application allows users to submit their resumes via a form. The submitted resume data is processed and stored temporarily on an AWS S3 bucket. Users can also download their submitted resumes.

## Files

- `app.py`: This is the main Python file that contains the Flask application. It defines the routes for rendering the HTML templates and handling form submissions.
- `index.html`: This HTML file contains the form for submitting resumes. It is rendered by Flask and includes JavaScript for dynamic form elements.
- `requirements.txt`: This file lists all the Python dependencies required to run the Flask application. Install these dependencies using `pip install -r requirements.txt`.
- `README.md`: This file provides an overview of the repository and instructions for running the web application.

## Running the Application

1. Clone the repository to your local machine:

    ```bash
    git clone https://github.com/your-username/resume-submission-web-app.git
    ```

2. Navigate to the project directory:

    ```bash
    cd resume-submission-web-app
    ```

3. Install the required Python dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Run the Flask application:

    ```bash
    python app.py
    ```

5. Open your web browser and go to `http://localhost:5000` to access the application.

## Contributing

If you'd like to contribute to this project, feel free to fork the repository, make your changes, and submit a pull request. Contributions are welcome!

## License

This project is licensed under the [MIT License](LICENSE).
