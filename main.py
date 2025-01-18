from PySide6.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, 
                              QHBoxLayout, QLabel, QLineEdit, QComboBox, 
                              QPushButton, QTableWidget, QTableWidgetItem, 
                              QMessageBox, QHeaderView, QSplitter, QFrame)
from PySide6.QtCore import Qt, QDate, QTimer
from PySide6.QtGui import QColor, QPalette
from database import DatabaseManager
from custom_calendar import CustomCalendar
from datetime import datetime
import sys
import darkdetect

class TaskManager(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Administrador de Tareas")
        self.setMinimumSize(1200, 700)
        
        # Detectar tema del sistema
        self.is_dark_mode = darkdetect.isDark()
        self.setup_theme()
        
        # Inicializar base de datos
        self.db = DatabaseManager()
        
        # Widget y layout principal
        main_widget = QWidget()
        self.setCentralWidget(main_widget)
        layout = QHBoxLayout(main_widget)
        
        # Crear formulario y tabla
        self.create_form_layout(layout)
        self.create_table_layout(layout)
        
        # Configurar notificaciones
        self.setup_notifications()
        
        # Cargar tareas
        self.load_tasks()

    def setup_theme(self):
        # Configurar tema claro/oscuro
        if self.is_dark_mode:
            self.setStyleSheet("""
                QMainWindow, QWidget {
                    background-color: #2d2d2d;
                    color: #ffffff;
                }
                QLineEdit, QComboBox {
                    background-color: #3d3d3d;
                    border: 1px solid #555555;
                    border-radius: 4px;
                    padding: 5px;
                    color: white;
                }
                QTableWidget {
                    background-color: #2d2d2d;
                    alternate-background-color: #353535;
                    gridline-color: #555555;
                }
                QHeaderView::section {
                    background-color: #404040;
                    color: white;
                    padding: 5px;
                }
                QLabel {
                    color: #ffffff;
                }
            """)
        else:
            self.setStyleSheet("""
                QMainWindow, QWidget {
                    background-color: #f5f5f5;
                }
                QLineEdit, QComboBox {
                    border: 1px solid #cccccc;
                    border-radius: 4px;
                    padding: 5px;
                }
                QTableWidget {
                    alternate-background-color: #fafafa;
                    gridline-color: #dddddd;
                }
                QHeaderView::section {
                    background-color: #f0f0f0;
                    padding: 5px;
                }
            """)

    def create_form_layout(self, parent_layout):
        # Crear un QSplitter para hacer la interfaz responsiva
        splitter = QSplitter(Qt.Horizontal)
        
        # Panel izquierdo (formulario)
        form_widget = QWidget()
        form_layout = QVBoxLayout(form_widget)
        form_layout.setContentsMargins(20, 20, 20, 20)
        form_layout.setSpacing(10)
        
        # Título con mejor estilo
        title_label = QLabel("Nueva Tarea")
        title_label.setStyleSheet("""
            font-size: 24px;
            font-weight: bold;
            margin-bottom: 20px;
            color: #2196F3;
        """)
        
        # Mejorar campos de entrada
        self.title_input = QLineEdit()
        self.title_input.setPlaceholderText("Título de la tarea")
        self.title_input.setMinimumHeight(30)
        
        self.desc_input = QLineEdit()
        self.desc_input.setPlaceholderText("Descripción de la tarea")
        self.desc_input.setMinimumHeight(30)
        
        # Combobox mejorado
        self.priority_combo = QComboBox()
        self.priority_combo.addItems(["Alta", "Media", "Baja"])
        self.priority_combo.setMinimumHeight(30)
        
        # Calendario personalizado
        self.calendar = CustomCalendar()
        
        # Botones con mejor estilo
        buttons_layout = QHBoxLayout()
        self.add_btn = QPushButton("Agregar Tarea")
        self.update_btn = QPushButton("Actualizar")
        self.delete_btn = QPushButton("Eliminar")
        
        button_style = """
            QPushButton {
                background-color: #2196F3;
                color: white;
                border: none;
                padding: 8px 20px;
                border-radius: 4px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #1976D2;
            }
            QPushButton:pressed {
                background-color: #0D47A1;
            }
        """
        
        for btn in [self.add_btn, self.update_btn, self.delete_btn]:
            btn.setStyleSheet(button_style)
            btn.setMinimumHeight(35)
        
        # Conectar señales
        self.add_btn.clicked.connect(self.add_task)
        self.update_btn.clicked.connect(self.update_task)
        self.delete_btn.clicked.connect(self.delete_task)
        
        # Agregar widgets al layout
        form_layout.addWidget(title_label)
        form_layout.addWidget(QLabel("Título:"))
        form_layout.addWidget(self.title_input)
        form_layout.addWidget(QLabel("Descripción:"))
        form_layout.addWidget(self.desc_input)
        form_layout.addWidget(QLabel("Prioridad:"))
        form_layout.addWidget(self.priority_combo)
        form_layout.addWidget(QLabel("Fecha:"))
        form_layout.addWidget(self.calendar)
        
        buttons_layout.addWidget(self.add_btn)
        buttons_layout.addWidget(self.update_btn)
        buttons_layout.addWidget(self.delete_btn)
        form_layout.addLayout(buttons_layout)
        
        form_layout.addStretch()
        splitter.addWidget(form_widget)
        parent_layout.addWidget(splitter)

    def create_table_layout(self, parent_layout):
        # Tabla con mejor estilo
        self.table = QTableWidget()
        self.table.setColumnCount(6)
        self.table.setHorizontalHeaderLabels(['ID', 'Título', 'Descripción', 'Fecha', 'Prioridad', 'Estado'])
        self.table.setAlternatingRowColors(True)
        
        # Configurar cabecera
        header = self.table.horizontalHeader()
        header.setStretchLastSection(True)
        header.setSectionResizeMode(QHeaderView.Interactive)
        header.setMinimumSectionSize(100)
        
        # Establecer anchos de columna
        column_widths = [50, 200, 300, 120, 100, 100]
        for i, width in enumerate(column_widths):
            self.table.setColumnWidth(i, width)
        
        # Conectar selección
        self.table.itemSelectionChanged.connect(self.on_selection_changed)
        
        parent_layout.addWidget(self.table)

    def load_tasks(self):
        self.table.setRowCount(0)
        tasks = self.db.get_all_tasks()
        
        for row, task in enumerate(tasks):
            self.table.insertRow(row)
            for col, value in enumerate(task):
                item = QTableWidgetItem(str(value))
                self.table.setItem(row, col, item)
            
            # Colorear según prioridad
            priority = task[4].lower()
            color = {
                'alta': QColor('#ffcdd2'),
                'media': QColor('#fff9c4'),
                'baja': QColor('#c8e6c9')
            }.get(priority, QColor('white'))
            
            for col in range(6):
                self.table.item(row, col).setBackground(color)

    def add_task(self):
        title = self.title_input.text()
        description = self.desc_input.text()
        priority = self.priority_combo.currentText()
        date = self.calendar.selectedDate().toString("yyyy-MM-dd")
        
        if title and description:
            self.db.add_task(title, description, date, priority)
            self.load_tasks()
            self.clear_form()
        else:
            QMessageBox.warning(self, "Error", "Por favor complete todos los campos")

    def update_task(self):
        selected_items = self.table.selectedItems()
        if not selected_items:
            QMessageBox.warning(self, "Advertencia", "Por favor seleccione una tarea")
            return
            
        row = selected_items[0].row()
        task_id = self.table.item(row, 0).text()
        title = self.title_input.text()
        description = self.desc_input.text()
        priority = self.priority_combo.currentText()
        date = self.calendar.selectedDate().toString("yyyy-MM-dd")
        status = "completada"
        
        self.db.update_task(task_id, title, description, date, priority, status)
        self.load_tasks()
        self.clear_form()

    def delete_task(self):
        selected_items = self.table.selectedItems()
        if not selected_items:
            QMessageBox.warning(self, "Advertencia", "Por favor seleccione una tarea")
            return
            
        row = selected_items[0].row()
        task_id = self.table.item(row, 0).text()
        
        self.db.delete_task(task_id)
        self.load_tasks()
        self.clear_form()

    def clear_form(self):
        self.title_input.clear()
        self.desc_input.clear()
        self.priority_combo.setCurrentIndex(1)  # Media
        self.calendar.setSelectedDate(QDate.currentDate())

    def on_selection_changed(self):
        selected_items = self.table.selectedItems()
        if selected_items:
            row = selected_items[0].row()
            self.title_input.setText(self.table.item(row, 1).text())
            self.desc_input.setText(self.table.item(row, 2).text())
            self.priority_combo.setCurrentText(self.table.item(row, 4).text())
            date = QDate.fromString(self.table.item(row, 3).text(), "yyyy-MM-dd")
            self.calendar.setSelectedDate(date)

    def setup_notifications(self):
        self.timer = QTimer()
        self.timer.timeout.connect(self.check_due_tasks)
        self.timer.start(3600000)  # 1 hora en milisegundos

    def check_due_tasks(self):
        tasks = self.db.get_all_tasks()
        current_date = datetime.now().strftime('%Y-%m-%d')
        
        for task in tasks:
            if task[3] == current_date and task[5] != 'completada':
                QMessageBox.information(
                    self,
                    "Recordatorio",
                    f"La tarea '{task[1]}' vence hoy!"
                )

if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    # Estilo global
    app.setStyle('Fusion')
    
    window = TaskManager()
    window.show()
    sys.exit(app.exec())