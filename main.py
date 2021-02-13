import calc as clc


# ZF13KVE-TFD EV
DATA_1_Q = [[-40.0, 30.0, 3.45], [-40.0, 40.0, 3.30], [-40.0, 50.0, 2.78],
            [-35.0, 30.0, 4.30], [-35.0, 40.0, 4.10], [-35.0, 50.0, 3.75],
            [-30.0, 30.0, 5.25], [-30.0, 40.0, 5.05], [-30.0, 50.0, 4.65],
            [-25.0, 30.0, 6.35], [-25.0, 40.0, 6.10], [-25.0, 50.0, 5.70],
            [-20.0, 30.0, 7.55], [-20.0, 40.0, 7.30], [-20.0, 50.0, 6.90],
            [-15.0, 30.0, 8.95], [-15.0, 40.0, 8.70], [-15.0, 50.0, 8.30],
            [-10.0, 30.0, 10.50], [-10.0, 40.0, 10.30], [-10.0, 50.0, 9.90],
            [-5.0, 30.0, 12.25], [-5.0, 40.0, 12.05], [-5.0, 50.0, 11.7],
            [0.0, 30.0, 14.25], [0.0, 40.0, 14.10], [0.0, 50.0, 13.75],
            [5.0, 30.0, 16.50], [5.0, 40.0, 16.40], [5.0, 50.0, 16.10],
            [7.0, 30.0, 17.50], [7.0, 40.0, 17.40], [7.0, 50.0, 17.10]]


# ZF09K4E-TFD
DATA_2_Q = [[-45.0, 30.0, 1.25], [-45.0, 40.0, 1.13], [-45.0, 50.0, 1.05],
            [-40.0, 30.0, 1.60], [-40.0, 40.0, 1.46], [-40.0, 50.0, 1.35],
            [-35.0, 30.0, 2.01], [-35.0, 40.0, 1.85], [-35.0, 50.0, 1.70],
            [-30.0, 30.0, 2.51], [-30.0, 40.0, 2.30], [-30.0, 50.0, 2.11],
            [-25.0, 30.0, 3.10], [-25.0, 40.0, 2.84], [-25.0, 50.0, 2.59],
            [-20.0, 30.0, 3.80], [-20.0, 40.0, 3.50], [-20.0, 50.0, 3.15],
            [-15.0, 30.0, 4.60], [-15.0, 40.0, 4.20], [-15.0, 50.0, 3.85],
            [-10.0, 30.0, 5.50], [-10.0, 40.0, 5.05], [-10.0, 50.0, 4.60],
            [-5.0, 30.0, 6.60], [-5.0, 40.0, 6.05], [-5.0, 50.0, 5.50],
            [0.0, 30.0, 7.80], [0.0, 40.0, 7.20], [0.0, 50.0, 6.50],
            [5.0, 30.0, 9.15], [5.0, 40.0, 8.45], [5.0, 50.0, 7.70],
            [7.0, 30.0, 9.75], [7.0, 40.0, 9.00], [7.0, 50.0, 8.20]]


clc.run([DATA_1_Q, DATA_2_Q], ["ZF13KVE-TFD EV", "ZF09K4E-TFD"])
