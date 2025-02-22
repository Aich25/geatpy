# -*- coding: utf-8 -*-
import numpy as np
import geatpy as ea


class UF2(ea.Problem):  # 继承Problem父类
    def __init__(self, M=None, Dim=30):  # M : 目标维数；Dim : 决策变量维数
        name = 'UF2'  # 初始化name（函数名称，可以随意设置）
        M = 2  # 初始化M（目标维数）
        maxormins = [1] * M  # 初始化maxormins（目标最小最大化标记列表，1：最小化该目标；-1：最大化该目标）
        varTypes = [0] * Dim  # 初始化varTypes（决策变量的类型，0：实数；1：整数）
        lb = [0] + [-1] * (Dim - 1)  # 决策变量下界
        ub = [1] * Dim  # 决策变量上界
        lbin = [1] * Dim  # 决策变量下边界（0表示不包含该变量的下边界，1表示包含）
        ubin = [1] * Dim  # 决策变量上边界（0表示不包含该变量的上边界，1表示包含）
        # 调用父类构造方法完成实例化
        ea.Problem.__init__(self, name, M, maxormins, Dim, varTypes, lb, ub, lbin, ubin)

    def evalVars(self, Vars):  # 目标函数
        x1 = Vars[:, [0]]
        J1 = np.array(list(range(2, self.Dim, 2)))
        J2 = np.array(list(range(1, self.Dim, 2)))
        yJ1 = Vars[:, J1] - (
                0.3 * x1 ** 2 * np.cos(24 * np.pi * x1 + 4 * (J1 + 1) * np.pi / self.Dim) + 0.6 * x1) * np.cos(
            6 * np.pi * x1 + (J1 + 1) * np.pi / self.Dim)
        yJ2 = Vars[:, J2] - (
                0.3 * x1 ** 2 * np.cos(24 * np.pi * x1 + 4 * (J2 + 1) * np.pi / self.Dim) + 0.6 * x1) * np.sin(
            6 * np.pi * x1 + (J2 + 1) * np.pi / self.Dim)
        f1 = x1 + 2 * np.mean((yJ1) ** 2, 1, keepdims=True)
        f2 = 1 - np.sqrt(np.abs(x1)) + 2 * np.mean((yJ2) ** 2, 1, keepdims=True)
        f = np.hstack([f1, f2])
        return f

    def calReferObjV(self):  # 设定目标数参考值（本问题目标函数参考值设定为理论最优值，即“真实帕累托前沿点”）
        N = 10000  # 生成10000个参考点
        ObjV1 = np.linspace(0, 1, N)
        ObjV2 = 1 - np.sqrt(ObjV1)
        referenceObjV = np.array([ObjV1, ObjV2]).T
        return referenceObjV
