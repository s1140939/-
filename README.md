# 雞蛋自動辨識機器人 - 期中專案

## 專案簡介
本專案為「基礎程式設計(二)」期中作業。主題為**自動辨識（YOLO模型）** 。
我開發了一個基於 YOLOv11 的即時影像辨識系統，能透過 Webcam 自動偵測畫面中的雞蛋，未來可整合至農業收蛋自動化硬體中。

## 技術說明
* **模型架構**: Ultralytics YOLOv11
* **訓練環境**: Google Colab (Tesla T4 GPU)
* **開發工具**: VS Code, Python 3.12
* **資料來源**: Roboflow 雞蛋標註資料集

## 執行方式
1. 安裝環境套件：
   ```bash
   pip install -r requirements.txt

## 開發挑戰與解決 (Troubleshooting)
1. 權重載入問題：發現模型將雞蛋誤認為 "orange"。
2. 解決方案：透過 model.names 驗證模型類別，發現問題出在鏡頭讀取或顯示暫存，重新開啟VS code並使用絕對路徑載入而解決。
3. 環境 Bug：修正 NameError: name 'cv2' is not defined，確保 OpenCV 套件正確導入。

## 執行成果
1. 辨識類別：{0: 'egg'}。
2. 辨識率：平均置信度（Confidence）達到 0.90 左右。