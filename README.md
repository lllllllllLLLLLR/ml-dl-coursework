# ML & DL Coursework — PyTorch, CNNs, Classic Models

A grab-bag of undergraduate machine-learning and deep-learning coursework notebooks, covering basic PyTorch model building, CNNs on CIFAR-10/100, decision trees / k-means / PCA on the digits dataset, NLP preprocessing exercises, and a Raspberry Pi car-control lab report.

## Highlights
- **PyTorch fundamentals**: simple fully-connected network on MNIST, and a from-scratch MLP training loop with `nn.Module` + `optim`.
- **CNN assignments**: convolutional networks trained on CIFAR-10 / CIFAR-100, including transfer learning with pretrained `torchvision` models and a confusion-matrix evaluation walkthrough.
- **Classical ML**: decision trees with `GridSearchCV`, k-means clustering with ARI, and PCA visualisation on `sklearn.datasets.load_digits`.
- **NLP preprocessing**: regex + `nltk` stopword removal and Porter stemming practice.
- **Lab report**: a group-written report on keyboard-controlled movement of a Raspberry Pi robot car (ROS setup, SSH, motor drivers).

## Quick start
```bash
pip install -r requirements.txt
# Datasets (CIFAR-10/100, MNIST) download automatically via torchvision on first run;
# place them under ./data/raw/ if you want to cache them locally.
jupyter notebook
```

## Layout
```
.
├── 深度学习HW1.ipynb                    # first PyTorch homework
├── 人工智能基础_HW1.ipynb / project1.ipynb  # PyTorch CIFAR training notebooks
├── HW2_CNN.ipynb                        # CNN assignment (CIFAR-10/100, transfer learning)
├── 深度学习基础- CNN.ipynb              # CNN basics + confusion matrix
├── 神经网络简单模型搭建.ipynb           # minimal MLP from scratch (numpy)
├── Assignment2.ipynb                    # probability / pattern-recognition written answers
├── Exercise2.ipynb                      # sklearn decision tree, k-means, PCA on digits
├── Practice.ipynb                       # nltk text preprocessing drills
├── 实验报告1.ipynb                       # Raspberry Pi car-control lab report (group)
├── Homework.ipynb                       # stub notebook
├── PythonHW7主要知识点与错误之处.ipynb  # stub notebook
├── 人工智能的程序设计_CIFAR_10.ipynb    # stub notebook
├── 人工智能的程序设计_CIFAR_100.ipynb   # stub notebook
├── HW13_1_20307130309_卢冉.py           # pandas race-time processing exercise
├── requirements.txt
└── README.md
```

## Notes
- These are undergraduate coursework / lab exercises. Several notebooks are empty stubs (no cells filled in at the time of archiving) and are kept for completeness.
- `实验报告1.ipynb` was a group lab; the Raspberry Pi IP address and SSH username have been replaced with `<raspberry-pi-ip>` / `<user>` placeholders.
- Raw datasets (CIFAR-10/100 archives, MNIST ubyte files) and model weights are **not** committed; they are downloaded at runtime by `torchvision` / `sklearn`.
- No API keys, passwords, or private addresses are hard-coded in any committed file.
