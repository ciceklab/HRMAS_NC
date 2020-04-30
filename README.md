# Glioma Classification from HRMAS NMR Spectrum

[Machine Learning Assisted Intraoperative Assessment of Brain Tumor Margins Using HRMAS NMR Spectroscopy](https://www.medrxiv.org/content/10.1101/2020.02.24.20026955v1) <br/>
Doruk Cakmakci, Emin Onur Karakaslar, Elisa Ruhland, Marie-Pierre Chenard, Francois Proust, Martial Piotto, Izzie Jacques Namer and A. Ercument Cicek

## Scripts
[Create Dataset](./create_dataset.py): This script is used to create the experiment setup presented in the paper. Samples are grouped according to their patient ids. Patients are randomly shuffled. Folds are generated by stratified and grouped k-fold cross validation approach. Finally, spectrum data is preprocessed as discussed in the paper.

[SHAP Value Plotting](./plot_shap.py): This script contains function used for generating SHAP Value Plots given in Figure 3 in the paper. 

### Benign vs. Malignant Glioma Classification Models
[Random Forest](./benign_aggressive/rf.py), [CNN](./benign_aggressive/cnn.py) , [Fully-connected NN](./benign_aggressive/nn.py), [SVM](./benign_aggressive/svm.py) , [PLSDA](./benign_aggressive/plsda.py)
### Control vs. Glioma Classification Models
[Random Forest](./control_tumor/rf.py), [CNN](./control_tumor/cnn.py), [Fully-connected NN](./control_tumor/nn.py), [SVM](./control_tumor/svm.py), [PLSDA](./control_tumor/plsda.py)

## Dependencies 
- PyTorch
- scikit-learn
- pandas
- numpy
- [PyNMR](https://github.com/bennomeier/pyNMR)
- [shap](https://github.com/slundberg/shap)

## Getting Started
 - Create **/data** and **/lib** folders.
 - Download and Extract the dataset as a subdirectory of **/data** folder
 - Download and save Supplementary Table 1 to **/data** folder. Rename the file to _supplement.xls_
 - Install dependencies. If an Ubuntu machine with GPU is used, dependencies may be installed by creating a conda environment using _ubuntu\_environment.yml_ file and installing _shap_  dependency using conda.
 - Clone [PyNMR library](https://github.com/bennomeier/pyNMR) to **/lib**
 - Generate dataset using **create_dataset.py** by uncommenting corresponding dataset option (Lines 222-225)
 - Execute any model script (For random forest, SHAP plots will be saved to the same directory)
