# 30-Day Senior Python Challenge

A comprehensive 40-day challenge designed to level up your Python skills to senior level. Each day focuses on a specific advanced concept or real-world application.

## Challenge Structure

### WEEK 1 — Core Architecture, Patterns, and Testing
Clean code, architecture, and extensibility fundamentals.

| Day | Challenge | Advanced Twist |
|-----|-----------|----------------|
| 1 | LRU Cache | Add Redis-backed persistence |
| 2 | Custom JSON Parser | Support nested objects + arrays |
| 3 | Dependency Injection Container | Add decorators for autowiring |
| 4 | Command Pattern Undo/Redo | Use event sourcing to persist states |
| 5 | Context Manager | Add async context support |
| 6 | Unit Testing Framework | Add parallel test execution |
| 7 | Legacy Refactor | Introduce SOLID and Type Hints refactor |

### WEEK 2 — Concurrency, Async, and Parallelism
Master async I/O, multiprocessing, and thread safety.

| Day | Challenge | Advanced Twist |
|-----|-----------|----------------|
| 8 | Async Web Crawler | Add rate limiting and error retry logic |
| 9 | Thread-Safe Cache | Benchmark vs Redis |
| 10 | Producer-Consumer System | Add message prioritization |
| 11 | Async Job Scheduler | Include cron-based job expressions |
| 12 | Batch Runner | Add backoff strategy and metrics |
| 13 | Benchmark CPU vs I/O | Visualize results via matplotlib |
| 14 | Parallel File Compressor | Add checksum validation |

### WEEK 3 — Microservices & Backend Systems
Design production-grade APIs and distributed backends.

| Day | Challenge | Advanced Twist |
|-----|-----------|----------------|
| 15 | URL Shortener | Add analytics dashboard |
| 16 | Auth System | Add OAuth2 + Refresh Tokens |
| 17 | Microservices | Implement gRPC between services |
| 18 | Message Queue | Add persistent message replay |
| 19 | Async File Upload | Use background tasks with Celery |
| 20 | Rate Limiter | Add Redis and IP-based rules |
| 21 | CLI API Client | Support interactive mode |

### WEEK 4 — Data, Analytics, and Observability
Big-data handling and distributed processing.

| Day | Challenge | Advanced Twist |
|-----|-----------|----------------|
| 22 | Log Analyzer (10M Rows) | Optimize with mmap + chunking |
| 23 | Event Notification | Add WebSocket push |
| 24 | Plugin Parser | Support live plugin hot-reload |
| 25 | Stream Aggregator | Simulate Kafka stream |
| 26 | Mini ORM | Add query caching layer |
| 27 | Rule Engine | Add dynamic rule persistence |
| 28 | Observability Toolkit | Export Prometheus metrics |
| 29 | Monorepo Refactor | Add shared package + lint pipeline |
| 30 | Distributed Analytics Platform | Include API + Web Dashboard |

### WEEK 5 — Advanced Bonus Projects (for Senior/Architect Track)
Extended challenges for those seeking architect-level expertise.

| Day | Project | What It Tests |
|-----|---------|---------------|
| 31 | 🧩 Realtime Chat Server (FastAPI + WebSockets) | Concurrency, pub/sub, session handling |
| 32 | ⚙️ Custom Task Queue Engine (like Celery) | Threading, job state persistence |
| 33 | 💾 In-Memory Time-Series Database | Data structures, memory optimization |
| 34 | 📬 GraphQL API Gateway | Schema stitching, query resolution |
| 35 | 🧠 Machine Learning API Wrapper | Model serving + async inference |
| 36 | ☁️ Dockerized Multi-Service Deployment | DevOps + architecture |
| 37 | 📡 ETL Pipeline (Extract → Transform → Load) | File streaming, data integrity |
| 38 | 🕵️ Event Log Replay Simulator | Replay system for debugging |
| 39 | 🔐 Access Control Middleware System (RBAC) | Security, permissions, policy design |
| 40 | 🚀 Final Capstone: AI-Driven Analytics Cloud | Combine everything — full platform with API, tasks, and data pipelines |

## Project Structure

- Week 1: Core Foundations (7 days)
- Week 2: Concurrency and Asynchronous Programming (7 days)
- Week 3: Backend Architecture (7 days)
- Week 4: Data Systems (9 days)
- Week 5: Advanced Bonus Projects (10 days)

## Getting Started

Each day's challenge is contained in its own directory with all necessary files and instructions. Follow the daily challenges sequentially for the best learning experience.

## Prerequisites

- Python 3.8+
- Understanding of basic Python concepts
- Familiarity with pip and virtual environments

## Installation

```bash
pip install -r requirements.txt
```