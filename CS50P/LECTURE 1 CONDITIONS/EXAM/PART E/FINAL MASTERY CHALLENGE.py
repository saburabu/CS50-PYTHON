name = str(input("Name: "))
score = int(input("Score: "))
attendance = int(input("Attendance: "))
name = name.strip().title()

def calculate_result(score, attendance):
    if 0 <= score <= 100 and 0 <= attendance <= 100:
        if score < 50:
            return f"============================\nName: {name}\nScore: {score}\nAttendance: {attendance}\nFAIL\n============================"
        elif score >= 50 and attendance >= 75:
            return f"============================\nName: {name}\nScore: {score}\nAttendance: {attendance}\nPASS\n============================"
        elif score >= 50 and attendance <75:
            return f"============================\nName: {name}\nScore: {score}\nAttendance: {attendance}\nCONDITIONAL PASS\n============================"
    else:
        return f"INVALID"
result = calculate_result(score, attendance)
print(result)