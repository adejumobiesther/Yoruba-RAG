# Yoruba-RAG

## Overview

Yoruba-RAG is a project aimed at enhancing the responses of large language models, such as GPT-3, when they interact with questions in low-resource languages like Yoruba.

## Project Steps

### 1. Web Scraping

To gather relevant data, I performed web scraping from a [Yorubablog] (https://www.theyorubablog.com/) using the Beautiful Soup library. The scraped data was then saved to a text file for further processing.

### 2. Data Chunking

To optimize data processing, I divided the collected data into smaller, manageable chunks using Langchain's recursive text splitter. This step was crucial for efficient handling of the Yoruba text.

### 3. Language-Agnostic BERT Sentence Embedding (LaBSE)

I utilized the Language-agnostic BERT Sentence Embedding (LaBSE) model by Google, known for its multilingual capabilities and strong comprehension of Yoruba. LaBSE was employed to embed the text data, resulting in rich contextual embeddings.

### 4. Chroma Database

The embedded text data was stored in a Chroma database, providing a structured and efficient storage solution. This database served as the foundation for improved language model responses.

## Achievements

By enriching the database with LaBSE embeddings, GPT's responses to questions in Yoruba have significantly improved. The model now demonstrates enhanced proficiency in handling inquiries in low-resource languages, making it a valuable tool for linguistic interactions.
