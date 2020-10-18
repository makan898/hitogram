import cv2
import matplotlib.pyplot as plt
import numpy as np


def display(img):
    # ヒストグラムを作成する。
    n_bins = 256  # ビンの数
    hist_range = [0, 256]  # 集計範囲
    
    hists = []
    channels = {0: "blue", 1: "green", 2: "red"}
    for ch in channels:
        hist = cv2.calcHist(
            [img], channels=[ch], mask=None, histSize=[n_bins], ranges=hist_range
        )
        hist = hist.squeeze(axis=-1)#axis=-1 とした場合は、一番最後の軸で結合します。
        hists.append(hist)#リストの最後に付加する
    
    
    # 描画する。
    def plot_hist(bins, hist, color):
        centers = (bins[:-1] + bins[1:]) / 2
        widths = np.diff(bins)
        ax.bar(centers, hist, width=widths, color=color)
    
    #Return evenly spaced numbers over a specified interval.
    #返回指定间隔内的等间隔数字。
    bins = np.linspace(*hist_range, n_bins + 1)
    
    fig, ax = plt.subplots()
    #Set the x ticks with list of ticks
    #用刻度列表设置x刻度
    ax.set_xticks([0, 256]) 
    #Set the x-axis view limits.
    #设置x轴视图限制。
    ax.set_xlim([0, 256])
    ax.set_xlabel("sample")
    #forループで複数のリストの要素を取得
    for hist, color in zip(hists, channels.values()):
        plot_hist(bins, hist, color=color)
    plt.show()
    
img = cv2.imread("sample.jpg")
display(img)