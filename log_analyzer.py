def analyze_logs(file_path):
    error = 0
    warning = 0
    info = 0

    with open(file_path, "r") as file:
        for line in file:
            if "ERROR" in line:
                error += 1
            elif "WARNING" in line:
                warning += 1
            elif "INFO" in line:
                info += 1

    print("Log Summary")
    print("-----------")
    print(f"Errors: {error}")
    print(f"Warnings: {warning}")
    print(f"Info: {info}")


if __name__ == "__main__":
    analyze_logs("app.log")