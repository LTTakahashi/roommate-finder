<!--
  Roommate Finder – README
  ============================================================
  A Django + PostgreSQL + Redis web platform for matching
  compatible roommates with advanced search & real-time chat.
-->

<p align="center">
  <img src="docs/banner.png" width="750" alt="Roommate Finder banner">
</p>

# Roommate Finder

Roommate Finder streamlines the hunt for a compatible roommate by combining:

* **Rich profiles** (age, location radius, bio, photo)  
* **Advanced search** with PostGIS distance filtering  
* **Real-time chat** (WebSockets) with message history  
* **Mobile-first UI** (Bootstrap 5 + HTMX)

| CI Status | Coverage | License | Demo |
|-----------|----------|---------|------|
| ![ci](https://github.com/your-org/roommate-finder/actions/workflows/ci.yml/badge.svg) | ![cov](https://img.shields.io/badge/coverage-96%25-brightgreen) | MIT | <https://roommate-finder.onrender.com> |

---

## 🗺 Table of Contents
1. [Architecture](#architecture)
2. [Feature Tour](#feature-tour)
3. [Tech Stack](#tech-stack)
4. [Quick Start](#quick-start)
   * [Prerequisites](#prerequisites)
   * [Environment Variables](#environment-variables)
   * [Local Setup](#local-setup)
5. [Developer Guide](#developer-guide)
   * [Run Unit Tests](#run-unit-tests)
   * [Lint & Formatting](#lint--formatting)
   * [Load Testing](#load-testing)
6. [Deployment](#deployment)
7. [Contributing](#contributing)
8. [License](#license)
9. [Authors & Acknowledgements](#authors--acknowledgements)

---

## Architecture

```text
Browser  <--HTTPS/WebSocket-->  Render Container (Django + Daphne)
                                    │
                                    ├─ Redis  ⟵⟶  Celery workers  (async mail)
                                    ├─ PostgreSQL + PostGIS
                                    └─ AWS S3  (media & static)

    Clean-architecture layers – presentation ► application service ► domain ► infrastructure

    Observer pattern – Redis Pub/Sub broadcasts new chat messages

    Repository pattern – decouples Django ORM from domain logic

Feature Tour
Feature	Description	Status
User registration / login	Argon2-hashed pw, email verification	✔
Profile CRUD	Bio, age, location, photo w/ thumbnail	✔
Advanced search	Radius slider (PostGIS ST_DWithin) + keyword	✔
Real-time chat	WebSockets, history preload, unread badges	✔
Password reset	Tokenized email (24 h expiry)	✔
Responsive UI	Lighthouse mobile score ≥ 90	✔
Zero-downtime deploy	Blue-green on Render.com	✔

Screenshots live in docs/.
Tech Stack
Layer	Technology
Front-end	Django Templates · HTMX · Alpine.js · Bootstrap 5
Back-end	Django 4 · Daphne (ASGI) · Channels 4
Data	PostgreSQL 15 · PostGIS 3 · Redis 6
DevOps	Render.com · GitHub Actions · Docker
Testing	PyTest-cov · Cypress · Locust
Quick Start
Prerequisites

# Ubuntu / macOS
python3.11   # or use pyenv
postgresql   # 15+
redis-server # 6+

Environment Variables

Create .env in the project root:

# Django
DJANGO_SECRET=replace-me
DEBUG=True

# DB
POSTGRES_DB=roommate
POSTGRES_USER=roommate
POSTGRES_PASSWORD=roommate
POSTGRES_HOST=localhost
POSTGRES_PORT=5432

# Email (Amazon SES example)
EMAIL_HOST=email-smtp.us-west-2.amazonaws.com
EMAIL_HOST_USER=AKIA...
EMAIL_HOST_PASSWORD=...
EMAIL_PORT=587

Local Setup

git clone https://github.com/your-org/roommate-finder.git
cd roommate-finder

python -m venv .venv && source .venv/bin/activate
pip install -U pip wheel
pip install -r requirements/local.txt

# Database
createdb roommate
python manage.py migrate
python manage.py loaddata fixtures/dev_seed.json

# Run dev server (ASGI)
python manage.py runserver
# open http://127.0.0.1:8000

Developer Guide
Run Unit Tests

pytest -q --cov=.

Generates htmlcov/index.html (coverage target ≥ 95 %).
Lint & Formatting

ruff check .
black --check .

Load Testing

locust -f loadtest/locustfile.py --headless -u 100 -r 20 -t 5m

Deployment

Render automatically builds Dockerfile:

# Production image
docker build -t roommate:prod -f Dockerfile .
docker run -p 8000:8000 --env-file .env.prod roommate:prod

    Collectstatic → S3 (via django-storages)

    Database URL + Redis URL injected via Render dashboard

    Blue-green swap guarantees zero downtime

Contributing

    Fork the repo → create feature branch: git checkout -b feat/awesome

    Commit with conventional commits: feat(ui): add dark-mode toggle

    Push and open a pull request
    – CI must pass (pytest, ruff, black, cypress run)
    – At least one approving review required

License

This project is licensed under the MIT License – see LICENSE.
Authors & Acknowledgements

    Luiz Takahashi – full-stack dev · PostGIS queries

    Keagen Chapman – front-end UI/UX · Bootstrap theming

    Chris Flores – chat subsystem · DevOps pipeline

Special thanks to Prof. Parteek Kumar (WSU CPT S 322) for guidance.
<p align="center">Made with ☕ + 💻 at Washington State University</p> ```
