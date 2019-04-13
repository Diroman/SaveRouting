import math

t = 0.3747 * 10 ** -3
graph = []

connection = [[1, 2], [1, 3], [1, 4], [1, 5], [1, 9], [1, 12], [1, 15], [1, 16], [1, 17], [1, 19], [1, 27],
              [2, 7], [2, 8], [2, 10], [2, 21], [2, 23], [3, 10], [3, 11], [3, 14], [4, 6], [4, 7], [4, 13],
              [5, 8], [5, 20], [5, 24], [6, 7], [6, 22], [6, 25], [7, 50], [8, 13], [8, 18], [9, 18], [9, 31],
              [9, 32], [10, 11], [10, 22], [10, 28], [11, 26], [12, 26], [12, 32], [13, 35], [14, 18], [15, 21],
              [15, 36], [15, 37], [15, 40], [16, 31], [16, 33], [16, 38], [17, 22], [17, 23], [17, 34], [17, 36],
              [18, 21], [19, 20], [19, 28], [19, 30], [19, 34], [20, 29], [20, 31], [20, 43], [21, 24], [21, 45],
              [22, 40], [23, 36], [23, 39], [24, 35], [24, 37], [25, 44], [25, 47], [26, 32], [26, 41], [27, 38],
              [27, 41], [28, 31], [28, 35], [29, 30], [29, 34], [30, 45], [31, 50], [32, 33], [32, 50], [33, 50],
              [34, 39], [34, 50], [35, 36], [36, 50], [37, 40], [38, 40], [39, 42], [39, 48], [39, 49], [40, 50],
              [41, 43], [41, 46], [41, 47], [42, 43], [42, 44], [42, 46], [42, 49], [43, 47], [43, 48], [44, 45],
              [44, 46], [44, 49], [45, 46], [45, 47], [46, 48], [47, 50], [48, 49], [48, 50], [49, 50]]

alpha = [1806, 1383, 873, 1127, 685, 549, 769, 694, 353, 836, 329, 1101, 1484, 325, 1024, 1971, 1948, 1661, 549,
         1372, 1149, 844, 1473, 911, 1205, 1100, 921, 1023, 413, 814, 588, 484, 729, 1497, 801, 791, 1541, 1909,
         1571, 815, 913, 654, 1849, 1989, 1904, 1909, 1573, 1989, 1394, 480, 934, 1329, 447, 1463, 886, 1087, 1810,
         1385, 404, 734, 1796, 1727, 1174, 996, 1742, 804, 512, 780, 974, 1001, 294, 1816, 1110, 664, 1335, 325,
         1607, 1843, 828, 476, 1294, 1369, 505, 319, 1092, 1767, 515, 1222, 1832, 537, 373, 1293, 1516, 622, 1343,
         2000, 659, 1716, 1027, 1455, 872, 925, 466, 1834, 634, 521, 900, 1745, 1865, 1237, 1223, 1228]

def F(a):
    return math.pi ** (-a*t)

class Node:
    def __init__(self, num, alpha, conn):
        self.p = 0
        self.p_buf = [1]
        self.num = num
        self.alpha = alpha
        self.count_ref = 0
        self.current_ref = 0
        self.connection = conn

    def __str__(self):
        return "Number: " + str(self.num) + "\nRef: " + str(self.count_ref) + "\n"

def CreateNode():

    for i in range(50):
        buf = []
        buf_alf = []
        for j, connect in enumerate(connection):
            if connect[0] == i + 1:
                buf.append(connect[1])
                buf_alf.append(alpha[j])

        graph.append(Node(i+1, buf_alf, buf))

def CalcRef():

    for i, node in enumerate(connection):
        graph[node[1]-1].count_ref += 1

def CalcProbability(node):

    run = set()
    while True:
        n = 0
        for i, node in enumerate(graph):
            if node.count_ref == node.current_ref and node.num not in run:
                run.add(node.num)
                mul = 1
                for i, x in enumerate(node.p_buf): mul *= x
                node.p = mul
                n += 1
                for i, child in enumerate(node.connection):
                    graph[child-1].current_ref += 1
                    p = node.p * (1 - F(node.alpha[i]))
                    graph[child-1].p_buf.append(p)
                    a = 2
        if n == 50:
            break

CreateNode()

CalcRef()
graph[0].p = 1
CalcProbability(graph[0])

p = 1 - graph[49].p

print("Result: ", p)