
# Visionary Data: Leveraging TruLens with MongoDB and LlamaIndex

This repository contains the code and resources for the tutorial on leveraging TruLens with MongoDB and LlamaIndex. The tutorial demonstrates how to integrate these powerful tools to create and manage visionary data projects.

## Table of Contents
- [Introduction](#introduction)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)

## Introduction
This tutorial guides you through the process of leveraging TruLens, MongoDB, and LlamaIndex to create a robust data management system. TruLens is a powerful framework for managing and visualizing data, MongoDB is a flexible NoSQL database, and LlamaIndex provides an efficient indexing mechanism.

## Prerequisites
Before you begin, ensure you have the following installed on your machine:
- Python 3.8 or higher
- MongoDB (Atlas or local instance)
- Git
- pip (Python package installer)

## Installation
Follow these steps to set up the project on your local machine:

1. **Clone the repository**
   ```bash
   git clone https://github.com/da-ros/CustomerCareSystem.git
   cd visionary-data
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows, use `venv\Scripts\activate`
   ```

3. **Install the required packages**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up MongoDB**
   - If using MongoDB Atlas, create a cluster and obtain the connection string.
   - If using a local instance, ensure MongoDB is running on your machine.

5. **Configure environment variables**
   Create a `.env` file in the root directory and add the following:
   ```env
   MONGODB_URI=mongodb+srv://<username>:<password>@cluster0.mongodb.net/<dbname>?retryWrites=true&w=majority
   OPENAI_API_KEY=sk-...
   ```

## Usage
Follow these steps to run the project:

1. **Start the application**
   ```bash
   python main.py
   ```

2. **Access the application**
   Open your web browser and navigate to `http://localhost:5000`.

3. **Interacting with TruLens and LlamaIndex**
   Use the web interface to manage your data, create indexes, and visualize your data using TruLens.

## Project Structure
Here is an overview of the project structure:

```
visionary-data/
│
├── .env                # Environment variables
├── requirements.txt    # Python dependencies
├── app.py              # Main application entry point
├── README.md           # Project documentation
```

## Contributing
We welcome contributions! Please read our [Contributing Guidelines](CONTRIBUTING.md) for more information on how to get started.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
