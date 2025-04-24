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
