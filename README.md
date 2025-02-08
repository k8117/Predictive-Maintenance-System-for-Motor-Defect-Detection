🚀 README for Predictive Maintenance System for Motor Defect Detection
This project implements a Predictive Maintenance System to classify motor defects using machine learning (Random Forest) and deep learning (CNNs). It analyzes vibration signals from motors, extracts meaningful features, and predicts whether a motor is normal or has specific defects (inner fault, roller fault, or outer fault).

📌 Project Overview
This project was carried out by a student from the University of Swabi, under the supervision of a doctoral student in mechanics and a teacher-researcher in mechanics at the University of Peshawar (UOP). The objective is to predict motor defects using audio signals, leveraging feature extraction and deep learning techniques.

📂 Dataset
The dataset contains 4 motor conditions:
Normal motor
Inner race fault
Roller fault
Outer race fault
Each signal originally had 120,000 samples, which were segmented into smaller windows (6,000 samples each) for better training.
The processed dataset is saved as Newdataset.mat.
🔬 Methodology
1️⃣ Data Preprocessing

Raw vibration signals are segmented to create more samples.
Features are extracted using MFCCs (Mel-Frequency Cepstral Coefficients).
Signals are converted into Spectrogram images for CNN training.
2️⃣ Model Development

Feature Extraction Model: Uses Random Forest trained on MFCCs.
Deep Learning Model: Uses a CNN trained on spectrogram images.
3️⃣ Model Evaluation

Models are tested on unseen data using accuracy, precision, recall, and F1-score.
Confusion Matrices are plotted for classification performance.
🏆 Results
Both models achieved 100% accuracy after dataset augmentation and feature extraction.

✅ Feature Extraction Model (Random Forest) Performance
markdown
Copy
Edit
              precision    recall  f1-score   support
           0       1.00      1.00      1.00         7
           1       1.00      1.00      1.00         6
           2       1.00      1.00      1.00         5
           3       1.00      1.00      1.00         6

    accuracy                           1.00        24
✅ CNN Model (Spectrogram-Based) Performance
markdown
Copy
Edit
              precision    recall  f1-score   support
           0       1.00      1.00      1.00         7
           1       1.00      1.00      1.00         6
           2       1.00      1.00      1.00         5
           3       1.00      1.00      1.00         6

    accuracy                           1.00        24
📌 Installation & Usage
1️⃣ Install Required Dependencies
bash
Copy
Edit
pip install numpy scipy librosa scikit-learn tensorflow matplotlib
2️⃣ Run Data Preprocessing & Model Training
bash
Copy
Edit
python train_models.py  # (Make sure to have dataset in the same directory)
3️⃣ Check Results
Results are automatically saved in Results.txt.

📁 Project Structure
bash
Copy
Edit
📂 Predictive_Maintenance
│── 📜 dataset.mat                # Original dataset
│── 📜 Newdataset.mat              # Augmented dataset (after segmentation)
│── 📜 train_models.py             # Code for training Random Forest & CNN
│── 📜 Results.txt                 # Saved model evaluation results
│── 📜 README.md                   # Project Documentation (this file)
📌 Future Work
🚀 Deploy as a Web App using Flask or Streamlit.
🚀 Integrate with IoT sensors for real-time motor health monitoring.
🚀 Use Transfer Learning to improve model robustness on unseen data.

👨‍💻 Author
Salal Ahmad - University of Swabi, Department of Computer Science.

📌 If this project helps you, give it a ⭐ on GitHub! 🚀

