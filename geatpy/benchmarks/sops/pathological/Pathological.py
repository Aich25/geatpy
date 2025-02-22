# -*- coding: utf-8 -*-
import numpy as np

import geatpy as ea


class Pathological(ea.Problem):  # 继承Problem父类
    def __init__(self, Dim=30):  # Dim : 决策变量维数
        name = 'Pathological'  # 初始化name（函数名称，可以随意设置）
        M = 1  # 初始化M（目标维数）
        maxormins = [1] * M  # 初始化maxormins（目标最小最大化标记列表，1：最小化该目标；-1：最大化该目标）
        varTypes = [0] * Dim  # 初始化varTypes（决策变量的类型，0：实数；1：整数）
        lb = [-100] * Dim  # 决策变量下界
        ub = [100] * Dim  # 决策变量上界
        lbin = [1] * Dim  # 决策变量下边界（0表示不包含该变量的下边界，1表示包含）
        ubin = [1] * Dim  # 决策变量上边界（0表示不包含该变量的上边界，1表示包含）
        # 调用父类构造方法完成实例化
        ea.Problem.__init__(self, name, M, maxormins, Dim, varTypes, lb, ub, lbin, ubin)

    def evalVars(self, Vars):  # 目标函数
        x1 = Vars[:, [0]]
        x2 = Vars[:, [1]]
        f = 0.5 + ((np.sin(np.sqrt(np.abs(x1 ** 2 + x2 ** 2)))) ** 2 - 0.5) / ((1 + 0.001 * (x1 ** 2 + x2 ** 2)) ** 2)
        return f

    def calReferObjV(self):  # 设定目标数参考值（本问题目标函数参考值设定为理论最优值）
        referenceObjV = np.array([[0]])
        return referenceObjV
