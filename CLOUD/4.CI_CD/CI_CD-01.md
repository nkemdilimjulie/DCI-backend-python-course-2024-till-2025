# CI/CD

### **Continuous Integration (CI)**

- A **software development practice** where developers **frequently integrate** their code, often multiple times a day.  
- Each integration is **automatically built and tested** to detect errors quickly. 
- Provide **rapid feedback** on code changes. 
- Find and fix bugs **early**.  
- Improve **software quality**.
- Reduce **time to release** new updates. 

- **Frequent commits** from developers. 
- **Automated tests** to catch errors early.  
- **Reporting tools** to notify developers of build/test results.  

- CI is often **combined with Continuous Delivery (CD)** for a streamlined release process.

### **Continuous Deployment**

- **Extends Continuous Delivery** by **automatically deploying** changes **directly to production**.  
- Every successful change that passes all tests is **immediately released** to customers.  
- **No manual approval** is required before deployment. 
- Ensures **fast and frequent releases** with minimal human intervention. 

### **GitHub Actions: CI/CD Automation in GitHub**
- **GitHub Actions** is GitHub’s **CI/CD platform**, enabling **workflow automation** directly in GitHub repositories.

#### **Overview**
- **GitHub Actions** is GitHub’s **CI/CD platform**, enabling **workflow automation** directly in GitHub repositories.
- Automates tasks such as **testing, building, and deploying** code.
- Workflows are triggered by events like **code pushes, pull requests, and scheduled runs**.

```bash
name: Django CI

on:
  push:
    branches: [ "master" ]
  workflow_dispatch:

jobs:
  build:
    runs-on: ubuntu-latest
    services:
      postgres:
        image: postgres:14
        env:
          POSTGRES_USER: myprojectuser2
          POSTGRES_PASSWORD: password
          POSTGRES_DB: myproject
        ports:
          - 5432:5432


    steps:
      # Step 1: Checkout Code
      - name: Checkout Code
        uses: actions/checkout@v4

      # Step 2: Set up Python
      - name: Set up Python
        uses: actions/setup-python@v3
        with:
          python-version: '3.10'

      # Step 3: Install Dependencies
      - name: Install Dependencies
        run: |
          python -m pip install --upgrade pip
          pip install -r requirements.txt

      # Step 4: Set Environment Variables
      - name: Set Environment Variables
        run: echo "DATABASE_HOST=postgres" >> $GITHUB_ENV

      # Step 5: Run Migrations
      - name: Run Migrations
        run: python manage.py migrate

      # Step 6: Run Tests
      - name: Run Tests
        run: python manage.py test
```

### **GitHub Actions Workflow Breakdown**  

#### **Runs on a Virtual Machine (VM) (`ubuntu-latest` runner)**
- **`runs-on: ubuntu-latest`** → The workflow runs on a **GitHub-hosted VM**.  
- **Step 1: Checkout Code** (`uses: actions/checkout@v4`)  
  - **Clones the repository** into the VM.  
- **Step 2: Set up Python** (`uses: actions/setup-python@v3`)  
  - **Installs Python 3.10** on the VM.  
- **Step 3: Install Dependencies**  
  - Installs dependencies **inside the VM**.  
 
- **Step 5: Run Migrations**  
  - Runs `python manage.py migrate` **inside the VM** to apply database migrations.  
- **Step 6: Run Tests**  
  - Runs `python manage.py test` **inside the VM** to execute Django tests.  

---

#### **Runs in a Docker Container (PostgreSQL service)**
- **`services.postgres`**
  - **Starts a PostgreSQL 14 container** using Docker.  
  - The database runs in a separate **container** within the VM.  
- **PostgreSQL Environment Variables**  
  - `POSTGRES_USER=myprojectuser2`  
  - `POSTGRES_PASSWORD=password`  
  - `POSTGRES_DB=myproject`  
- **Database Connection**
  - The VM communicates with the **Postgres container** via `DATABASE_HOST=localhost`.  
  - Port **5432** is mapped for communication

