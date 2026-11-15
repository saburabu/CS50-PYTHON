import sys

from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QPushButton, QTableWidget, QTableWidgetItem, QMessageBox,
    QDialog, QFormLayout, QLineEdit, QDoubleSpinBox, QComboBox,
    QDialogButtonBox, QLabel, QFrame, QHeaderView
)

import main as backend


class ProductDialog(QDialog):
    def __init__(self, parent=None, title="Product", product=None):
        super().__init__(parent)
        self.setWindowTitle(title)
        self.setMinimumWidth(390)

        layout = QFormLayout(self)
        layout.setContentsMargins(22, 22, 22, 22)
        layout.setSpacing(13)

        self.name_input = QLineEdit()
        self.name_input.setPlaceholderText("e.g. Wireless Keyboard")

        self.price_input = QDoubleSpinBox()
        self.price_input.setRange(0, 1_000_000_000)
        self.price_input.setDecimals(2)
        self.price_input.setPrefix("$ ")

        self.category_input = QLineEdit()
        self.category_input.setPlaceholderText("e.g. Electronics")

        if product:
            self.name_input.setText(str(product.get("name", "")))
            self.price_input.setValue(float(product.get("price", 0)))
            self.category_input.setText(str(product.get("category", "")))

        layout.addRow("Name", self.name_input)
        layout.addRow("Price", self.price_input)
        layout.addRow("Category", self.category_input)

        buttons = QDialogButtonBox(
            QDialogButtonBox.StandardButton.Ok |
            QDialogButtonBox.StandardButton.Cancel
        )
        buttons.button(QDialogButtonBox.StandardButton.Ok).setObjectName(
            "dialogPrimary"
        )
        buttons.accepted.connect(self.accept)
        buttons.rejected.connect(self.reject)
        layout.addRow(buttons)

    def get_data(self):
        return (
            self.name_input.text().strip(),
            self.price_input.value(),
            self.category_input.text().strip()
        )


class UpdateDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Update Product")
        self.setMinimumWidth(390)

        layout = QFormLayout(self)
        layout.setContentsMargins(22, 22, 22, 22)
        layout.setSpacing(13)

        self.name_input = QLineEdit()
        self.field = QComboBox()
        self.field.addItems(["Price", "Category"])
        self.value_input = QLineEdit()

        layout.addRow("Product", self.name_input)
        layout.addRow("Field", self.field)
        layout.addRow("New value", self.value_input)

        buttons = QDialogButtonBox(
            QDialogButtonBox.StandardButton.Ok |
            QDialogButtonBox.StandardButton.Cancel
        )
        buttons.button(QDialogButtonBox.StandardButton.Ok).setObjectName(
            "dialogPrimary"
        )
        buttons.accepted.connect(self.accept)
        buttons.rejected.connect(self.reject)
        layout.addRow(buttons)

    def get_data(self):
        field = "price" if self.field.currentText() == "Price" else "category"
        return self.name_input.text().strip(), field, self.value_input.text().strip()


class ApiDialog(QDialog):
    def __init__(self, parent, products):
        super().__init__(parent)
        self.setWindowTitle("API Explorer • DummyJSON")
        self.resize(760, 520)

        layout = QVBoxLayout(self)
        layout.setContentsMargins(22, 22, 22, 22)

        title = QLabel("Products from DummyJSON API")
        title.setStyleSheet("font-size: 19px; font-weight: 800; color: white;")
        layout.addWidget(title)

        table = QTableWidget()
        table.setColumnCount(3)
        table.setHorizontalHeaderLabels(["TITLE", "PRICE", "CATEGORY"])
        table.verticalHeader().setVisible(False)
        table.setAlternatingRowColors(True)
        table.horizontalHeader().setSectionResizeMode(
            0, QHeaderView.ResizeMode.Stretch
        )
        table.horizontalHeader().setSectionResizeMode(
            1, QHeaderView.ResizeMode.ResizeToContents
        )
        table.horizontalHeader().setSectionResizeMode(
            2, QHeaderView.ResizeMode.ResizeToContents
        )
        table.setRowCount(len(products))

        for row, product in enumerate(products):
            table.setItem(row, 0, QTableWidgetItem(str(product.get("title", ""))))
            table.setItem(
                row, 1,
                QTableWidgetItem(f"${float(product.get('price', 0)):,.2f}")
            )
            table.setItem(
                row, 2,
                QTableWidgetItem(str(product.get("category", "")))
            )

        layout.addWidget(table)

        close = QPushButton("Close")
        close.setObjectName("primaryButton")
        close.clicked.connect(self.accept)
        layout.addWidget(close)


