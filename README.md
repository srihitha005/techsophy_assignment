# Techsophy Assignment — DevOps Team Productivity and Bottleneck Analyzer

## 🚀 Problem Statement

Build a system that analyzes development and deployment metrics to identify team productivity bottlenecks and suggest improvements.

---

## 💡 Features

- Workflow analysis (commit to PR, PR review, build, deployment stages)
- Bottleneck detection based on defined thresholds
- Automated improvement recommendations
- Modular architecture with clear separation of components
- API accessible via FastAPI

---

## 🛠️ Technologies Used

- Python
- FastAPI

---

## ⚙️ How to Run

### 1️⃣ Clone the repository

```bash
git clone https://github.com/srihitha005/techsophy_assignment.git
cd techsophy_assignment


2️⃣ Install dependencies
pip install -r requirements.txt

3️⃣ Run the API
uvicorn main:app --reload

4️⃣ Access endpoints
Base URL: http://127.0.0.1:8000
Analysis endpoint: http://127.0.0.1:8000/analyze


Example API Output
{
  "workflow_summary": {
    "avg_commit_to_pr": 2,
    "avg_pr_review": 24,
    "avg_build": 15,
    "avg_deploy": 45
  },
  "bottlenecks": [
    "PR review time is too high",
    "Deployment time is too high"
  ],
  "recommendations": [
    "Reduce PR review time by introducing code ownership, automating reviewer assignment, providing reviewer training, and tracking review SLAs in dashboards.",
    "Shorten deployment time by investing in deployment pipeline optimization, parallelizing steps, introducing advanced strategies like canary releases, and setting automated rollback policies."
  ]
}

