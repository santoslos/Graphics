import matplotlib.pyplot as plt
import numpy as np
import io, base64
from graphic.models import Graphic
from math import *
from celery import shared_task
from django.core.files.images import ImageFile


@shared_task
def plot(f, bot, top, step):
    x = np.arange(bot, top, step)
    y = []
    for i in x:
        exec(f'def func(x):\n return {f}\ny.append(func(i))')
    y = np.array(y)
    fig = plt.figure(figsize=(10, 4))
    print(x, y)
    plt.plot(x, y)
    figure = io.BytesIO()
    plot_instance = Graphic.objects.get(function=f, step=step,
                                        bot_interval=bot, top_interval=top, figure='')
    print(y)
    if len(y) > 0:
        plt.savefig(figure, format="png")
        content_file = ImageFile(figure)
        plot_instance.figure.save(f + '.png', content_file)
    else:
        plot_instance.figure.name = 'Ошибка'
        plot_instance.save()
