students = ["Ahmet", "Ayşe", "Mehmet", "Zeynep"]
here = ["Ahmet", "Ayşe", "Zeynep"]
absent = []
for student in students:
  if student not in here:
    absent.append(student)
print(f"Yoklamaya katılmayanlar: {absent}")
