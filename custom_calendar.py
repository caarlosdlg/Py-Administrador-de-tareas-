from PySide6.QtWidgets import QCalendarWidget
from PySide6.QtGui import QPalette, QTextCharFormat
from PySide6.QtCore import Qt, QDate

class CustomCalendar(QCalendarWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setup_ui()

    def setup_ui(self):
        # Formato general
        self.setVerticalHeaderFormat(QCalendarWidget.NoVerticalHeader)
        self.setHorizontalHeaderFormat(QCalendarWidget.SingleLetterDayNames)
        self.setNavigationBarVisible(True)
        self.setGridVisible(False)

        # Formato para días
        weekday_format = QTextCharFormat()
        weekday_format.setForeground(Qt.black)
        
        weekend_format = QTextCharFormat()
        weekend_format.setForeground(Qt.red)

        # Usar Qt.DayOfWeek enum en lugar de enteros
        day_mapping = {
            Qt.Saturday: weekend_format,
            Qt.Sunday: weekend_format,
            Qt.Monday: weekday_format,
            Qt.Tuesday: weekday_format,
            Qt.Wednesday: weekday_format,
            Qt.Thursday: weekday_format,
            Qt.Friday: weekday_format
        }

        for day, format in day_mapping.items():
            self.setWeekdayTextFormat(day, format)

        # Estilo
        self.setStyleSheet("""
            QCalendarWidget {
                background-color: white;
                border: 1px solid #cccccc;
                border-radius: 4px;
            }
            QCalendarWidget QToolButton {
                color: #333333;
                padding: 6px;
                background-color: transparent;
                border-radius: 4px;
            }
            QCalendarWidget QToolButton:hover {
                background-color: #e6e6e6;
            }
            QCalendarWidget QSpinBox {
                border: 1px solid #cccccc;
                border-radius: 4px;
                padding: 3px;
            }
            QCalendarWidget QMenu {
                border: 1px solid #cccccc;
                border-radius: 4px;
                background-color: white;
            }
            QCalendarWidget QWidget#qt_calendar_navigationbar {
                background-color: #f8f9fa;
                border-bottom: 1px solid #dee2e6;
                padding: 4px;
            }
            QCalendarWidget QWidget#qt_calendar_prevmonth {
                qproperty-icon: url(left.png);
                padding: 4px;
            }
            QCalendarWidget QWidget#qt_calendar_nextmonth {
                qproperty-icon: url(right.png);
                padding: 4px;
            }
        """)
