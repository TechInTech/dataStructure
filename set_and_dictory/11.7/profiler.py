# !/usr/bin/env python
# -*- coding:utf-8 -*-

# @Time    : 2019/2/25 22:11
# @Author  : Despicable Me
# @Email   : 
# @File    : profiler.py
# @Software: PyCharm
# @Explain :

from hashtable import HashTable

class Profiler(object):
    """探测器类"""

    def __init__(self):
        self._table = None    # 哈希表
        self._collisions = 0   # 冲突的总次数
        self._probeCount = 0  # 解决冲突需要的总探测次数

    def test(self, table, data):
        """返回带有给定数据集的一个表上的探测器"""
        self._table = table
        self._collisions = 0
        self._probeCount = 0
        self._result = "Load Factor  Item Inserted " + \
            " Home Index  Actual Index   Probes\n"
        for item in data:
            loadFactor = self._table.loadFactor()
            self._table.insert(item)
            homeIndex = self._table.homeIndex()
            actualIndex = self._table.actualIndex()
            probes = self._table.probeCount()
            self._probeCount += probes

            # probes>0,表明发生了探测，记录冲突次数
            if probes > 0:
                self._collisions += 1

            line = "%8.3f%14d%12d%12d%14d" % (loadFactor, item, \
                                              homeIndex, actualIndex, probes)
            self._result += line + "\n"
        self._result += "Total collisions: " + str(self._collisions) + "\nTotal probes: " +\
            str(self._probeCount) + "\nAverage probes per collisions: " + \
                        str(self._probeCount / self._collisions)

    def __str__(self):
        if self._table is None:
            return "No test has been run yet."
        else:
            return self._result

    def collisions(self):
        return self._collisions

    def probeCount(self):
        return self._probeCount

def main():
    """Create a table with 8 cells, an identity hash function and liner probeing."""
    table = HashTable(8, lambda x: x)
    # The data are the numbers from 10 throgh 70, by 10
    data = list(range(10, 71, 10))
    profiler = Profiler()
    profiler.test(table, data)
    print(profiler)

if __name__ == "__main__":
    main()