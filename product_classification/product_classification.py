import os
os.makedirs("../datasets/", exist_ok=True)
from roboflow import Roboflow
rf = Roboflow(api_key="Rig4Wm7yMAhBIHmqxQIR")
project = rf.workspace("supermarketproductdetection").project("product_classification-b0ygy")
version = project.version(2)
dataset = version.download("folder")

dataset_name = dataset.location.split(os.sep)[-1]
os.environ["DATASET_NAME"] = dataset_name

# python train.py --model yolov5s-cls.pt --data datasets --epochs 100 --img 128 --pretrained weights/yolov5s-cls.pt