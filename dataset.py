import torch
import torchvision
from torchvision import transforms
from torch.utils.data import DataLoader

import train



def get_train_data_loader() -> torch.utils.data.DataLoader:
    """
    获取训练数据
    :return: 训练数据
    """
    print("----> 正在加载训练集")
    train_transform = transforms.Compose(
        [
            transforms.Resize(size=train.IMAGE_SIZE),  # 调整图像大小
            transforms.TrivialAugmentWide(),  # 图像增强
            transforms.ToTensor(),  # 0~255 像素值转为 0.0~1.0 的 tensor
        ]
    )
    train_data = torchvision.datasets.ImageFolder(
        root=train.TRAIN_DIR,  # 训练集目录地址
        transform=train_transform,  # 图片数据的转换
        target_transform=None,  # 对标签执行变换
    )

    class_names = train_data.classes  # ['cats', 'dogs']
    class_dict = train_data.class_to_idx  # {'cats': 0, 'dogs': 1}
    print("----> 训练集长度: ", len(train_data))
    print("----> 训练集类型及标签: ", class_names, class_dict)

    # 将训练数据集转换为 DataLoader
    train_dataloader = DataLoader(
        dataset=train_data,
        batch_size=train.BATCH_SIZE,  # 每次训练的样本数
        shuffle=True,  # 打乱训练集的数据
        num_workers=train.NUM_WORKERS,  # 子进程数
    )
    print("----> 加载训练集完成")
    return train_dataloader


def get_test_data_loader() -> torch.utils.data.DataLoader:
    """
    获取测试数据
    :return: 测试数据
    """
    print("----> 正在加载测试集")
    test_transform = transforms.Compose(
        [
            transforms.Resize(size=train.IMAGE_SIZE),  # 调整图像大小
            transforms.ToTensor(),  # 0~255 像素值转为 0.0~1.0 的 tensor
        ]
    )

    test_data = torchvision.datasets.ImageFolder(
        root=train.TEST_DIR,  # 训练集目录地址
        transform=test_transform,  # 图片数据的转换
        target_transform=None,  # 对标签执行变换
    )

    class_names = test_data.classes  # ['cats', 'dogs']
    class_dict = test_data.class_to_idx  # {'cats': 0, 'dogs': 1}
    print("----> 测试集长度: ", len(test_data))
    print("----> 测试集类型及标签: ", class_names, class_dict)

    # 将测试数据集转换为 DataLoader
    test_dataloader = DataLoader(
        dataset=test_data,
        batch_size=train.BATCH_SIZE,  # 每次训练的样本数
        shuffle=False,  # 一般不打乱测试集的数据
        num_workers=train.NUM_WORKERS,  # 子进程数
    )
    print("----> 加载测试集完成")
    return test_dataloader


def get_pred_data_loader():
    print("----> 正在加载识别目标")
    print("----> 加载识别目标完成")
    pass


if __name__ == "__main__":
    train_data_loader = get_train_data_loader()
    test_data_loader = get_test_data_loader()
    print("----> Data Loader Length: ", len(train_data_loader), len(test_data_loader))
