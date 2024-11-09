from PyQt5.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QPushButton, QLabel, QFileDialog, QTextEdit
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
from image_processor import process_karyotype_image
from ai_model import predict_karyotype, analyze_karyotype
from database import Database

class MainWindow(QMainWindow):
    def __init__(self, model):
        super().__init__()
        self.setWindowTitle("Karyotype Analyzer")
        self.setGeometry(100, 100, 800, 600)

        self.model = model
        self.db = Database()

        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)

        self.image_label = QLabel()
        self.image_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.image_label)

        load_button = QPushButton("Load Image")
        load_button.clicked.connect(self.load_image)
        layout.addWidget(load_button)

        analyze_button = QPushButton("Analyze Karyotype")
        analyze_button.clicked.connect(self.analyze_karyotype)
        layout.addWidget(analyze_button)

        self.result_text = QTextEdit()
        self.result_text.setReadOnly(True)
        layout.addWidget(self.result_text)

        self.current_image_path = None

    def load_image(self):
        file_name, _ = QFileDialog.getOpenFileName(self, "Open Image", "", "Image Files (*.png *.jpg *.bmp)")
        if file_name:
            self.current_image_path = file_name
            pixmap = QPixmap(file_name)
            self.image_label.setPixmap(pixmap.scaled(self.image_label.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation))

    def analyze_karyotype(self):
        if self.current_image_path:
            # Process the karyotype image
            processed_chromosomes = process_karyotype_image(self.current_image_path)
            
            # Predict chromosome classes
            predictions = predict_karyotype(self.model, processed_chromosomes)
            
            # Analyze the karyotype
            result = analyze_karyotype(predictions)
            
            # Display the result
            self.result_text.setText(result)
            
            # Save the analysis to the database
            self.db.insert_analysis(self.current_image_path, result)
        else:
            self.result_text.setText("Please load an image first.")
