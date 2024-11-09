# Karyotype Analyzer

This project aims to automate cytogenetic analysis of human karyotypes using AI to identify and classify chromosomal aberrations.

## Setup
1. Clone the repository
2. Create a virtual environment: `python3 -m venv venv`
3. Activate the virtual environment: `source venv/bin/activate`
4. Install dependencies: `pip install -r requirements.txt`

## Running the application
```
python src/main.py
```

## Project Structure
- `src/`: Contains the main source code
  - `main.py`: Entry point of the application
  - `gui.py`: GUI implementation using PyQt5
  - `image_processor.py`: Image processing functions
  - `ai_model.py`: AI model implementation using TensorFlow
  - `database.py`: Database operations using SQLite
- `tests/`: Contains test files
- `data/`: Directory for storing data files and datasets

## Dependencies
- PyQt5
- TensorFlow
- Pillow
- NumPy
- SciPy
- Matplotlib
