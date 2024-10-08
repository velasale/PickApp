# PickApp
Package to perform apple picking experiments with a UR5 robotic manipulator and a 3-finger underactuated gripper. 

## Contact
Alejandro Velasquez  
velasale@oregonstate.edu  
Robotics PhD Student

## Description
This package takes datasets of apple picks performed with a robotic manipulator UR5e and a robotic gripper as end effector.
The picks are performed in a real tree and in an apple proxy that emulates the physics of the apple tree.
Hence, this package is useful for the user to:
- [x] Post-process data in a suitable form for Machine Learning classification.
- [x] Compare time-series plots from real and proxy picks.
- [x] Obtain statistics about the experiments, such as the distribution of cartesian and angular noise.
- [x] Do basic machine learning to check if - with the given data - it is possible to train a classifier and predict the outcome of the pick (e.g. successful, failed).

For brief usage instructions, type:

```html
python pickapp_compare.py --help
```
```
python pickapp_learning.py --help
```
```
python pickapp_stats.py --help
```
```
python pickapp_data.py --help
```


## Examples
### module: pickapp_main.py
Note: Before running rosserial, make sure that the USB device is connected before starting the docker container
```
rosrun rosserial_python serial_node.py
```

```
rosrun PickApp pickapp_main.py
```




### module: pickapp_compare.py
The following example analyzes *variable* 'Force_z', among the 'failed' picks *case*, and does the Dynamic Time Warping (DTW) analysis during the 'pick' *phase*.
```
python pickapp_compare.py --variable force_z --case failed --phase pick --specific_pick 64-10
```
It outputs a time-series plot with the closest real and proxy picks.
I also outputs a time-series plot comparing the proxy pick 64-10 with the real pick 64.
It also outputs a .csv file with a list of the real and proxy picks that are comparable. Comparable picks are the ones where the pose of the robot with respect to the apple is the same.
These files are stored in the sub-folder **results**.

![Image](https://github.com/velasale/PickApp/blob/main/results/%20force_z__during__pick.png)


### module: pickapp_learning.py
The following example runs a Random Forest Classifier (RFC), with 10 *experiments* to account for the classifier's stochasticity, with a *depth* of 5 branches, and utilizes 5 *features*.
```
python pickapp_learning.py --experiments 10 --depth 5 --feature 5 --classifier rfc 
```
It outputs a boxplot with the classifier's accuracies during the experiments.
The boxplot gets stored in a .pdf file, along with a .txt file with the confusion matrix of the best accuracy.
These files are stored in the sub-folder **results**.

![Image](https://github.com/velasale/PickApp/blob/main/results/ML_RFC%20accuracy.png)

### module: pickapp_stats.py
In the following example, the statistic analysis is run for the dataset *3_proxy_winter22_x1*.
```html
python pickapp_stats.py --dataset 3_proxy_winter22_x1
```
It outputs .pdfs with box-plots of the angular and cartesian noise.
It also outputs a .txt file with Mean, SD and percentiles of each noise.
These files are stored in the sub-folder **results**.

```html
x_noises
Mean: -0.012SD: 0.014Percentiles: [-0.02  -0.01   0.003]
y_noises
Mean: -0.005SD: 0.01Percentiles: [-0.015 -0.007  0.   ]
z_noises
Mean: -0.012SD: 0.006Percentiles: [-0.015 -0.01  -0.005]
roll_noises
Mean: -4.846SD: 12.74Percentiles: [-10.  -5.   5.]
pitch_noises
Mean: -4.382SD: 12.627Percentiles: [-10.   0.   5.]
yaw_noises
Mean: 0.0SD: 0.0Percentiles: [0. 0. 0.]
```


## Installation

### Dependencies
I recommend installing the following packages:
- [x] System related: os, sys
- [x] User Interface related: tqdm, argparse
- [x] Data related: csv, pandas, collections, ast
- [x] Plots related: matplotlib, seaborn
- [x] Math/Stat related: numpy, scipy, dtw
- [x] Machine Learning related: sklearn

### Data
Download the data subfolder, which includes all the features, metadata, and data from real and proxy domains picks

### Choice 1: Install from PyPI
```
pip install pickApp
```

### Choice 2: Download
Download the repo, and run the following code
```html
python setup.py install
```


## Tips
Tips to write better functions  
https://pybit.es/articles/writing-better-functions/

Git cheat-sheet  
https://education.github.com/git-cheat-sheet-education.pdf

MarkDown cheat-sheet  
https://www.markdownguide.org/cheat-sheet/

Packaging Python Projects  
https://packaging.python.org/en/latest/tutorials/packaging-projects/