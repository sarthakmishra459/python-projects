import face_recognition
import cv2
import numpy as np
import csv
from datetime import datetime

# Load known Faces
sarthaks_image = face_recognition.load_image_file("faces/sarthak.jpg")
sarthak_encoding = face_recognition.face_encodings(sarthaks_image)[0]

priyabrata_image = face_recognition.load_image_file("faces/priyabrata.jpg")
priyabrata_encoding = face_recognition.face_encodings(priyabrata_image)[0]

# Create a list of known face encodings and names
known_face_encodings = [sarthak_encoding, priyabrata_encoding]
known_face_names = ["Sarthak", "Priyabrata"]

# Create a dictionary to track attendance
attendance_dict = {name: False for name in known_face_names}

# Initialize video capture
video_capture = cv2.VideoCapture(0)

# Get current date
now = datetime.now()
current_date = now.strftime("%Y-%m-%d")

# Open CSV file for writing attendance
with open(f"{current_date}.csv", "w", newline="") as f:
    lnwriter = csv.writer(f)

    while True:
        ret, frame = video_capture.read()
        small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
        rgb_small_frame = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)

        # Recognize faces
        face_locations = face_recognition.face_locations(rgb_small_frame)
        face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

        # Initialize name variable outside the loop
        name = "Unknown"

        for face_encoding in face_encodings:
            matches = face_recognition.compare_faces(known_face_encodings, face_encoding, tolerance=0.6)

            if True in matches:
                first_match_index = matches.index(True)
                name = known_face_names[first_match_index]
                if not attendance_dict[name]:
                    attendance_dict[name] = True
                    current_time = now.strftime("%H:%M:%S")
                    lnwriter.writerow([name, current_time])

        font = cv2.FONT_HERSHEY_SIMPLEX
        bottomLeftCornerOfText = (10, 100)
        fontScale = 1.5
        fontColor = (255, 0, 0)
        thickness = 3
        lineType = 2
        cv2.putText(frame, name, bottomLeftCornerOfText, font, fontScale, fontColor, thickness, lineType)
        cv2.imshow("Attendance", frame)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

# Write remaining students' attendance status
with open(f"{current_date}.csv", "a", newline="") as f:
    writer = csv.writer(f)
    for student in known_face_names:
        status = "Present" if attendance_dict[student] else "Unauthorized"
        writer.writerow([student, status])

video_capture.release()
cv2.destroyAllWindows()
