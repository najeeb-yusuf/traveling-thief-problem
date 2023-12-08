import sys
import numpy as np
import pandas as pd
import random
import os
import math
import csv


LEAST_SOLUTIONS = []
CITY_DATA = []
KNAPSACK_CAPACITY = 0
ITEMS_DATA = []
NUMBER_OF_ITEMS = 0
MIN_SPEED = 0.0
MAX_SPEED = 0.0
# Set the random seed for reproducability of results
# random.seed(1000)

# RENTING RATIO
R = 5.1
alpha = 0.4
beta = 0.6
path = [1, 3, 2, 4]
velocity_max = 0.8
velocity_min = 0.1
Q = 30

def temp_parse_data(data):
    """Temporary function to parse a small part of the dataset for testing"""
    # Initialize arrays to store profits, weights, and assigned node numbers
    profits = []
    weights = []
    assigned_nodes = []

    # Split the data into lines
    lines = data.split('\n')

    # Iterate through each line starting from the second line (skipping header)
    for line in lines[2:]:
        # Split the line into values
        values = line.split()

        # Check if there are enough values in the line
        if len(values) == 4:
            # Extract profit, weight, and assigned node number and convert them to integers
            profit = int(values[1])
            weight = int(values[2])
            assigned_node = int(values[3])

            # Append values to the respective arrays
            profits.append(profit)
            weights.append(weight)
            assigned_nodes.append(assigned_node)

    # Return the arrays
    return profits, weights, assigned_nodes




def main():
    data ="""ITEMS SECTION	(INDEX, PROFIT, WEIGHT, ASSIGNED NODE NUMBER): 
1	101	1	2
2	202	2	3
3	404	4	4
4	202	2	5
5	996	896	6
6	1992	1792	7
7	3984	3584	8
8	467	367	9
9	934	734	10
10	1868	1468	11
11	790	690	12
12	790	690	13
13	713	613	14
14	1426	1226	15
15	2852	2452	16
16	974	874	17
17	974	874	18
18	222	122	19
19	444	244	20
20	888	488	21
21	666	366	22
22	586	486	23
23	1172	972	24
24	1172	972	25
25	923	823	26
26	923	823	27
27	563	463	28
28	1126	926	29
29	563	463	30
30	689	589	31
31	1378	1178	32
32	1378	1178	33
33	425	325	34
34	850	650	35
35	1700	1300	36
36	1275	975	37
37	1100	1000	38
38	2200	2000	39
39	4400	4000	40
40	876	776	41
41	1752	1552	42
42	2628	2328	43
43	223	123	44
44	456	356	45
45	405	305	46
46	810	610	47
47	1620	1220	48
48	405	305	49
49	147	47	50
50	294	94	51
51	588	188	52
52	745	645	53
53	1490	1290	54
54	2980	2580	55
55	1490	1290	56
56	239	139	57
57	347	247	58
58	694	494	59
59	1388	988	60
60	1041	741	61
61	311	211	62
62	622	422	63
63	1244	844	64
64	933	633	65
65	200	100	66
66	400	200	67
67	800	400	68
68	200	100	69
69	727	627	70
70	1454	1254	71
71	1454	1254	72
72	860	760	73
73	1720	1520	74
74	876	776	75
75	1752	1552	76
76	3504	3104	77
77	575	475	78
78	1150	950	79
79	2300	1900	80
80	1037	937	81
81	2074	1874	82
82	4148	3748	83
83	1037	937	84
84	201	101	85
85	402	202	86
86	804	404	87
87	402	202	88
88	381	281	89
89	762	562	90
90	1524	1124	91
91	762	562	92
92	851	751	93
93	1702	1502	94
94	3404	3004	95
95	1702	1502	96
96	630	530	97
97	1260	1060	98
98	2520	2120	99
99	340	240	100
100	680	480	101
101	680	480	102
102	348	248	103
103	696	496	104
104	1044	744	105
105	868	768	106
106	131	31	107
107	262	62	108
108	131	31	109
109	713	613	110
110	1426	1226	111
111	2852	2452	112
112	713	613	113
113	981	881	114
114	1962	1762	115
115	1962	1762	116
116	467	367	117
117	934	734	118
118	1868	1468	119
119	467	367	120
120	812	712	121
121	510	410	122
122	1020	820	123
123	2040	1640	124
124	510	410	125
125	257	157	126
126	514	314	127
127	1028	628	128
128	771	471	129
129	924	824	130
130	342	242	131
131	572	472	132
132	1144	944	133
133	1716	1416	134
134	822	722	135
135	1644	1444	136
136	3288	2888	137
137	875	775	138
138	875	775	139
139	471	371	140
140	942	742	141
141	1884	1484	142
142	437	337	143
143	874	674	144
144	437	337	145
145	985	885	146
146	1970	1770	147
147	3940	3540	148
148	1970	1770	149
149	304	204	150
150	608	408	151
151	1216	816	152
152	608	408	153
153	694	594	154
154	1388	1188	155
155	2776	2376	156
156	1388	1188	157
157	326	226	158
158	652	452	159
159	1304	904	160
160	326	226	161
161	652	452	162
162	1021	921	163
163	637	537	164
164	1274	1074	165
165	2548	2148	166
166	212	112	167
167	212	112	168
168	1059	959	169
169	2118	1918	170
170	3177	2877	171
171	492	392	172
172	492	392	173
173	809	709	174
174	1618	1418	175
175	3236	2836	176
176	1040	940	177
177	2080	1880	178
178	1043	943	179
179	2086	1886	180
180	4172	3772	181
181	179	79	182
182	179	79	183
183	1022	922	184
184	2044	1844	185
185	2044	1844	186
186	461	361	187
187	1047	947	188
188	2094	1894	189
189	1047	947	190
190	961	861	191
191	1922	1722	192
192	3844	3444	193
193	2883	2583	194
194	1037	937	195
195	2074	1874	196
196	4148	3748	197
197	3111	2811	198
198	854	754	199
199	1708	1508	200
200	2562	2262	201
201	972	872	202
202	736	636	203
203	736	636	204
204	559	459	205
205	1118	918	206
206	2236	1836	207
207	1677	1377	208
208	490	390	209
209	490	390	210
210	241	141	211
211	482	282	212
212	723	423	213
213	211	111	214
214	422	222	215
215	844	444	216
216	633	333	217
217	688	588	218
218	1376	1176	219
219	688	588	220
220	106	6	221
221	106	6	222
222	255	155	223
223	510	310	224
224	1020	620	225
225	765	465	226
226	823	723	227
227	1646	1446	228
228	3292	2892	229
229	1646	1446	230
230	823	723	231
231	1646	1446	232
232	3292	2892	233
233	2469	2169	234
234	767	667	235
235	1534	1334	236
236	1534	1334	237
237	929	829	238
238	1858	1658	239
239	3716	3316	240
240	929	829	241
241	587	487	242
242	1174	974	243
243	1174	974	244
244	690	590	245
245	1380	1180	246
246	2760	2360	247
247	1380	1180	248
248	470	370	249
249	940	740	250
250	1880	1480	251
251	923	823	252
252	1846	1646	253
253	3692	3292	254
254	923	823	255
255	273	173	256
256	546	346	257
257	156	56	258
258	1077	977	259
259	2154	1954	260
260	3231	2931	261
261	781	681	262
262	1562	1362	263
263	2343	2043	264
264	789	689	265
265	1578	1378	266
266	3156	2756	267
267	789	689	268
268	1033	933	269
269	2066	1866	270
270	3099	2799	271
271	909	809	272
272	1818	1618	273
273	687	587	274
274	1374	1174	275
275	786	686	276
276	1572	1372	277
277	786	686	278
278	566	466	279
279	456	356	280

    """
    capacity = 25936
    no_items = 279
    profits,weights,assigned_nodes = temp_parse_data(data)
    local_search(profits=profits,weights=weights,capacity=capacity,no_items=no_items)


