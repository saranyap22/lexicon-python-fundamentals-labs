# use case for method override and still use base class method

class Report:
    def get_information(self):
        return "Final report Summary: \n"


class SalesReport(Report):
    def get_information(self):
        report = super().get_information()
        return report + "Sales report summary"


sales_report = SalesReport()
print(sales_report.get_information())
# Here both base class and override method used. By using super()

# ---------------------------------------------------------------
