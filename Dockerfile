FROM python:3.11-slim
HEALTHCHECK CMD curl -f http://localhost:8000/health || exit 1
