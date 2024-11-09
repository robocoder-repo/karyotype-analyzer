# Karyotype Analyzer

This project aims to automate cytogenetic analysis of human karyotypes using AI to identify and classify chromosomal aberrations.

## Setup

1. Clone the repository:
   ```
   git clone https://github.com/ezrafchev/karyotype-analyzer.git
   cd karyotype-analyzer
   ```

2. Create a virtual environment:
   ```
   python3 -m venv venv
   ```

3. Activate the virtual environment:
   - On Windows:
     ```
     venv\Scripts\activate
     ```
   - On macOS and Linux:
     ```
     source venv/bin/activate
     ```

4. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

## Running the application

To run the application in development mode:

```
python src/main.py
```

## Building the executable

To build the executable for Windows:

1. Ensure you have PyInstaller installed:
   ```
   pip install pyinstaller
   ```

2. Run the build script:
   ```
   python build.py
   ```

3. The executable will be created in the `build` directory.

## Project Structure

- `src/`: Contains the main source code
  - `main.py`: Entry point of the application
  - `gui.py`: GUI implementation using PyQt5
  - `image_processor.py`: Image processing functions
  - `ai_model.py`: AI model implementation using TensorFlow
  - `database.py`: Database operations using SQLite
- `tests/`: Contains test files (to be implemented)
- `data/`: Directory for storing data files and datasets
- `build.py`: Script to build the executable
- `requirements.txt`: List of Python dependencies

## TODO

- Implement unit tests
- Train the AI model with a large dataset of karyotype images
- Implement integration with laboratory robots for sample preparation
- Optimize image processing and AI model performance
- Enhance the user interface with more detailed analysis results and visualizations

## Contributing

Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details on our code of conduct, and the process for submitting pull requests to us.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.
