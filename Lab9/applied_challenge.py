# Applied Challenge: Exporter System

class Exporter:

    def export(self, data):
        pass


class TextExporter(Exporter):

    def export(self, data):
        return f"TEXT-LOG: {data.timestamp}  : {data.level} : {data.message}"


class SummaryExporter(Exporter):

    def export(self, data):
        return f"SUMMARY: {data.level} - {data.message}"


class ConsoleExporter(Exporter):

    def export(self, data):
        return (
            f"CONSOLE: \nTime: {data.timestamp}\n"
            f"Level: {data.level}\n"
            f"message: {data.message}\n"
        )


class Data:
    def __init__(self, message, timestamp, level):
        self.message = message
        self.timestamp = timestamp
        self.level = level

    def __str__(self):
        return (
            f"Message: {self.message}"
            f"Timestamp: {self.timestamp}"
            f"level: {self.level}"
        )


class LogSystem:
    def __init__(self, exporters=None):
        self.exporters = [] if exporters is None else exporters

    def add_exporter(self, exporter):
        self.exporters.append(exporter)

    def export(self, data):
        for exporter in self.exporters:
            print(exporter.export(data))


exporters = [
    TextExporter(), ConsoleExporter(), SummaryExporter()
]

Log_system = LogSystem(exporters)
data = Data("DataBase connection timed out", "24-09-2026", "Error")
Log_system.export(data)
