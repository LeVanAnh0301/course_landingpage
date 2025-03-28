# Computer Science Cambridge IP Landing Page

A professional landing page for the Computer Science Cambridge IP course.

## Setup Instructions

1. Create a virtual environment (recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the application:
```bash
python app.py
```

4. The application will be available at:
   - Local URL: `http://localhost:5000`
   - Public URL: Will be displayed in the console (provided by ngrok)

## Project Structure

- `app.py`: Main Flask application with ngrok integration
- `templates/index.html`: Main landing page template
- `static/style.css`: Custom CSS styles
- `static/teacher.jpg`: Teacher profile image (you need to add this)
- `requirements.txt`: Project dependencies

## Important Notes

1. The public URL provided by ngrok will change each time you restart the application
2. You can access the landing page from anywhere using the public URL
3. No need for Heroku or other hosting services

## Customization

You can customize the content by editing:
- Teacher information in `templates/index.html`
- Course details in `templates/index.html`
- Styling in `static/style.css`
- Add your own images to the `static` folder 