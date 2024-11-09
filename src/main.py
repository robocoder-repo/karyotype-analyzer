import sys
import os
import tensorflow as tf
from PyQt5.QtWidgets import QApplication
from gui import MainWindow
from ai_model import create_model

def load_model():
    model = create_model()
    # TODO: Load pre-trained weights here
    # model.load_weights('path_to_weights.h5')
    return model

def main():
    # Set the current working directory to the script's directory
    os.chdir(os.path.dirname(os.path.abspath(__file__)))

    # Enable memory growth for GPU
    physical_devices = tf.config.list_physical_devices('GPU')
    if physical_devices:
        tf.config.experimental.set_memory_growth(physical_devices[0], True)

    app = QApplication(sys.argv)
    
    # Load the model
    model = load_model()
    
    # Create and show the main window
    window = MainWindow(model)
    window.show()
    
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
