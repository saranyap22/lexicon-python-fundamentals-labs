"""Module contains functions for Report Builder"""


def create_report(title, *sections, **metadata):
    """ Return a dictionary of report
    Each section is expected to be a small dictionary for consistency"""
    report = {"title": title}
    if sections:
        report["sections"] = sections
    if metadata:
        report["metadata"] = metadata

    return report


def summarize_report(report):
    """ Return multiline String format"""
    formatted_report = f"{report["title"]:^15}\n"

    for section in report["sections"]:
        for key, value in section.items():
            formatted_report += f"{key:<30}:  {value:<30}\n"

    for data, value in report["metadata"].items():
        formatted_report += f"{data:<30}:  {value:<30}\n"

    return formatted_report


def count_words(*sections):
    """Return count of words in sections"""
    words = []
    for section in sections:
        for key, value in section.items():
            words.append(key)
            words.extend(value.strip().split())
    return len(words)


student_performance_sections = [{
    "summary": "In total 100 students witten exam. 80 students Passed in all and 20 failed in one or more",
    "recommentation": "Conduct review meeting for the Failed student and take corrective measures"
}]

attendence_sections = [{
    "summary": "Average attendence for september is 80%"
}]
student1_report_metadata = {
    "author": "saranya", "department": "computer science",
    "version": "1.0", "is_confidential": False, "date": "18-09-2026"
}
student2_report_metadata = {
    "author": "Anna", "department": "IT",
    "version": "1.0"
}
attendence_report_metadata = {
    "author": "Roam", "department": "administration",
    "version": "2.0", "is_confidential": True, "date": "19-09-2026"
}

print(summarize_report(create_report("Student Performance Report",
                       *student_performance_sections, **student1_report_metadata)))
print(summarize_report(create_report("Attendence Report",
                       *student_performance_sections, **student2_report_metadata)))
print(summarize_report(create_report("Attendence Report",
                       *attendence_sections, **attendence_report_metadata)))
print(count_words(*student_performance_sections))
