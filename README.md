# 🏠 Roomzone - Django Project

## 📌 Overview
Roomzone is a web application built with **Django** that allows users to manage and explore various projects. It includes authentication, project management, and a responsive frontend.

## 🚀 Features
✅ **User Authentication** - Sign up, log in, and manage profiles 🔑  
✅ **Project Management** - Add, update, and delete projects 📝  
✅ **Search & Filter** - Find projects easily 🔍  
✅ **Responsive UI** - Optimized for all devices 📱  
✅ **Django Admin Panel** - Manage data efficiently ⚙️  

## 🏗️ Tech Stack
- **Backend:** Django 🐍  
- **Frontend:** HTML, CSS, JavaScript 🎨  
- **Database:** SQLite 🗄️  
- **Authentication:** Django's built-in auth system 🔒  

## 📂 Project Structure
```
📦 Roomzone-main
├── 📄 manage.py
├── 📄 db.sqlite3
├── 📂 projects
│   ├── 📄 __init__.py
│   ├── 📄 admin.py
│   ├── 📄 apps.py
│   ├── 📄 models.py
│   ├── 📄 urls.py
│   ├── 📄 views.py
│   ├── 📄 form.py
│   ├── 📄 signals.py
│   ├── 📄 tests.py
└── 📄 README.md
```

## 🔧 Installation
1️⃣ **Clone the repository**
```bash
git clone https://github.com/HarshKadbe/Roomzone.git
cd Roomzone-main
```
2️⃣ **Create a virtual environment** (Recommended)
```bash
python -m venv env
source env/bin/activate  # For Linux/macOS
env\Scripts\activate    # For Windows
```
3️⃣ **Install dependencies**
```bash
pip install -r requirements.txt
```
4️⃣ **Run migrations**
```bash
python manage.py migrate
```
5️⃣ **Run the server**
```bash
python manage.py runserver
```
6️⃣ **Open the app in browser**
```
http://127.0.0.1:8000/
```

## 📜 License
This project is **MIT Licensed** 📝. Feel free to use and contribute.

## 🤝 Contributing
Pull requests are welcome! 🚀 If you have suggestions, create an issue and let's discuss.

