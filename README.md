
---

# AcademicHub

**AcademicHub** is a Django-based web application for managing academic resources such as papers, projects, and blogs. It features a robust admin dashboard for content moderation, user management, and analytics — all in a modern, responsive interface built using Tailwind CSS and ECharts.

---

## 🚀 Features

* **Admin Dashboard**: View key metrics (users, papers, projects, blogs, downloads) with interactive charts.
* **Content Moderation**: Approve/reject uploaded content with filtering and pagination.
* **Blog Management**: Add, edit, and delete blog posts.
* **Quick Actions**: Floating dropdown for common tasks (add content, export data).
* **Responsive Design**: Built with Tailwind CSS for mobile-first UI.
* **Real-time Analytics**: Monitor activity feeds and dynamic charts.

---

## ⚙️ Prerequisites

* Python 3.8+
* Django 3.2+
* PostgreSQL (recommended) or SQLite (for local development)
* Node.js 16+ (optional, for Tailwind CSS)
* Git

---

## 🧩 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/academichub.git
cd academichub
```

### 2. Create and Activate a Virtual Environment

```bash
python -m venv venv
# Linux/macOS:
source venv/bin/activate
# Windows:
venv\Scripts\activate
```

### 3. Install Python Dependencies

```bash
pip install -r requirements.txt
```

### 4. Set Up the Database

#### PostgreSQL (recommended)

Update `academichub/settings.py`:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'academichub',
        'USER': 'your-username',
        'PASSWORD': 'your-password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

#### SQLite (development only)

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
```

Run migrations:

```bash
python manage.py makemigrations
python manage.py migrate
```

---

### 5. Install Tailwind CSS (Optional)

If building Tailwind locally:

```bash
npm install -D tailwindcss
npx tailwindcss init
```

Update `tailwind.config.js`:

```js
module.exports = {
  content: [
    './templates/**/*.html',
    './templates/admin/*.html',
  ],
  theme: {
    extend: {},
  },
  plugins: [],
}
```

Create `static/css/input.css`:

```css
@tailwind base;
@tailwind components;
@tailwind utilities;
```

Build the CSS:

```bash
npx tailwindcss -i ./static/css/input.css -o ./static/css/output.css --watch
```

---

### 6. Run the Development Server

```bash
python manage.py runserver
```

Visit [http://localhost:8000](http://localhost:8000)

---

## 🔐 Environment Variables

Create a `.env` file in the root directory:

```
SECRET_KEY=your-secret-key
DEBUG=True
DATABASE_NAME=academichub
DATABASE_USER=your-username
DATABASE_PASSWORD=your-password
DATABASE_HOST=localhost
DATABASE_PORT=5432
```

Install `python-decouple`:

```bash
pip install python-decouple
```

Update `settings.py`:

```python
from decouple import config

SECRET_KEY = config('SECRET_KEY')
DEBUG = config('DEBUG', default=False, cast=bool)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': config('DATABASE_NAME'),
        'USER': config('DATABASE_USER'),
        'PASSWORD': config('DATABASE_PASSWORD'),
        'HOST': config('DATABASE_HOST'),
        'PORT': config('DATABASE_PORT'),
    }
}
```

---

## 📁 Static Files

For production:

```bash
python manage.py collectstatic
```

In `settings.py`:

```python
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_DIRS = [BASE_DIR / 'static']
```

---

## 🌐 URL Patterns

In `urls.py`:

```python
from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('papers/upload/', views.upload_old_paper, name='upload_old_paper'),
    path('projects/upload/', views.upload_project, name='upload_project'),
    path('blogs/create/', views.create_blog, name='create_blog'),
    path('users/add/', views.add_user, name='add_user'),
    path('data/export/', views.export_data, name='export_data'),
    path('papers/', views.papers_view, name='papers'),
    path('projects/', views.projects_view, name='projects'),
    path('blogs/', views.blogs_view, name='blogs'),
    path('content-moderation/', views.content_moderation, name='content_moderation'),
]
```

---

## 🗂️ Project Structure

```
academichub/
├── academichub/
│   ├── settings.py
│   ├── urls.py
│   └── ...
├── core/
│   ├── views.py
│   └── ...
├── templates/
│   ├── admin/
│   ├── auth/
│   └── core/
├── static/
│   ├── css/
│   ├── js/
│   └── ...
├── media/
│   ├── blog_images/
│   └── ...
├── database/
│   └── academichub.sql
├── manage.py
├── requirements.txt
├── README.md
├── LICENSE
└── CODE_OF_CONDUCT.md
```

---

## 📦 Dependencies

### Python Packages

See `requirements.txt`:

```
django>=3.2
psycopg2-binary>=2.9
python-decouple>=3.6
```

Install:

```bash
pip install -r requirements.txt
```

### Frontend Libraries

* **Tailwind CSS**: Local or via CDN
* **ECharts** (Charts):
  CDN: `https://cdn.jsdelivr.net/npm/echarts@5.5.0/dist/echarts.min.js`
* **RemixIcon** (Icons):
  CDN: `https://cdn.jsdelivr.net/npm/remixicon@3.5.0/fonts/remixicon.css`

---

## 🧪 Usage

* Visit `/dashboard/` to access the admin interface.
* Use the floating quick actions dropdown for rapid access.
* Moderate user content, manage blogs, and analyze metrics.

---

## 🚀 Deployment

* Set `DEBUG=False` and configure `ALLOWED_HOSTS`.
* Use PostgreSQL for production.
* Collect and serve static files using Nginx or similar.
* Set environment variables securely.

---

## 🛠️ Troubleshooting

| Issue                      | Solution                                       |
| -------------------------- | ---------------------------------------------- |
| Quick actions not working  | Check JS console; verify ECharts CDN is loaded |
| Database connection errors | Check credentials and server                   |
| Static files not loading   | Run `collectstatic` and check static paths     |
| URL not found              | Confirm route exists in `urls.py` and views    |

---

## 🤝 Contributing

We welcome contributions!

1. Fork the repository
2. Create a branch: `git checkout -b feature/your-feature`
3. Make changes and add tests (if needed)
4. Ensure code follows **PEP8**
5. Commit: `git commit -m "Add feature"`
6. Push: `git push origin feature/your-feature`
7. Open a pull request

Please follow our [Code of Conduct](CODE_OF_CONDUCT.md) and ensure new features are tested.


---

## 📬 Contact

For support or questions, open an [issue](https://github.com/your-username/academichub/issues) or join the discussions on GitHub.

---

