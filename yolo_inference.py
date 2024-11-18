from ultralytics import YOLO 

#model = YOLO('yolov8x')
model = YOLO('models/yolov5_last.pt')

#result = model.predict('input_videos/input_video.mp4',conf=0.2, save=True) #assigns player ids (see  track)
print(result)

result = model.track('input_videos/input_video.mp4',conf=0.2, save=True) #assigns player ids (see  track)
# print(result)
# print("boxes:")
# for box in result[0].boxes:
#     print(box)