scores = [72, 45, 90, 61, 38]

passed = 0
failed = 0
total_score = 0

for score in scores:
    total_score = total_score + score

    if score >= 80:
        grade = "A"
    elif score >= 70:
        grade = "B"
    elif score >= 50:
        grade = "C"
    else:
        grade = "F"

    if score >= 50:
        passed = passed + 1
    else:
        failed = failed + 1

    print(f"Score: {score} -> Grade: {grade}")

average = total_score / len(scores)

print(f"\nPassed: {passed}")
print(f"Failed: {failed}")
print(f"Average: {round(average, 1)}")
