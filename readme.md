---

# 🏛️ AI-Powered Citizen Grievance Redressal Platform

### Smart Tamil Nadu – Digital Governance & Smart Cities Initiative

---

## 📌 Project Overview

The **AI-Powered Citizen Grievance Redressal Platform** is a smart governance solution designed to streamline complaint management for urban local bodies.

The system allows citizens to submit complaints related to:

* 🛣 Roads
* 💧 Water Supply
* ⚡ Electricity
* 🧹 Sanitation
* 🏢 Other civic issues

Using AI/ML, the platform automatically:

* Classifies complaints
* Assigns priority levels
* Routes them to relevant departments
* Tracks resolution timelines
* Ensures accountability and transparency

---

## 🎯 Problem Statement

Citizen complaints in municipalities are often:

* Manually classified
* Poorly tracked
* Delayed in resolution
* Lacking transparency

This results in:

* Frustrated citizens
* Department inefficiencies
* Poor accountability

---

## 💡 Solution

This platform:

* Accepts complaints via text and images
* Uses AI to auto-classify issue category
* Automatically assigns priority
* Provides real-time tracking dashboard
* Maintains department accountability with resolution time tracking

---

## 🏗️ System Architecture

```
Citizen (Web/Mobile)
        ↓
   FastAPI Backend
        ↓
 AI Classification Service
        ↓
   PostgreSQL Database
        ↓
 Admin Dashboard
```

---

## 🛠️ Tech Stack

### Backend

* FastAPI
* Uvicorn
* SQLAlchemy
* PostgreSQL

### AI / ML

* Python
* Scikit-learn
* TF-IDF Vectorizer
* Logistic Regression

### Frontend (Planned)

* React.js
* Tailwind CSS

### Deployment (Optional)

* AWS EC2 / Render / Railway

---

## 📂 Project Structure

```
grievance-backend/
│
├── app/
│   ├── main.py
│   ├── database.py
│   ├── models.py
│   ├── schemas.py
│   ├── routes/
│   │   ├── users.py
│   │   ├── complaints.py
│   ├── services/
│   │   ├── ai_classifier.py
│
├── requirements.txt
├── README.md
```

---

## 🚀 Getting Started

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/grievance-platform.git
cd grievance-platform
```

---

### 2️⃣ Create Virtual Environment

```bash
python -m venv venv
```

Activate:

**Linux/Mac**

```bash
source venv/bin/activate
```

**Windows**

```bash
venv\Scripts\activate
```

---

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

If requirements file not present:

```bash
pip install fastapi uvicorn sqlalchemy psycopg2-binary scikit-learn
```

---

### 4️⃣ Run the Server

```bash
uvicorn app.main:app --reload
```

Open:

* API: [http://127.0.0.1:8000](http://127.0.0.1:8000)
* Swagger Docs: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

---

## 📡 API Endpoints

### 🟢 Health Check

```
GET /health
```

---

### 🟢 Submit Complaint

```
POST /complaints
```

Request Body:

```json
{
  "user_id": 1,
  "description": "Large pothole near bus stand",
  "image_url": "optional"
}
```

Response:

```json
{
  "category": "Roads",
  "priority": "High",
  "status": "Pending"
}
```

---

### 🟢 Get All Complaints

```
GET /complaints
```

---

### 🟢 Update Complaint Status

```
PUT /complaints/{id}
```

---

## 🧠 AI Classification Logic

### Categories:

* Roads
* Water
* Electricity
* Sanitation
* Other

### Method:

* TF-IDF Vectorization
* Logistic Regression classifier

### Priority Rules:

* High: "accident", "danger", "fire", "leak"
* Medium: "broken", "not working"
* Low: "request", "suggestion"

---

## 🗄️ Database Schema

### Users Table

| Field | Type          |
| ----- | ------------- |
| id    | Integer       |
| name  | String        |
| email | String        |
| role  | Citizen/Admin |

---

### Complaints Table

| Field       | Type                         |
| ----------- | ---------------------------- |
| id          | Integer                      |
| user_id     | Foreign Key                  |
| description | Text                         |
| category    | String                       |
| priority    | String                       |
| status      | Pending/In Progress/Resolved |
| created_at  | Timestamp                    |
| resolved_at | Timestamp                    |

---

## 📊 Admin Dashboard Features (Planned)

* View complaints by category
* Filter by status
* Track resolution times
* SLA violation tracking
* Analytics:

  * Complaints per department
  * Average resolution time
  * High priority issue trends

---

## 🔒 Future Enhancements

* JWT Authentication
* Role-Based Access Control (RBAC)
* Voice-to-text complaint input
* Image-based issue detection (Computer Vision)
* Google Maps heatmap integration
* SMS/Email notifications
* SLA-based escalation system

---

## 📈 Expected Impact

* Reduced manual complaint routing
* Faster issue resolution
* Increased government accountability
* Data-driven civic planning
* Improved citizen satisfaction

---

## 🎓 Academic Value

This project demonstrates:

* Full-stack development
* REST API design
* AI/ML integration in production systems
* Database design
* Smart governance solutions
* Scalable backend architecture

---

## 👨‍💻 Author

Bala Murugan
Mini Project – Smart Governance Initiative
2026

---

## 📜 License

This project is for academic and research purposes.

---

---