class ProductManager(QMainWindow):
    def __init__(self):
        super().__init__()

        self.products = backend.initialize_products()

        self.setWindowTitle("NOVA • Product Manager")
        self.resize(1180, 720)
        self.setMinimumSize(1000, 620)

        self.apply_theme()
        self.build_ui()
        self.refresh_table()

    def apply_theme(self):
        self.setStyleSheet("""
            * {
                font-family: "Segoe UI", Arial, sans-serif;
            }
            QMainWindow, QWidget {
                background: #0b0f17;
                color: #e8edf5;
            }
            #sidebar {
                background: #101622;
                border-right: 1px solid #202a3a;
            }
            #brand {
                color: #ffffff;
                font-size: 25px;
                font-weight: 800;
                letter-spacing: 1px;
            }
            #subtitle {
                color: #7f8ba3;
                font-size: 12px;
            }
            #navLabel {
                color: #647086;
                font-size: 11px;
                font-weight: 700;
                padding-top: 18px;
                padding-bottom: 6px;
            }
            QPushButton {
                background: transparent;
                color: #aab4c5;
                border: 1px solid transparent;
                border-radius: 9px;
                padding: 11px 14px;
                text-align: left;
                font-size: 13px;
                font-weight: 600;
            }
            QPushButton:hover {
                background: #171f2d;
                color: #ffffff;
                border: 1px solid #26334a;
            }
            #navActive {
                background: #19182d;
                color: #9b87ff;
                border: 1px solid #322d55;
            }
            #primaryButton, #dialogPrimary {
                background: #7c5cff;
                color: white;
                border: none;
                border-radius: 9px;
                padding: 12px 17px;
                font-weight: 700;
            }
            #primaryButton:hover, #dialogPrimary:hover {
                background: #8d70ff;
            }
            #dangerButton {
                background: #21161b;
                color: #ff7f96;
                border: 1px solid #49242e;
                border-radius: 9px;
                padding: 12px 17px;
                font-weight: 700;
            }
            #pageTitle {
                font-size: 27px;
                font-weight: 800;
                color: #ffffff;
            }
            #pageDescription {
                color: #7f8ba3;
                font-size: 13px;
            }
            #card, #tableCard {
                background: #111824;
                border: 1px solid #202a3a;
                border-radius: 14px;
            }
            #cardTitle {
                color: #7f8ba3;
                font-size: 12px;
                font-weight: 600;
            }
            #cardValue {
                color: #ffffff;
                font-size: 23px;
                font-weight: 800;
            }
            QTableWidget {
                background: #111824;
                alternate-background-color: #0e1520;
                border: none;
                gridline-color: #1b2535;
                color: #dce3ef;
                selection-background-color: #292347;
                selection-color: #ffffff;
                outline: none;
                font-size: 13px;
            }
            QTableWidget::item {
                padding: 12px;
                border-bottom: 1px solid #1b2535;
            }
            QHeaderView::section {
                background: #0e1520;
                color: #707c91;
                border: none;
                border-bottom: 1px solid #202a3a;
                padding: 13px 12px;
                font-size: 11px;
                font-weight: 800;
            }
            QLineEdit, QDoubleSpinBox, QComboBox {
                background: #0d141f;
                color: #eef2f8;
                border: 1px solid #29354a;
                border-radius: 8px;
                padding: 10px;
            }
            QLineEdit:focus, QDoubleSpinBox:focus, QComboBox:focus {
                border: 1px solid #7c5cff;
            }
            QDialog {
                background: #101622;
            }
            QDialogButtonBox QPushButton {
                text-align: center;
                padding: 9px 18px;
            }
            QStatusBar {
                background: #0b0f17;
                color: #647086;
                border-top: 1px solid #202a3a;
            }
        """)

    def build_ui(self):
        central = QWidget()
        self.setCentralWidget(central)

        root = QHBoxLayout(central)
        root.setContentsMargins(0, 0, 0, 0)
        root.setSpacing(0)

        sidebar = QFrame()
        sidebar.setObjectName("sidebar")
        sidebar.setFixedWidth(225)

        side = QVBoxLayout(sidebar)
        side.setContentsMargins(18, 24, 18, 18)

        brand = QLabel("NOVA")
        brand.setObjectName("brand")
        side.addWidget(brand)

        subtitle = QLabel("PRODUCT OPERATIONS")
        subtitle.setObjectName("subtitle")
        side.addWidget(subtitle)

        side.addSpacing(25)

        label = QLabel("WORKSPACE")
        label.setObjectName("navLabel")
        side.addWidget(label)

        dashboard = QPushButton("  ◈   Dashboard")
        dashboard.setObjectName("navActive")
        side.addWidget(dashboard)

        products_btn = QPushButton("  ▦   Products")
        side.addWidget(products_btn)

        api_btn = QPushButton("  ◉   API Explorer")
        side.addWidget(api_btn)

        label = QLabel("ACTIONS")
        label.setObjectName("navLabel")
        side.addWidget(label)

        add_side = QPushButton("  ＋   Add Product")
        side.addWidget(add_side)

        update_side = QPushButton("  ✎   Update Product")
        side.addWidget(update_side)

        side.addStretch()

        exit_btn = QPushButton("  ↪   Exit")
        side.addWidget(exit_btn)

        root.addWidget(sidebar)

        content = QWidget()
        content_layout = QVBoxLayout(content)
        content_layout.setContentsMargins(30, 25, 30, 25)
        content_layout.setSpacing(18)

        header = QHBoxLayout()

        heading = QVBoxLayout()
        title = QLabel("Product Dashboard")
        title.setObjectName("pageTitle")
        heading.addWidget(title)

        description = QLabel(
            "Manage your inventory, API data and product records."
        )
        description.setObjectName("pageDescription")
        heading.addWidget(description)

        header.addLayout(heading)
        header.addStretch()

        refresh = QPushButton("↻  Refresh")
        refresh.setObjectName("primaryButton")
        header.addWidget(refresh)

        content_layout.addLayout(header)

        stats = QHBoxLayout()

        self.total_value = QLabel("0")
        self.categories_value = QLabel("0")
        self.avg_value = QLabel("$0.00")

        for value in (
            self.total_value,
            self.categories_value,
            self.avg_value
        ):
            value.setObjectName("cardValue")

        stats.addWidget(self.make_stat_card(
            "TOTAL PRODUCTS", self.total_value, "Inventory"
        ))
        stats.addWidget(self.make_stat_card(
            "CATEGORIES", self.categories_value, "Product groups"
        ))
        stats.addWidget(self.make_stat_card(
            "AVERAGE PRICE", self.avg_value, "Across inventory"
        ))

        content_layout.addLayout(stats)

        table_card = QFrame()
        table_card.setObjectName("tableCard")

        table_layout = QVBoxLayout(table_card)
        table_layout.setContentsMargins(18, 15, 18, 12)

        table_header = QHBoxLayout()

        table_title = QLabel("Your Products")
        table_title.setStyleSheet(
            "font-size: 16px; font-weight: 800; color: #ffffff;"
        )
        table_header.addWidget(table_title)
        table_header.addStretch()

        self.count_label = QLabel("0 products")
        self.count_label.setStyleSheet("color: #68758b; font-size: 12px;")
        table_header.addWidget(self.count_label)

        table_layout.addLayout(table_header)

        self.table = QTableWidget()
        self.table.setColumnCount(3)
        self.table.setHorizontalHeaderLabels(
            ["PRODUCT", "PRICE", "CATEGORY"]
        )
        self.table.setSelectionBehavior(
            QTableWidget.SelectionBehavior.SelectRows
        )
        self.table.setSelectionMode(
            QTableWidget.SelectionMode.SingleSelection
        )
        self.table.setEditTriggers(
            QTableWidget.EditTrigger.NoEditTriggers
        )
        self.table.setAlternatingRowColors(True)
        self.table.verticalHeader().setVisible(False)
        self.table.horizontalHeader().setSectionResizeMode(
            0, QHeaderView.ResizeMode.Stretch
        )
        self.table.horizontalHeader().setSectionResizeMode(
            1, QHeaderView.ResizeMode.ResizeToContents
        )
        self.table.horizontalHeader().setSectionResizeMode(
            2, QHeaderView.ResizeMode.ResizeToContents
        )

        table_layout.addWidget(self.table)

        actions = QHBoxLayout()

        add = QPushButton("＋  Add Product")
        add.setObjectName("primaryButton")

        replace = QPushButton("↻  Replace")
        update = QPushButton("✎  Update")

        delete = QPushButton("⌫  Delete")
        delete.setObjectName("dangerButton")

        actions.addWidget(add)
        actions.addWidget(replace)
        actions.addWidget(update)
        actions.addWidget(delete)
        actions.addStretch()

        table_layout.addLayout(actions)
        content_layout.addWidget(table_card, 1)

        root.addWidget(content, 1)

        refresh.clicked.connect(self.refresh_table)
        dashboard.clicked.connect(self.refresh_table)
        products_btn.clicked.connect(self.refresh_table)
        api_btn.clicked.connect(self.show_api_products)

        add.clicked.connect(self.add_product)
        add_side.clicked.connect(self.add_product)
        replace.clicked.connect(self.replace_product)
        update.clicked.connect(self.update_product)
        update_side.clicked.connect(self.update_product)
        delete.clicked.connect(self.delete_product)
        exit_btn.clicked.connect(self.close)

        self.statusBar().showMessage("Ready")

    def make_stat_card(self, title, value, description):
        card = QFrame()
        card.setObjectName("card")

        layout = QVBoxLayout(card)
        layout.setContentsMargins(17, 14, 17, 14)

        title_label = QLabel(title)
        title_label.setObjectName("cardTitle")
        layout.addWidget(title_label)
        layout.addWidget(value)

        desc = QLabel(description)
        desc.setStyleSheet("color: #59667b; font-size: 11px;")
        layout.addWidget(desc)

        return card

    def refresh_table(self):
        products = backend.get_all_products(self.products)
        self.table.setRowCount(0)

        categories = set()
        prices = []

        for product in products:
            row = self.table.rowCount()
            self.table.insertRow(row)

            name = str(product.get("name", ""))
            category = str(product.get("category", ""))

            try:
                price = float(product.get("price", 0))
                price_text = f"${price:,.2f}"
                prices.append(price)
            except (ValueError, TypeError):
                price_text = str(product.get("price", ""))

            categories.add(category)

            self.table.setItem(row, 0, QTableWidgetItem(name))
            self.table.setItem(row, 1, QTableWidgetItem(price_text))
            self.table.setItem(row, 2, QTableWidgetItem(category))

        total = len(products)
        average = sum(prices) / len(prices) if prices else 0

        self.total_value.setText(str(total))
        self.categories_value.setText(str(len(categories)))
        self.avg_value.setText(f"${average:,.2f}")
        self.count_label.setText(
            f"{total} product{'s' if total != 1 else ''}"
        )

    def get_selected_product_name(self):
        row = self.table.currentRow()

        if row < 0:
            QMessageBox.warning(
                self,
                "No Selection",
                "Select a product first."
            )
            return None

        return self.table.item(row, 0).text()

    def show_api_products(self):
        result = backend.get_products_from_api()

        if not result["success"]:
            QMessageBox.critical(self, "API Error", result["message"])
            return

        ApiDialog(self, result["products"]).exec()

    def add_product(self):
        dialog = ProductDialog(self, "Add Product")

        if dialog.exec() != QDialog.DialogCode.Accepted:
            return

        name, price, category = dialog.get_data()

        success, message, _ = backend.add_product(
            self.products, name, price, category
        )

        if success:
            self.refresh_table()
            QMessageBox.information(self, "Product Added", message)
        else:
            QMessageBox.warning(self, "Could Not Add Product", message)

    def replace_product(self):
        selected = self.get_selected_product_name()

        if not selected:
            return

        product = next(
            (p for p in self.products if p.get("name") == selected),
            None
        )

        if not product:
            QMessageBox.warning(self, "Not Found", "Product no longer exists.")
            return

        dialog = ProductDialog(self, "Replace Product", product)

        if dialog.exec() != QDialog.DialogCode.Accepted:
            return

        name, price, category = dialog.get_data()

        success, message, _ = backend.replace_product(
            self.products,
            selected,
            name,
            price,
            category
        )

        if success:
            self.refresh_table()
            QMessageBox.information(self, "Product Replaced", message)
        else:
            QMessageBox.warning(self, "Could Not Replace Product", message)

    def update_product(self):
        selected = self.get_selected_product_name()

        if not selected:
            return

        dialog = UpdateDialog(self)
        dialog.name_input.setText(selected)

        if dialog.exec() != QDialog.DialogCode.Accepted:
            return

        name, field, value = dialog.get_data()

        success, message, _ = backend.update_product(
            self.products, name, field, value
        )

        if success:
            self.refresh_table()
            QMessageBox.information(self, "Product Updated", message)
        else:
            QMessageBox.warning(self, "Could Not Update Product", message)

    def delete_product(self):
        selected = self.get_selected_product_name()

        if not selected:
            return

        answer = QMessageBox.question(
            self,
            "Confirm Delete",
            f"Delete '{selected}'?",
            QMessageBox.StandardButton.Yes |
            QMessageBox.StandardButton.No
        )

        if answer != QMessageBox.StandardButton.Yes:
            return

        success, message, _ = backend.delete_product(
            self.products, selected
        )

        if success:
            self.refresh_table()
            QMessageBox.information(self, "Product Deleted", message)
        else:
            QMessageBox.warning(self, "Could Not Delete Product", message)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ProductManager()
    window.show()
    sys.exit(app.exec())
