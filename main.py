import mediapipe as mp
import cv2

cap = cv2.VideoCapture(0)
facemd = mp.solutions.face_mesh
face = facemd.FaceMesh(refine_landmarks = True)
facecon = mp.solutions.face_mesh_connections

while 1:
    success, read = cap.read()
    read = cv2.flip(read, 1)
    rgb = cv2.cvtColor(read, cv2.COLOR_BGR2RGB)
    result = face.process(rgb)
    mesh = result.multi_face_landmarks
    h, w, _ = read.shape
    if mesh:
        landmarks = mesh[0].landmark
        for landmark in landmarks:
            x = int(landmark.x * w)
            y = int(landmark.y * h)

    cv2.imshow("Video", read)
    if cv2.waitKey(1) == ord('q'):
        break