import tensorflow as tf
from tensorflow.keras import layers, models
import numpy as np

def create_model(input_shape=(224, 224, 3), num_classes=24):
    """
    Create a ResNet-based model for karyotype analysis.
    """
    base_model = tf.keras.applications.ResNet50(
        include_top=False,
        weights='imagenet',
        input_shape=input_shape
    )

    # Freeze the base model
    base_model.trainable = False

    model = models.Sequential([
        base_model,
        layers.GlobalAveragePooling2D(),
        layers.Dense(1024, activation='relu'),
        layers.Dropout(0.5),
        layers.Dense(num_classes, activation='softmax')
    ])

    return model

def train_model(model, train_data, validation_data, epochs=10):
    """
    Train the model on karyotype data.
    """
    model.compile(
        optimizer='adam',
        loss='categorical_crossentropy',
        metrics=['accuracy']
    )

    history = model.fit(
        train_data,
        validation_data=validation_data,
        epochs=epochs
    )

    return history

def predict_karyotype(model, preprocessed_chromosomes):
    """
    Predict the karyotype class for a given set of preprocessed chromosome images.
    """
    predictions = []
    for chromosome in preprocessed_chromosomes:
        prediction = model.predict(np.expand_dims(chromosome, axis=0))
        predicted_class = tf.argmax(prediction, axis=1).numpy()[0]
        predictions.append(predicted_class)
    
    return predictions

def analyze_karyotype(predictions):
    """
    Analyze the karyotype based on the predictions for individual chromosomes.
    """
    # Count occurrences of each chromosome class
    chromosome_counts = {i: predictions.count(i) for i in range(24)}  # 22 autosomes + X + Y
    
    # Check for abnormalities
    abnormalities = []
    for chromosome, count in chromosome_counts.items():
        if chromosome < 22:  # Autosomes
            if count != 2:
                abnormalities.append(f"Chromosome {chromosome + 1}: Expected 2, found {count}")
        elif chromosome == 22:  # X chromosome
            if count not in (1, 2):
                abnormalities.append(f"X Chromosome: Expected 1 or 2, found {count}")
        elif chromosome == 23:  # Y chromosome
            if count not in (0, 1):
                abnormalities.append(f"Y Chromosome: Expected 0 or 1, found {count}")
    
    # Determine sex based on sex chromosomes
    sex = "Male" if chromosome_counts[23] == 1 else "Female"
    
    # Generate analysis result
    if abnormalities:
        result = f"Abnormal karyotype detected. Sex: {sex}. Abnormalities:\n" + "\n".join(abnormalities)
    else:
        result = f"Normal karyotype. Sex: {sex}."
    
    return result