def local_search(profits, weights, capacity,n=100000, discretion=0.1, annealing_prob=0, initial_solution_type='intuitive'):
    """
    NOTE: An assumption is made that the list of profits and weights correspond to thesame items. That is, profits[0] and weights[0] refer to the profits
    and weights for item 0

    NOTE: Our local search might work better with the ACO if we provide information about which cities we're visiting first. This
    allows us improve the probability of picking items towards the end of our route. Although this may be detrimental to the knapsack problem in seclusion,
    it might provide better pareto optimal solutions.

    Local search algorithm to be used to calculate the best combination of items to take in order to maximise the 
    weight of the bag without exceeding the capacity.

    Two heuristics are employed in selecting the initial solution:

    a.    A heuristic is used to choose items with the greatest profit/weight ration. This is because items that weigh less and
        have higher profits allow us to pick more items. This is implemented as a kind of tournament solution because even items with low profit to weight ratio are desirable.
        The logic is explained as follows:
        - The ratio of profits to weights is calculated for the items
        - The probability distribution is then calculated by dividing the array with the sum of the ratios
        * In order to use this as a probability of selecting an item then we need to scale it up
            ** We can do this by using a multiplier
            ** The multiplier has to be a value that will lead to us selecting the closest weight to the capacity of the knapsack
            ** This means that we need to have an approximate idea of how many items we need to pick from the knapsack
            ** We can get this by dividing the knapsack capacity by the average weight of the objects
            ** We want to start with a half filled knapsack so that we can consistently improve so we divide the multiplier by 2

    b.    A second heuristic is chosen to ensure that we have a nice selection of items and not just huge items being selected, this heuristic is called discretion.
        If the weight of the object is larger than the knapsack capacity * discretion, then don't pick it.
    

    Inputs:
    n: number of iterations to run
    profits: list of profits for the items
    weights: list of weights for the items
    capacity: capacity of knapsack
    discretion: the probability that controls whether or not we carry really heavy items from the onset
    initial_solution_type: the logic described above gives us an intuitively good initial solution, we can also initialize a random solution
    """
    w = np.array(weights)
    p = np.array(profits)
    ratio = np.array(p) / np.array(w)
    total_ratio = ratio.sum()
    prob_distribution = ratio/total_ratio
    multiplier = capacity / (w.mean())
    probabilities = prob_distribution * multiplier
    def initialize_solution():
        """ 
        This subfunction initializes a solution

        - Intuitive uses information about the ratio of profit/weight while random randomly picks items to be selected
        """
        solution = []
        if initial_solution_type == 'intuitive':
            for index,i in enumerate(probabilities):
                random_float = random.random()
                if i >= random_float:
                    if weights[index] < capacity * discretion:
                        solution.append(1)
                else:
                    solution.append(0)
        elif initial_solution_type == 'random':
            
            # define a threshold for the random items picked. The higher the threshold the higher the number of items picked
            threshold = 0.4
            solution_fitness = -math.inf
            # execute while the fitness of the solution is infinity. This ensures that we only consider valid solutions
            while solution_fitness == -math.inf:
                for i in range(len(weights)):
                    random_float = random.random()
                    if random_float > threshold:
                        solution.append(1)
                    else:
                        solution.append(0)
                solution_fitness = fitness(solution)[0]        
        else:
            raise TypeError(f"Invalid argument: {initial_solution_type}")
        return solution
    
    def generate_neighbor(solution):
        # flip the bit at a random index
        index = random.randint(0,len(solution)-1)
        solution[index] = 1 if not solution[index] else 0
        new_solution = solution
        # if the new solution is infeasible, fix it and flip a different bit
        while fitness(new_solution)[0] == -math.inf:
            solution[index] = 0
            index = random.randint(0,len(solution)-1)
            new_solution[index] = 1
        # return the neighbor
        return new_solution
    
    def fitness(solution):
        # Return the profit and weight of a solution. Return neg infinity if the solution is infeasible(weight is too high)
        total_profit = 0
        total_weight = 0
        for weight,profit,picked in zip(weights,profits,solution):
            if picked:
                total_profit += profit
                total_weight += weight
        if total_weight > capacity:
            return [-math.inf,total_weight]
        return [total_profit,total_weight]

    solution = initialize_solution()
    for i in range(n):
        new_solution = generate_neighbor(solution)
        fitness_new = fitness(new_solution)
        fitness_curr = fitness(solution)
        if fitness_new[0] > fitness_curr[0] and fitness_new[1] != -math.inf:
            solution = new_solution
    print(f"Total weight of knapsack: {fitness(solution)} / {capacity}")
    return solution


