from setuptools import setup

setup(
    name="ModbusGuiApp",
    author="Ivan Cindric",
    author_email="ivan.cindric95@example.com",
    description="ModbusGuiApplication.",
    version="0.7",
    packages=['modbus_gui_app',
              'modbus_gui_app.communication',
              'modbus_gui_app.database',
              'modbus_gui_app.database',
              'modbus_gui_app.gui',
              'modbus_gui_app.state',
              'test',
              'test.test_communication',
              'test.test_database',
              'test.test_state'
              ],
    python_requires='>=3.6',
)
