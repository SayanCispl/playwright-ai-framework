# Playwright AI-Assisted QA Framework 🚀

![Python](https://img.shields.io/badge/python-3.10%2B-blue)
![Pytest](https://img.shields.io/badge/tested_with-pytest-green)
![Playwright](https://img.shields.io/badge/Playwright-Python-orange)
![Docker](https://img.shields.io/badge/docker-ready-lightblue)
![GitHub](https://img.shields.io/badge/version-control-git-black)


```---

## 📖 Overview

This project is a **hybrid QA automation framework** combining:

- **Playwright CLI** for browser automation and test execution
- **Pytest** for structured test cases
- **AI Agent** for assisted test generation and adaptation
- **Docker** for containerized CI/CD runs
- **GitHub** for version control and portfolio visibility

It demonstrates **login, add-to-cart, and checkout flows** on a demo website, with logs, screenshots, and HTML reports.

---

## 🔀 Hybrid Framework Concept: CLI + AI Agent

The framework is designed to balance **efficiency** and **intelligence**:

- **AI Agent Layer**

  - Generates new test cases (e.g., login, checkout) using natural language prompts.
  - Adapts existing tests when requirements change.
  - Consumes tokens only during generation/adaptation.
  - Example: “Generate a login test” → AI outputs a ready‑to‑run Pytest script.
- **Playwright CLI Layer**

  - Executes tests locally or in CI/CD pipelines.
  - Produces logs, screenshots, and HTML reports.
  - No token usage during execution.
  - Example: `pytest tests/ --html=reports/test-report.html`

**Workflow:**

1. AI Agent scaffolds or adapts test code.
2. Developer commits generated tests to GitHub.
3. Playwright CLI runs tests in Docker or CI/CD.
4. Reports and screenshots are shared with stakeholders.

This hybrid model ensures **cost‑efficient execution** while leveraging AI for **rapid test creation**.

```

---

## 🧱 Project Structure

playwright\_ai\_framework/

├── config/            # Config files

├── tests/             # Pytest test cases

├── pages/             # Page Object Model classes

├── utils/             # Logger & screenshot helpers

├── ai\_agent/          # AI-assisted test generation

├── reports/           # HTML reports

├── logs/              # Execution logs

├── Dockerfile         # Container setup

├── requirements.txt   # Dependencies

├── .gitignore         # Git ignore rules

└── README.md          # Project documentation

---

## ⚙️ Setup

### 1. Clone the repo

```bash
git clone https://github.com/<your-username>/playwright-ai-framework.git
cd playwright_ai_framework
---

2. Install dependencies

   pip install -r requirements.txt
   playwright install
3. Run tests

   pytest tests/ --headed --html=reports/test-report.html
4. 🐳 Docker Usage

### Build image

docker build -t playwright-ai-framework .

Run tests inside container

docker run --rm playwright-ai-framework

📸 Logs & Screenshots

* **Logs** → `logs/test_run.log`
* **Screenshots** → `screenshots/`
* **Reports** → `reports/test-report.html`

## 📌 Roadmap

* [ ]  Integrate Allure reports
* [ ]  Add CI/CD pipeline (GitHub Actions)
* [ ]  Expand test coverage (search, profile update)
* [ ]  AI-assisted test adaptation



## 👤 Author

Sayan Koley — QA Automation Specialist. Persistent, practical, and focused on recruiter‑ready frameworks.


## 📜 License

MIT License – free to use and adapt.
```