def initial_data(filepath:str) -> None:
    """
    Takes as input a filename, reads the data from the file and updates the global variables
        CITY_DATA = []
        KNAPSACK_CAPACITY = 0
        ITEMS_DATA = []
        NUMBER_OF_ITEMS = 0
        MIN_SPEED = 0.0
        MAX_SPEED = 0.0
    with the values from the file

    input = filepath
    output = None
    """
    with open(filepath) as f:
        pass

def fitness(c_path, distance, p_flag, c_flag, c_weight, c_profit) -> (float,float,float):
    """
    Fitness function takes a solution and returns its fitness as a tuple(time,profit)

    input = 
    """
    total_weight = 0
    total_time = 0
    total_profit = 0
    for i in range(len(c_path) - 1):
        city_start = c_path[i] - 1
        city_end = c_path[i + 1] - 1
        speed = update_speed(total_weight)
        if p_flag[city_end - 1]:
            flag = c_flag[city_end - 1]
            for j in range(len(flag)):
                if flag[j]:
                    total_weight += c_weight[city_end - 1][j]
                    total_profit += c_profit[city_end - 1][j]
        # if the maximum capacity constraint is reached, Adding a penalty mechanism
        if total_weight > Q:
            total_time = float('inf')
            total_profit = -float('inf')
            break
        total_time += distance[city_start][city_end] / speed
    if total_weight <= Q:
        speed = update_speed(total_weight)
        total_time += distance[city_start][city_end] / speed
    # The fitness value can be calculated based on the set time and profit weights.
    # We can add two parameters
    # fitness_value = alpha * total_time + beta * total_profit
    # fitness_value = round(fitness_value, 3)
    objects = [round(total_time, 3), total_profit]
    # return total_weight, fitness_value, objects
    return total_time, total_profit, objects

def update_solutions(new_solution):
    """
    If new_solution is better than any solution in LEAST_SOLUTIONS then replace the worst one.
    This is meant to favour the best pareto optimal solution.

    input: new_solution
    output: None
    """
    pass


def update_speed(bag_weight):
    return velocity_max - (bag_weight / Q) * (velocity_max - velocity_min)

def calculate_time():
    pass

def get_distance(cityA:int,cityB:int) -> int:
    """
    Given two cities, return their distance from the CITY_DATA
    """
    return math.sqrt((cityB[0] - cityA[0]) ** 2 + (cityB[1] - cityA[1]) ** 2)

def get_item_value(city_index,item_index):
    """
    Given an item and a city, return the value of the item using ITEM_DATA
    """

def get_item_weight(city_index,item_index):
    pass


def is_valid_solution(solution):
    """
    Takes as input the solution and r
    """
    pass


def algorithm():
    pass



if __name__ == "__main__":
    main()