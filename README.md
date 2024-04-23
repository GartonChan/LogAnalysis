## logAnalyser
This is a simple tool for analysing the log of benchmarks (by extracting the useful data from log files and calculating the statistics)
#### Directory Structure
- log/
    - eapp/
        - directories for the log of each benchmark 
    - host/
        - directories for the log of each benchmark 
- Analyser.py
- demo.py
- utils.py: some helper functions
- README.md

#### Demo Result
```
--- Statistics: tiny
mean:   6.632273913043478
var:    2.1286275992439093e-05
min:    6.6235
max:    6.6405
----------------------------------
--- Statistics: darknet19
mean:   52.606165217391315
var:    0.008806573572778902
min:    52.4617
max:    52.7618
----------------------------------
--- Statistics: darknet53
mean:   133.44871304347825
var:    0.03472976200378124
min:    133.2467
max:    134.0372
----------------------------------
--- Statistics: alexnet
mean:   16.55303043478261
var:    0.001556198638941377
min:    16.481
max:    16.6141
----------------------------------
--- Statistics: yolov3-tiny
mean:   45.434791304347826
var:    0.0024199434026464283
min:    45.3425
max:    45.5081
----------------------------------
--- Statistics: yolov3
mean:   1279.6406315789473
var:    130.23319812742398
min:    1231.231
max:    1283.054
----------------------------------
--- Statistics: tiny
mean:   6.8397347916666655
var:    0.004026617869831603
min:    6.767599
max:    6.97776
----------------------------------
--- Statistics: darknet19
mean:   53.031771416666665
var:    0.0005827829692430408
min:    52.993191
max:    53.098701
----------------------------------
--- Statistics: darknet53
mean:   134.67509326086955
var:    0.020417348435583058
min:    134.571518
max:    135.264481
----------------------------------
--- Statistics: alexnet
mean:   16.660464695652177
var:    3.347640290737231e-05
min:    16.651457
max:    16.675436
----------------------------------
--- Statistics: yolov3-tiny
mean:   45.8631224347826
var:    0.00026208745189791523
min:    45.840922
max:    45.89086
----------------------------------
--- Statistics: yolov3
mean:   1297.78109075
var:    0.011219028497174741
min:    1297.654315
max:    1297.920383
----------------------------------
```