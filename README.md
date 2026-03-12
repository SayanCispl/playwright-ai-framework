Playwright AI Framework with MCP Server & Allure Reporting ⚡

![Python](https://img.shields.io/badge/python-3.10%2B-blue)
![Pytest](https://img.shields.io/badge/tested_with-pytest-green)
![Playwright](https://img.shields.io/badge/Playwright-Python-orange)
![Docker](https://img.shields.io/badge/docker-ready-lightblue)

## 📖 Overview

A modern QA automation framework built with Python + Playwright + Pytest, enhanced by Allure reporting and a mock MCP (Model Context Protocol) server simulating AI agent integration.
This project demonstrates end‑to‑end automation workflows: Page Object Model (POM), parallel execution, evidence capture, and AI‑driven test case generation.

- **Playwright CLI** for browser automation and test execution
- **Pytest** for structured test cases
- **AI Agent** for assisted test generation and adaptation
- **Docker** for containerized CI/CD runs
- **GitHub** for version control and portfolio visibility

It demonstrates **login, add-to-cart, and checkout flows** on a demo website, with logs, screenshots, and HTML reports.

---

📂 Project Structure
playwright_ai_framework/
├── config/                # Configuration package
│   ├── __init__.py
│   └── config.py          # Base URLs, credentials, paths
├── pages/                 # Page Object Models (Login, Cart, Checkout)
├── tests/                 # Pytest test suites with Allure steps
├── mcp_server/            # Mock AI MCP server
│   └── server.py
├── logs/                  # Test run logs
├── reports/               # Allure raw results
├── screenshots/           # Captured evidence
├── main.py                # Entry point (server/tests/both)
└── pytest.ini             # Pytest markers & config

🤖 MCP Server & AI Agent Integration
The MCP server (mcp_server/server.py) simulates an AI agent that can generate test cases or respond to QA prompts.
Endpoint:
POST http://localhost:8001/v1/chat/completions
Sample Request:
curl -X POST http://127.0.0.1:8001/v1/chat/completions 
-H "Content-Type: application/json" 
-d '{"model":"demo","messages":[{"role":"user","content":"Generate login test cases"}],"max_tokens":800}'
Sample Response:
{
"choices": [
{
"message": {
"content": "Mock AI Agent: Generated test cases for -> Generate login test cases"
}
}
]
}
This allows you to plug AI‑driven test generation into your QA workflow. In CI/CD, the MCP server can be used to dynamically generate or validate test scenarios before execution.

📊 Allure Reporting (Enhanced)
Allure transforms raw pytest results into a visual dashboard with:

Features & Stories → group tests by functionality (Authentication, Cart, Checkout).

Severity Levels → highlight importance (BLOCKER, CRITICAL, NORMAL).

Step Breakdown → login → add to cart → checkout flows.

Evidence Attachments → screenshots, URLs, JSON payloads.

Failure Evidence → automatic screenshots on test failure.

⚙️ Running Locally

1. Setup environment
   python -m venv .venv
   source .venv/bin/activate
   pip install -r requirements.txt
   playwright install
2. Start MCP server
   python mcp_server/server.py
3. Run tests (desktop only, parallel)
   pytest -m desktop -n auto --alluredir=reports/
4. View Allure report
   allure serve reports/

🐳 Run with Docker
docker-compose up --build

MCP server runs on http://localhost:8001

Playwright tests run in a separate container

Reports generated in reports/

🚀 Usage via main.py
python main.py

Options:

Run MCP server

Run tests

Run MCP server + tests together (multiprocessing)

🛠️ Optimized Parallel Execution
Only desktop tests run in parallel (-m desktop).

Mobile tests are commented out in pytest.ini and test files.

Use -n auto to maximize CPU utilization.

✅ Next Steps
Add CI/CD pipeline (GitHub Actions) to auto‑run tests and publish Allure reports.

Re‑enable mobile tests when device/browser matrix is ready.

Extend config/ for environment‑specific configs (dev, staging, prod).

👉 This README now explains MCP server AI agent integration in detail, shows how Allure captures evidence, and highlights parallel execution optimizations.

## 👤 Author

Sayan Koley — QA Automation Specialist. Persistent, practical, and focused on recruiter‑ready frameworks.

## 📜 License

MIT License – free to use and adapt.
