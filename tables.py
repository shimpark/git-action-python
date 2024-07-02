import json
import pandas as pd
from datetime import datetime
from bs4 import BeautifulSoup


def load_json(file_path):
    """Load JSON data from a file."""
    with open(file_path, "r", encoding="utf-8") as file:
        return json.load(file)["data"]


def extract_time(datetime_str):
    """Extract and format time from a datetime string."""
    try:
        return datetime.strptime(datetime_str, "%Y-%m-%dT%H:%M:%S.%f").strftime("%H:%M")
    except ValueError:
        return datetime.strptime(datetime_str, "%Y-%m-%dT%H:%M:%S").strftime("%H:%M")


def clean_html(raw_html):
    """Clean HTML content and replace <br> with new lines."""
    soup = BeautifulSoup(raw_html, "html.parser")
    for br in soup.find_all("br"):
        br.replace_with("\n")
    return soup.get_text()


def format_date(date_str):
    """Format date string to the desired format."""
    try:
        return datetime.strptime(date_str, "%Y-%m-%dT%H:%M:%S.%f").strftime("%Y.%m.%d")
    except ValueError:
        return datetime.strptime(date_str, "%Y-%m-%dT%H:%M:%S").strftime("%Y.%m.%d")


def prepare_record(item):
    """Prepare a single record for the DataFrame."""
    shift_start_date = format_date(item["ShiftStartDate"])
    shift_start_time = extract_time(item["ShiftStartDate"])
    shift_end_time = extract_time(item["ShiftEndDate"])

    application_time = f"{clean_html(item['ReqContentText'])}"

    return {
        "applicant": item["Name"],
        "application (retroactive time)": application_time,
        "type": item["ReqTypeText"],
        "reason for application (retroactive)": item["ReqReasonText"],
        "request date": datetime.strptime(
            item["ReqStartDate"], "%Y-%m-%dT%H:%M:%S.%f"
        ).strftime("%Y-%m-%d %H:%M"),
        "approvalName": item["ApprovalName"],
        "approvalDate": datetime.strptime(
            item["ApprovalDate"], "%Y-%m-%dT%H:%M:%S.%f"
        ).strftime("%Y-%m-%d %H:%M"),
    }


def create_dataframe(data):
    """Create a DataFrame from the JSON data."""
    records = [prepare_record(item) for item in data]
    return pd.DataFrame(records)


def save_to_excel(df, file_path):
    """Save the DataFrame to an Excel file."""
    df.to_excel(file_path, index=False)
    print(f"Excel file created at: {file_path}")


def main():
    file_path = "test.json"
    data = load_json(file_path)
    df = create_dataframe(data)
    save_to_excel(df, "applications.xlsx")


if __name__ == "__main__":
    main()
