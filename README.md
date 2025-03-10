# Kidney-Disease-Detection-ML-Application
End-to-End ML Application, with deployment via CI/CD pipelines and best MLOps Practices
 
This project leverages machine learning algorithms to predict the presence of kidney disease in patients. It encompasses the entire machine learning lifecycle, from data preprocessing and model training to deployment and continuous integration/continuous deployment (CI/CD). The application is built with a modular architecture, ensuring scalability and maintainability.

## Technologies Used

- **Machine Learning / Deep Learning Frameworks**: Scikit-learn, TensorFlow, CNN
- **Programming Languages**: Python
- **Web Framework**: Flask
- **Containerization**: Docker
- **Version Control**: Git
- **Continuous Integration/Continuous Deployment (CI/CD)**: GitHub Actions
- **Experiment Tracking**: MLflow
- **Data Version Control**: DVC

## 📁 Project Structure

The project is organized as follows:

```

Kidney-Disease-Detection-ML-Application/
├── .dvc/                  # DVC configuration files
├── .github/workflows/     # GitHub Actions workflows
├── config/                # Configuration files
├── mlruns/                # MLflow experiment logs
├── model/                 # Serialized models
├── research/              # Notebooks and research materials
├── src/
│   └── mypackage/         # Source code package
├── templates/             # HTML templates for Flask
├── app.py                 # Flask application
├── dockerfile             # Docker configuration
├── dvc.yaml               # DVC pipeline definition
├── params.yaml            # Hyperparameters and configurations
├── requirements.txt       # Python dependencies
├── setup.py               # Package setup
└── README.md              # Project documentation
```


## Installation

To set up the project locally, follow these steps:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/SayamKhatri/Kidney-Disease-Detection-ML-Application.git
   ```


2. **Navigate to the project directory**:
   ```bash
   cd Kidney-Disease-Detection-ML-Application
   ```


3. **Create and activate a virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```


4. **Install the required dependencies**:
   ```bash
   pip install -r requirements.txt
   ```


## Usage

1. **Data Version Control**: Ensure DVC is installed and configured. Pull the latest data version:
   ```bash
   dvc pull
   ```


2. **Run the application**:
   ```bash
   python app.py
   ```



## Deployment

The application is containerized using Docker for consistent deployment across environments.

1. **Build the Docker image**:
   ```bash
   docker build -t kidney-disease-detection .
   ```


2. **Run the Docker container**:
   ```bash
   docker run -p 5000:5000 kidney-disease-detection
   ```

   The application will be accessible at `http://localhost:5000/`

   ![image](https://github.com/user-attachments/assets/6e65de9b-de95-432d-85c5-515f447f02dc)




## 📄 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

# Snippets

<img width="1470" alt="Screenshot 2025-03-05 at 4 43 18 PM" src="https://github.com/user-attachments/assets/d5aab087-2449-44ec-9679-35818a5a3eda" />

