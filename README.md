🚀 AI‑Powered QA Automation: Playwright meets GitHub Copilot for smarter, faster testing.

![Python](https://img.shields.io/badge/python-3.10%2B-blue)
![Pytest](https://img.shields.io/badge/tested_with-pytest-green)
![Playwright](https://img.shields.io/badge/Playwright-Python-orange)
![Docker](https://img.shields.io/badge/docker-ready-lightblue)

## 📖 Overview

A comprehensive QA automation framework built with Python + Playwright + Pytest, enhanced by Allure reporting, a mock MCP (Model Context Protocol) server, and GitHub Copilot as the AI agent.
This project demonstrates end‑to‑end QA workflows:

Page Object Model (POM)

Parallel execution

Evidence capture (screenshots, logs)

API validation

AI‑driven test case generation powered by Copilot

🖼️ Architecture Diagram Preview
The diagram includes:

Playwright for UI automation

MCP Server as the bridge to GitHub Copilot

GitHub Copilot generating AI-driven test cases

API Testing Layer validating backend endpoints

Allure Reporting aggregating results from both UI and API tests

Arrows showing data flow and interaction between components

It demonstrates **login, add-to-cart, and checkout flows** on a demo website, with logs, screenshots, and HTML reports.

---

playwright_ai_framework/
├── api/                   # API client layer
├── config/                # Configs (URLs, credentials, paths)
├── pages/                 # Page Object Models
├── tests/                 # UI + API test suites
├── mcp_server/            # MCP server bridging Copilot
├── logs/                  # Test run logs
├── reports/               # Allure raw results
├── screenshots/           # Captured evidence
├── main.py                # Entry point
└── pytest.ini             # Pytest markers & config

🔧 Features
🧩 Page Object Model (POM) for scalable UI automation

🤖 GitHub Copilot Integration via MCP server for AI‑driven test generation

📊 Allure Reporting with step breakdowns, screenshots, and severity levels

⚡ Parallel Execution with pytest-xdist

🔌 API Testing Layer covering product list, user registration, login, and search endpoints

🖥️ Centralized Entry Point (main.py) to run server, tests, or both

🤖 MCP Server + Copilot
The MCP server bridges GitHub Copilot with your QA framework.
Copilot acts as the AI agent, generating recruiter‑ready test cases and demo scripts.

Sample Request:
curl -X POST http://127.0.0.1:8001/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d '{"model":"copilot","messages":[{"role":"user","content":"Generate login test cases"}],"max_tokens":800}'

Sample Response:
{
  "choices": [
    {
      "message": {
        "content": "GitHub Copilot Agent: Generated test cases for -> Generate login test cases"
      }
    }
  ]
}

📊 Allure Reporting (Enhanced)
Allure transforms raw pytest results into a visual dashboard with:

Features & Stories → group tests by functionality (Authentication, Cart, Checkout).

Severity Levels → highlight importance (BLOCKER, CRITICAL, NORMAL).

Step Breakdown → login → add to cart → checkout flows.

Evidence Attachments → screenshots, URLs, JSON payloads.

Failure Evidence → automatic screenshots on test failure.

🔌 API Testing Layer
Endpoints covered:

GET /api/productsList → All products

POST /api/createAccount → Register user

POST /api/verifyLogin → Verify login

POST /api/searchProduct → Search products

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


👉 This README now explains MCP server AI agent integration in detail, shows how Allure captures evidence, and highlights parallel execution optimizations.

## 👤 Author

Sayan Koley — QA Automation Specialist. Persistent, practical, and focused on recruiter‑ready frameworks.

## 📜 License

MIT License – free to use and adapt.
