# -*- coding: utf-8 -*-
import numpy as np

import geatpy as ea


class Beale(ea.Problem):  # 继承Problem父类
    def __init__(self, Dim=None):  # Dim : 决策变量维数
        name = 'Beale'  # 初始化name（函数名称，可以随意设置）
        M = 1  # 初始化M（目标维数）
        Dim = 2  # 初始化Dim（决策变量维数）
        maxormins = [1] * M  # 初始化maxormins（目标最小最大化标记列表，1：最小化该目标；-1：最大化该目标）
        varTypes = [0] * Dim  # 初始化varTypes（决策变量的类型，0：实数；1：整数）
        lb = [-4.5, -100]  # 决策变量下界
        ub = [100, 4.5]  # 决策变量上界
        lbin = [1] * Dim  # 决策变量下边界（0表示不包含该变量的下边界，1表示包含）
        ubin = [1] * Dim  # 决策变量上边界（0表示不包含该变量的上边界，1表示包含）
        # 调用父类构造方法完成实例化
        ea.Problem.__init__(self, name, M, maxormins, Dim, varTypes, lb, ub, lbin, ubin)

    def evalVars(self, Vars):  # 目标函数
        x = Vars[:, [0]]
        y = Vars[:, [1]]
        f = (1.5 - x + x * y) ** 2 + (2.25 - x + x * y ** 2) ** 2 + (2.625 - x + x * y ** 3) ** 2
        return f

    def calReferObjV(self):  # 设定目标数参考值（本问题目标函数参考值设定为理论最优值）
        referenceObjV = np.array([[0]])
        return referenceObjV
