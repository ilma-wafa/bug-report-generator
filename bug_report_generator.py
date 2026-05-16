import datetime

def get_bug_details():

    print("=== Bug Report ===")
    print()
    print("Please answer the following questions:")

    title = input("Bug Title: ") #input asks the user to type
    bug_type = input("Bug Type (syntax/runtime/logic/ui): ")
    steps= input("Steps to Reproduce: ")
    expected = input("Expected Behavior: ")
    actual = input("Actual Behavior: ")
    severity = input("Severity (low/medium/high/critical): ")

    date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")  

    return{
        "title": title,
        "bug_type": bug_type,
        "steps": steps,
        "expected": expected,
        "actual": actual,
        "severity": severity,
        "date": date
     } #return the data collected by function

def format_report(report):
    print()
    print("=" * 40)
    print("         BUG REPORT")
    print("=" * 40)
    print(f"Title:     {report['title']}")
    print(f"Type:      {report['bug_type']}")
    print(f"Severity:  {report['severity']}")
    print("-" * 40)
    print(f"Steps to Reproduce:\n  {report['steps']}")
    print(f"Expected Behavior:\n  {report['expected']}")
    print(f"Actual Behavior:\n  {report['actual']}")
    print("=" * 40)
    print(f"Date:      {report['date']}")

def save_report(report):
    filename = f"bug_report_{report['title'].replace(' ', '_')}.txt"
    with open(filename, 'w') as f:
        f.write("=" * 40 + "\n")
        f.write("         BUG REPORT\n")
        f.write("=" * 40 + "\n")
        f.write(f"Title:     {report['title']}\n")
        f.write(f"Type:      {report['bug_type']}\n")
        f.write(f"Severity:  {report['severity']}\n")
        f.write("-" * 40 + "\n")
        f.write(f"Steps to Reproduce:\n  {report['steps']}\n")
        f.write(f"Expected Behavior:\n  {report['expected']}\n")
        f.write(f"Actual Behavior:\n  {report['actual']}\n")
        f.write("=" * 40 + "\n")
        f.write(f"Date:      {report['date']}\n")
    print(f"Date:      {report['date']}")
        
    print(f"\nReport saved as: {filename}")

report = get_bug_details() #calling the function
format_report(report)
save_report(report)
