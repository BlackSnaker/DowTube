#!/usr/bin/python
import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget, QFileDialog
from PyQt6.QtCore import Qt
from pytube import YouTube

class YouTubeDownloader(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("DowTube")
        self.setGeometry(100, 100, 300, 200)
        self.setFixedSize(300, 200)
        self.setWindowOpacity(0.9)
        self.setStyleSheet(
            """
            QWidget {
                background-color: rgba(33, 33, 33, 180);
                border-radius: 20px;  /* Увеличиваем радиус скругления углов */
            }
            QLabel {
                color: #FFFFFF;
            }
            QLineEdit {
                background-color: rgba(255, 255, 255, 180);
                color: #000000;
                border-radius: 10px;
                border: 2px solid #2E2E2E;
            }
            QPushButton {
                background-color: #FF0000;
                color: #FFFFFF;
                border-radius: 10px;
                padding: 5px 10px;
                border: 2px solid #2E2E2E;
                font-weight: bold;
                text-align: center;
                transition: background-color 0.3s ease;
            }
            QPushButton:hover {
                background-color: #CC0000;
            }
            """
        )

        self.url_label = QLabel("DowTube")
        self.url_input = QLineEdit()
        self.url_input.setPlaceholderText("Введите ссылку YouTube URL")
        self.url_input.setStyleSheet("QLineEdit { background-color: rgba(255, 255, 255, 180); color: #000000; border-radius: 10px; border: 2px solid #2E2E2E; }")

        self.download_video_button = QPushButton("Загрузить видео")
        self.download_video_button.clicked.connect(self.choose_save_location_video)

        self.download_audio_button = QPushButton("Загрузить аудио")
        self.download_audio_button.clicked.connect(self.choose_save_location_audio)

        self.status_label = QLabel("")

        layout = QVBoxLayout()
        layout.addWidget(self.url_label)
        layout.addWidget(self.url_input)
        layout.addWidget(self.status_label)

        button_layout = QVBoxLayout()
        button_layout.addWidget(self.download_video_button)
        button_layout.addWidget(self.download_audio_button)

        layout.addLayout(button_layout)

        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

        self.save_location = ""

    def choose_save_location_video(self):
        self.save_location = QFileDialog.getExistingDirectory(self, "Куда сохранить видео")
        if self.save_location:
            self.download_video()

    def choose_save_location_audio(self):
        self.save_location = QFileDialog.getExistingDirectory(self, "Куда сохранить аудио")
        if self.save_location:
            self.download_audio()

    def download_video(self):
        url = self.url_input.text()
        if url:
            try:
                yt = YouTube(url)
                stream = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
                stream.download(output_path=self.save_location)
                self.status_label.setText("Видео загружено!")
            except Exception as e:
                self.status_label.setText(f"Ошибка: {str(e)}")
        else:
            self.status_label.setText("Введите ссылку YouTube URL.")

    def download_audio(self):
        url = self.url_input.text()
        if url:
            try:
                yt = YouTube(url)
                stream = yt.streams.filter(only_audio=True, file_extension='mp4').first()
                stream.download(output_path=self.save_location)
                self.status_label.setText("Аудио загружено!")
            except Exception as e:
                self.status_label.setText(f"Ошибка: {str(e)}")
        else:
            self.status_label.setText("Введите ссылку YouTube URL.")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = YouTubeDownloader()
    window.show()
    sys.exit(app.exec())
