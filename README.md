# 🌍 Disaster Allocation System

A smart disaster management platform that helps authorities efficiently allocate resources during emergencies like floods, earthquakes, and fires. The system uses real-time data, priority-based logic, and location intelligence to ensure fast and effective response.

---

## 🚀 Key Features

- 🔐 Admin login for disaster authorities  
- 🌪️ Disaster creation (type, location, severity)  
- 📦 Resource management (food, medical kits, rescue teams, vehicles)  
- 👨‍🚒 Volunteer updates from ground teams  
- 🧠 Smart resource allocation (priority-based)  
- 📍 Map-based visualization  
- 📊 Dashboard with tracking & analytics  

---

## 🔁 System Workflow

### STEP 1: Admin Login
- Authority logs into the system  
- Creates a disaster event:
  - Type (Flood, Earthquake, Fire)  
  - Location  
  - Severity level  
👉 System enters **Active Disaster Mode**

---

### STEP 2: Resource Data Upload
- Admin / NGOs add resources:
  - Food  
  - Medical Kits  
  - Rescue Teams  
  - Vehicles  

Each resource includes:
- Quantity  
- Current location  
- Availability status  

---

### STEP 3: Ground Team Updates
- Volunteers update:
  - Number of affected people  
  - Urgency level  
  - Medical requirements  

👉 Data stored in backend  

---

### STEP 4: Smart Allocation Logic
- System:
  - Prioritizes areas (severity + population)  
  - Finds nearest resources  
  - Suggests shortest routes  

📍 Map shows:
- Affected areas  
- Resource locations  
- Delivery paths  

---

### STEP 5: Monitoring & Tracking
- Admin dashboard:
  - Resource movement  
  - Pending requests  
  - Completed deliveries  

📊 Charts:
- Resource usage  
- Area-wise distribution  

---

## 🛠️ Tech Stack

### Frontend
- HTML  
- CSS  
- JavaScript  
- Map Integration  

### Backend
- FastAPI  
- Python 3.11  
- MongoDB  
- PyMongo  
- Uvicorn  
- Swagger UI  

---

## ⚙️ Installation & Setup

### 1. Clone Repository
git clone https://github.com/your-username/Disaster-Allocation-System.git

cd Disaster-Allocation-System


### 2. Install Dependencies

pip install fastapi uvicorn pymongo



### 3. Run Server

uvicorn app.main:app --reload



### 4. Open API Docs

http://127.0.0.1:8000/docs

---

## 🧠 Core Concepts

- Priority-based allocation  
- Location-based optimization  
- Real-time data handling  
- RESTful APIs  



## 🤝 Contributing

Feel free to fork and contribute 🚀



## 📄 License

Open-source and free to use.
