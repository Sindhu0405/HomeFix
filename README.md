# 🏠 HomeFix – Smart Appliance Care & Diagnosis

HomeFix is a full-stack web application designed to help users manage their household appliances, perform basic appliance diagnosis, estimate repair costs, and find nearby appliance service shops.

The application combines a React frontend with a FastAPI backend and a database to provide a simple and user-friendly appliance management experience.

---

## 🚀 Features

### 🔐 User Authentication
- User registration with name and password
- User login
- Password visibility toggle
- User profile display
- Logout functionality

### 🏠 Appliance Management
- Add household appliances
- View registered appliances
- Store appliance details such as:
  - Appliance name
  - Category
  - Brand
  - Model
  - Purchase year
  - Warranty information
  - Notes

### 🩺 Smart Diagnosis
- Select an appliance category
- Enter the appliance symptom/problem
- Generate possible causes
- Display safe troubleshooting checks
- Provide an estimated repair cost range
- Show repair recommendations

### 📍 Nearby Service Shops
- Find nearby appliance repair shops
- Opens Google Maps with appliance repair shop search
- Helps users locate local repair services

### 💬 HomeFix Assistant
- Interactive chatbot interface
- Personalized greeting using the logged-in user's name
- Provides a simple interface for appliance-related assistance

### 🎨 Modern UI
- Responsive React interface
- Dark/glassmorphism-inspired design
- Interactive cards and buttons
- Responsive layout for different screen sizes

---

## 🛠️ Technologies Used

### Frontend
- React.js
- Vite
- JavaScript
- HTML5
- CSS3
- Axios

### Backend
- Python
- FastAPI
- SQLAlchemy
- Pydantic
- Uvicorn

### Database
- SQLite – local development
- PostgreSQL – deployment configuration

### Tools
- Visual Studio Code
- Git
- GitHub
- npm
- Render
- Google Maps

---

## 🏗️ Project Architecture

```text
HomeFix
│
├── backend
│   ├── app
│   │   ├── main.py
│   │   ├── database.py
│   │   ├── models.py
│   │   ├── schemas.py
│   │   │
│   │   ├── routers
│   │   │   ├── auth.py
│   │   │   ├── appliances.py
│   │   │   └── diagnosis.py
│   │   │
│   │   └── services
│   │
│   ├── requirements.txt
│   └── homefix.db
│
├── frontend
│   ├── src
│   │   ├── components
│   │   ├── pages
│   │   ├── App.jsx
│   │   └── main.jsx
│   │
│   ├── package.json
│   └── vite.config.js
│
└── README.md