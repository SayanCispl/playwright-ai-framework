# ---------------------------------------------------------
# Dockerfile for Playwright + Copilot QA Framework
# ---------------------------------------------------------

# ✅ Use Playwright’s official Python image (includes browsers + deps)
# This avoids manual apt-get installs and ensures stability
FROM mcr.microsoft.com/playwright/python:v1.42.0-focal

# ✅ Set working directory inside the container
WORKDIR /app

# ✅ Copy all project files into the container
COPY . .

# ✅ Install Python dependencies from requirements.txt
# --no-cache-dir prevents caching to keep image size small
RUN pip install --no-cache-dir -r requirements.txt

# ✅ Expose MCP server port (used for Copilot integration)
EXPOSE 8001

# ✅ Default command: start MCP server
# You can override this in docker-compose to run tests instead
CMD ["python", "mcp_server/server.py"]
