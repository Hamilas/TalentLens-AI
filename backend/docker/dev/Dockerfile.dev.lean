FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV PYTHONPATH=/code

RUN apt-get update \
    && apt-get install -y --no-install-recommends gcc postgresql-client curl \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /code

# Install only the lightweight core deps — skip torch/chromadb/sentence-transformers
RUN pip install --no-cache-dir \
    fastapi>=0.109.1 \
    "uvicorn[standard]>=0.27.0" \
    pydantic>=2.6.1 \
    pydantic-settings>=2.0.3 \
    sqlalchemy>=2.0.25 \
    asyncpg>=0.29.0 \
    psycopg2-binary>=2.9.9 \
    alembic>=1.13.1 \
    python-dotenv>=1.0.0 \
    httpx>=0.26.0 \
    greenlet>=2.0.2 \
    python-json-logger>=2.0.7 \
    aiosqlite>=0.20.0 \
    numexpr>=2.11.0 \
    langgraph>=0.3.0 \
    langchain>=0.3.0 \
    langchain-anthropic>=0.3.0 \
    langchain-community>=0.3.0 \
    langchain-core>=0.3.0 \
    langchain-openai>=0.3.0 \
    langchain-groq>=0.2.0 \
    langchain-chroma>=0.1.0 \
    chromadb>=0.5.0 \
    ddgs>=6.0.0

COPY . .

EXPOSE 8000

CMD ["uvicorn", "src.app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
