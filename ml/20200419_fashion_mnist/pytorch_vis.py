import torch
import matplotlib.pyplot as plt
from torch.nn import functional as F

def images_to_probs(net, images):
    output = net(images)
    probs, predictions = F.softmax(output, 1).max(1)
    return predictions, probs

def plot_classes_preds(preds, probs, images, labels, classes, img_per_row=4, 
                       subplot_kw={}, **fig_kw):
    n = images.size()[0]
    fig, ax = plt.subplots((n + img_per_row - 1) // img_per_row, img_per_row, 
                           squeeze=False,
                          sharex=True, sharey=True,
                          subplot_kw=subplot_kw,
                           **fig_kw
                          )
    
    for idx in range(n):
        ax_idx = ax.ravel()[idx]
        matplotlib_imshow(images[idx], one_channel=True, ax=ax_idx)
        
        ax_idx.set_title("{0}, {1:.1f}%\n(label: {2})".format(
            classes[preds[idx]],
            probs[idx] * 100.0,
            classes[labels[idx]]),
                    color=("green" if preds[idx]==labels[idx].item() else "red"))
    return fig

def matplotlib_imshow(img, one_channel=False, ax=plt):
    if one_channel:
        img = img.mean(dim=0)
    img = img / 2 + 0.5     # unnormalize
    npimg = img.numpy()
    if one_channel:
        ax.imshow(npimg, cmap="Greys")
    else:
        ax.imshow(np.transpose(npimg, (1, 2, 0)))