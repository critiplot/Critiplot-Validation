import critiplot

from critiplot import plot_nos, plot_jbi_case_report, plot_jbi_case_series, plot_grade, plot_robis, plot_mmat

# NOS
plot_nos("tests/sample_nos.csv", "output_nos.png", theme="blue")

# ROBIS
plot_robis("tests/sample_robis.csv", "output_robis.png", theme="smiley")

# JBI Case Report
plot_jbi_case_report("tests/sample_jbi_case_report.csv", "output_case_report.png", theme="gray")

# JBI Case Series
plot_jbi_case_series("tests/sample_jbi_case_series.csv", "output_case_series.png", theme="smiley_blue")

# GRADE
plot_grade("tests/sample_grade.csv", "output_grade.png", theme="green")

# MMAT
plot_mmat("tests/sample_mmat.csv", "output_mmat.png", theme="default")