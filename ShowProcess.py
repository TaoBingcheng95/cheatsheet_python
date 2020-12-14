#!/usr/local/lib
# -*- coding: UTF-8 -*-
"""
@author: Comet

进度条类

"""


import sys


class ShowProcess():
    """
    ShowProcess : 调用该类相关函数即可实现处理进度的显示
        num : 当前处理进度
        total : 总共需要处理的次数
        bar_length : 进度条长度, 默认为50
    """

    def __init__(self, total):
        """
        初始化函数，需要知道总共的处理次数total
        """
        self.total = total
        self.num = 0
        self.bar_length = 50

    def test(self):
        import time
        for proessing in range(2):
            info_show = 'Processing {}'.format(proessing+1)
            process_bar = ShowProcess(self.total)
            for step in range(self.total):
                process_bar.show_process(info=info_show)
                time.sleep(0.05)
            process_bar.close()

    def show_process(self, i=None, info='Prcessing!'):
        """
        显示函数，根据当前的处理进度i显示进度
        效果为[>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>]100.00%
        """
        if i is not None:
            self.num = i
        else:
            self.num += 1
    
        rate = float(self.num) / self.total
        rate_num = int(self.bar_length * rate)
        percent = 100.0 * rate
        process_bar = "\r[{}{}]{:.1f}% {}".format('>' * rate_num, ' ' * (self.bar_length-rate_num), percent, info)
        sys.stdout.write(process_bar)
        sys.stdout.flush()
  
    def close(self, words='done'):
        print("\n{}".format(words))
        self.num = 0



def test_process_bar():
    max_steps = 50
    process_bar = ShowProcess(max_steps)
    process_bar.test()    
    return None


if __name__=='__main__':
    
    test_process_bar()
