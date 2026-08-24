# ProductIQ-AI

### AI-Powered Product Intelligence & Semantic Search Platform

 **ProductIQ-AI** is an intelligent product discovery platform that understands natural-language shopping queries, extracts relevant product attributes, applies price constraints, and ranks products using NLP-based semantic relevance scoring.

## Overview

Traditional product search systems often depend on exact keyword matching. This can produce poor results when users describe what they want using natural language.

a user can ask:

```text
I need comfortable black formal shoes for office under ₹3000.
```

ProductIQ-AI processes this query using NLP techniques to identify important product attributes and constraints, retrieves matching products from MySQL, and ranks the results according to their textual relevance.

The platform combines:

* Natural Language Processing
* Named/entity-style attribute extraction
* Price constraint extraction
* SQL-based product filtering
* TF-IDF vectorization
* Cosine similarity
* Relevance-based ranking
* FastAPI backend
* Interactive UI


##  Problem Statement

E-commerce users do not always search using structured filters.

A conventional search engine may expect:

```text
Color = Black
Category = Shoes
Style = Sports
Max Price = ₹3000
```

However, users naturally express the same requirement as:

```text
I need black sports shoes below 3000
```

ProductIQ-AI bridges this gap by converting natural-language queries into structured search constraints and relevance signals.


##  System Architecture

```text
                    ┌──────────────────────┐
                    │       User           │
                    │ Natural Language     │
                    │ Product Query        │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │      UI Layer        │
                    │   Streamlit / UI     │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │     FastAPI API      │
                    │   /search endpoint   │
                    └──────────┬───────────┘
                               │
                 ┌─────────────┴─────────────┐
                 │                           │
                 ▼                           ▼
       ┌──────────────────┐       ┌──────────────────┐
       │  Price Parser    │       │ Entity Extractor │
       │     spaCy        │       │      spaCy       │
       └────────┬─────────┘       └────────┬─────────┘
                │                          │
                └────────────┬─────────────┘
                             │
                             ▼
                   ┌────────────────────┐
                   │   MySQL Database   │
                   │ Product Filtering  │
                   └──────────┬─────────┘
                              │
                              ▼
                   ┌────────────────────┐
                   │   TF-IDF Engine    │
                   │ Vectorization      │
                   └──────────┬─────────┘
                              │
                              ▼
                   ┌────────────────────┐
                   │ Cosine Similarity  │
                   │ Relevance Scoring  │
                   └──────────┬─────────┘
                              │
                              ▼
                   ┌────────────────────┐
                   │ Product Ranking    │
                   │ Top 3 Results      │
                   └──────────┬─────────┘
                              │
                              ▼
                   ┌────────────────────┐
                   │   UI Response      │
                   │ Ranked Products    │
                   └────────────────────┘
```



##  Technology Stack

| Technology               | Purpose                              |
| ------------------------ | ------------------------------------ |
| **Python**               | Core programming language            |
| **FastAPI**              | REST API backend                     |
| **spaCy**                | NLP processing and entity extraction |
| **scikit-learn**         | TF-IDF and cosine similarity         |
| **MySQL**                | Product data storage                 |
| **SQLAlchemy**           | Database ORM                         |
| **Streamlit / UI Layer** | Interactive frontend                 |
| **Uvicorn**              | ASGI server                          |
| **Pydantic**             | Request/response validation          |



##  Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/krishkydv77/ProductIQ-AI.git
cd ProductIQ-AI
```

### 2. Create a Virtual Environment

Windows:

```bash
python -m venv .venv
```

Activate:

```bash
.venv\Scripts\activate
```


### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Install the spaCy English Model

```bash
python -m spacy download en_core_web_sm
```

## 🗄️ Database Configuration

Configure your database credentials using environment variables.

Example:

```env
DB_HOST=localhost
DB_PORT=3306
DB_USER=root
DB_PASSWORD=your_password
DB_NAME=productiq
```


##  Running the Application

### Start the FastAPI Backend

```bash
uvicorn main:app --reload
```


### Start the UI

Run:

```bash
streamlit run ui.py
```


## ⚡ Run Backend + UI Together

The repository includes:

```text
start.bat
```

which can be used to simplify local startup on Windows.

You can configure it to start both the FastAPI backend and UI from a single command.

---



##  Current Capabilities

ProductIQ-AI currently demonstrates:

* Natural-language product search
* NLP attribute extraction
* Price constraint extraction
* MySQL product retrieval
* SQL-based filtering
* TF-IDF feature representation
* Cosine similarity scoring
* Relevance-based ranking
* Top-K product retrieval
* FastAPI REST API
* Interactive product search UI


##  Project Highlights

ProductIQ-AI demonstrates practical implementation of:

```text
NLP
+
Information Retrieval
+
Machine Learning
+
REST API Development
+
Database Integration
+
Frontend Integration
```

It is designed as a practical example of how natural-language understanding can be combined with traditional information-retrieval techniques to build an intelligent product discovery system.

