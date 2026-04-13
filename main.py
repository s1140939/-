import cv2
import os
from ultralytics import YOLO

# 獲取當前程式碼所在的資料夾路徑
current_path = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(current_path, 'best.pt')

# 確認檔案是否存在
if os.path.exists(model_path):
    print(f"✅ 成功找到自定義權重：{model_path}")
    model = YOLO(model_path)
else:
    print("❌ 警告：在當前資料夾找不到 best.pt！請檢查檔案位置。")
    # 強迫停止，不要讓它跑預設模型
    exit()

# 2. 開啟 Webcam (0 通常是電腦內建鏡頭)
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("錯誤：無法開啟攝影機")
    exit()

print("按下 'q' 鍵可以退出程式")

while True:
    # 讀取攝影機畫面
    ret, frame = cap.read()
    if not ret:
        break

    # 3. 進行影像辨識
    # conf=0.5 代表信心值超過 50% 才會顯示
    results = model.predict(source=frame, conf=0.5, show=False)

    # 4. 在畫面上繪製辨識結果
    annotated_frame = results[0].plot()

    # 顯示視窗
    cv2.imshow("Egg Detection - Midterm Project", annotated_frame)

    # 按下 'q' 鍵退出
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 釋放資源
cap.release()
cv2.destroyAllWindows()