# Google Analytics Django Project

This Django project provides a simple implementation of Google Analytics statistics, including calls, messages, people asking for directions, website visits from profiles, profile views, and searches appearances.

## Getting Started

1. Clone the repository:

    ```bash
    git clone https://github.com/your-username/GoogleAnalytics.git
    ```

2. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Apply migrations to create the database tables:

    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

4. Run the Django development server:

    ```bash
    python manage.py runserver
    ```

5. Access the project in your browser at [http://localhost:8000/](http://localhost:8000/).

## Project Structure

- `core`: Django app containing models and views.
- `templates`: HTML templates for rendering the Google Analytics report.

## Technologies Used

- Django
- MySQL

## How to Use

1. Access the project at [http://localhost:8000/](http://localhost:8000/).
2. View the Google Analytics report, including statistics on calls, messages, people asking for directions, website visits from profiles, profile views, and searches appearances.

## Customization

- Modify the models in `core/models.py` to add or customize statistics.
- Adjust the HTML templates in `templates/index.html` to change the appearance of the report.

## Contributing

Contributions are welcome! Please follow the guidelines in [CONTRIBUTING.md](CONTRIBUTING.md).

## License

This project is licensed under the [MIT License](LICENSE).
