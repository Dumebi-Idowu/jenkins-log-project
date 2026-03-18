def analyze_logs(file_path, output_path="report.txt"):
    error = 0
    warning = 0
    info = 0
    error_lines = []
    warning_lines = []

    with open(file_path, "r") as file:
        for line in file:
            if "ERROR" in line:
                error += 1
                error_lines.append(line.strip())
            elif "WARNING" in line:
                warning += 1
                warning_lines.append(line.strip())
            elif "INFO" in line:
                info += 1

    # print to console
    print("Log Summary")
    print("-----------")
    print(f"Errors:   {error}")
    print(f"Warnings: {warning}")
    print(f"Info:     {info}")

    # 👇 also save to a file
    with open(output_path, "w") as report:
        report.write("LOG ANALYSIS REPORT\n")
        report.write("===================\n\n")
        report.write(f"Total Errors:   {error}\n")
        report.write(f"Total Warnings: {warning}\n")
        report.write(f"Total Info:     {info}\n\n")

        if error_lines:
            report.write("ERROR LINES\n")
            report.write("-----------\n")
            for line in error_lines:
                report.write(f"{line}\n")

        if warning_lines:
            report.write("\nWARNING LINES\n")
            report.write("-------------\n")
            for line in warning_lines:
                report.write(f"{line}\n")

    print(f"\n✅ Report saved to {output_path}")

if __name__ == "__main__":
    analyze_logs("app.log", "report.txt")