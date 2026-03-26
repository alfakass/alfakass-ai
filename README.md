# Project 1: Document Q&A System

## Overview

This project implements a Document Q&A System using Retrieval-Augmented Generation (RAG) pipeline. It allows users to upload documents (PDFs and text files) and ask natural language questions about their content. The system returns answers grounded in the documents with source references.

## Learning Objectives

This project covers foundational AI technologies:
- LLM API calls and prompt engineering
- Document parsing and text chunking
- Embeddings and vector search
- Vector database integration (recommended: pgvector)
- RAG pipeline implementation
- Basic evaluation of answer correctness

## Features

- **Document Upload**: Support for PDF and text file formats
- **Natural Language Queries**: Ask questions in plain English
- **Source-Referenced Answers**: Responses include citations from original documents
- **Modular Architecture**: Separates parsing, embedding, retrieval, and generation components

## Technologies Used

- **Language Model**: OpenAI API (configurable via environment variables)
- **Vector Database**: pgvector (PostgreSQL extension) for efficient similarity search
- **Embeddings**: OpenAI embeddings for document and query vectorization
- **Document Processing**: PDF parsing libraries (e.g., PyPDF2, pdfplumber)
- **Environment Management**: uv for dependency management

## Installation

1. **Prerequisites**:
   - Python 3.13+
   - PostgreSQL with pgvector extension
   - OpenAI API key

2. **Clone and Setup**:
   ```bash
   git clone <repository-url>
   cd project-1
   uv sync
   ```

3. **Environment Configuration**:
   Create a `.env` file with the following variables:
   ```
   INFERENCE_ENDPOINT=https://api.openai.com/v1
   GITHUB_API_KEY=your-openai-api-key-here
   MODEL=gpt-4  # or your preferred model
   DATABASE_URL=postgresql://user:password@localhost:5432/dbname
   ```

## Usage

1. **Run the Application**:
   ```bash
   uv run python main.py
   ```

2. **Upload Documents**:
   - Place PDF/text files in the `documents/` directory
   - The system will automatically parse and index them

3. **Ask Questions**:
   - Use the chat interface to ask questions about your documents
   - Receive answers with source references

## Dataset Recommendations

For immediate utility and familiar content, use your consultancy's internal documents:
- Past proposals
- Methodology documentation
- Client reports
- Internal knowledge bases

This ensures you can easily verify answer correctness and relevance.

## Evaluation

The project includes basic evaluation mechanisms to assess:
- Answer accuracy against ground truth
- Source citation validity
- Retrieval quality metrics

## Project Structure

```
project-1/
├── agent.py          # LLM interaction and RAG logic
├── main.py           # Application entry point
├── pyproject.toml    # Project dependencies and configuration
├── .env              # Environment variables (not committed)
├── .gitignore        # Git ignore rules
└── README.md         # This file
```

## Contributing

This is a learning project. Feel free to extend functionality with:
- Additional document formats
- Different embedding models
- Advanced chunking strategies
- Comprehensive evaluation suites

## License

[Add license information here]