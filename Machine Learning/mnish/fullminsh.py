import numpy as np
import torch
from torch.optim.lr_scheduler import StepLR
from torchvision.datasets import mnist
import matplotlib.pyplot as plt
from torch import nn
from torch.autograd import Variable
from torch.utils.data import DataLoader


def data_tf(x):
    x = np.array(x, dtype="float32") / 255
    x = (x - 0.5) / 0.5
    x = x.reshape((-1))  # 变成1行n列
    x = torch.from_numpy(x)
    return x


# 加载mnist数据集
train_set = mnist.MNIST("./data", train=True, transform=data_tf, download=False)
test_set = mnist.MNIST("./data", train=False, transform=data_tf, download=False)

a, a_label = train_set[0]
print(a.shape)
print(a_label)

# for i in range(1, 26):
#     plt.subplot(5, 5, i)
#     plt.xticks([])  # 去掉坐标系
#     plt.yticks([])
#     plt.imshow(train_set.data[i].numpy(), cmap="gray")
#     plt.title("%i" % train_set.targets[i])
# plt.subplots_adjust(wspace=0, hspace=1)  # 调整子图间距
# plt.show()

train_data = DataLoader(train_set, batch_size=64, shuffle=True)
test_data = DataLoader(test_set, batch_size=128, shuffle=False)

a, a_label = next(iter(train_data))
print(a.shape)
print(a_label.shape)

net = nn.Sequential(
    nn.Linear(784, 400),
    nn.ReLU(),
    nn.Linear(400, 200),
    nn.ReLU(),
    nn.Linear(200, 100),
    nn.ReLU(),
    nn.Linear(100, 10),
    nn.ReLU()
)
if torch.cuda.is_available():
    net = net.cuda()

criterion = nn.CrossEntropyLoss()
optimizer = torch.optim.SGD(net.parameters(), 1e-1)

losses = []
acces = []
eval_losses = []
eval_acces = []
# scheduler = StepLR(optimizer, step_size=30, gamma=0.1)

for e in range(20):  # 训练20轮
    train_loss = 0
    train_acc = 0
    net.train()
    for im, label in train_data:
        if torch.cuda.is_available():
            im = Variable(im).cuda()
            label = Variable(label).cuda()
        else:
            im = Variable(im)
            label = Variable(label)

        # 前向传播
        out = net(im)

        loss = criterion(out, label)

        # 反向传播
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
        # scheduler.step()
        # 记录误差
        train_loss += loss.item()

        # 计算分类的准确率
        # max函数参数1表示按行取最大值，第一个返回值是值，第二个返回值是下标
        # pred是一個1*64的向量
        _, pred = out.max(1)
        num_correct = (pred == label).sum().item()
        acc = num_correct / im.shape[0]
        train_acc += acc

    # 此时一轮训练完了
    losses.append(train_loss / len(train_data))
    acces.append(train_acc / len(train_data))

    # 在测试集上检验效果
    eval_loss = 0
    eval_acc = 0
    net.eval()
    for im, label in test_data:
        if torch.cuda.is_available():
            im = Variable(im).cuda()
            label = Variable(label).cuda()
        else:
            im = Variable(im)
            label = Variable(label)
        # 前向传播
        out = net(im)

        # 计算误差
        loss = criterion(out, label)
        eval_loss += loss.item()

        # 计算准确率
        _, pred = out.max(1)
        num_correct = (pred == label).sum().item()
        acc = num_correct / im.shape[0]
        eval_acc += acc

    eval_losses.append(eval_loss / len(test_data))
    eval_acces.append(eval_acc / len(test_data))

    print('epoch: {}, Train Loss: {:.6f}, Train Acc: {:.6f}, Eval Loss: {:.6f}, Eval Acc: {:.6f}'
          .format(e, train_loss / len(train_data), train_acc / len(train_data),
                  eval_loss / len(test_data), eval_acc / len(test_data)))

plt.subplot(2, 2, 1)
plt.title("train loss")
plt.plot(np.arange(len(losses)), losses)
plt.grid()
plt.show()
plt.subplot(2, 2, 2)
plt.title("train acc")
plt.plot(np.arange(len(acces)), acces)
plt.grid()
plt.show()
plt.subplot(2, 2, 3)
plt.title("test loss")
plt.plot(np.arange(len(eval_losses)), eval_losses)
plt.grid()
plt.show()
plt.subplot(2, 2, 4)
plt.title("test acc")
plt.plot(np.arange(len(eval_acces)), eval_acces)
plt.grid()
plt.subplots_adjust(wspace=0.5, hspace=0.5)
plt.show()
