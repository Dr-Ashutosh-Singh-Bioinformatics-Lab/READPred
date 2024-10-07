# READPred: A Tool for Identification of Rectum Adenocarcinoma using Machine Learning.
Rectum adenocarcinoma is a type of cancer that originates in the glandular cells of the rectum, part of the lower gastrointestinal tract. Identifying biomarkers is crucial for early detection and diagnosis, enabling personalized treatment plans and improving prognosis, ultimately enhancing patient outcomes through timely intervention and management strategies. Biomarkers are pivotal in this regard, providing noninvasive means for early detection, facilitating prompt treatment initiation, and potentially boosting survival rates. Hence, the recognition and validation of biomarkers are of primary importance in effectively addressing rectum adenocarcinoma.


## Introduction

READPred is an innovative solution for identifying rectum adenocarcinoma through transcriptomic profiling. By leveraging advanced machine learning algorithms, this cutting-edge technology analyzes tissue biomarkers to deliver highly accurate prognoses for rectal cancer.

Furthermore, the integration of machine learning enables continuous refinement of the predictive model’s accuracy as more data is gathered, enhancing its reliability and effectiveness over time. READPred represents a significant breakthrough in the early detection of rectum adenocarcinoma, potentially leading to earlier interventions and improved patient outcomes.

To further strengthen our approach, we selected 38 features using a range of Feature Selection Methods. These include the Fast Correlation-Based Filter Method (FCBF), Spike and Slab ("spikeslab"), Univariate statistical tests (F-test), and wrapper methods like Boruta and Recursive Feature Elimination (RFE). Additionally, we employed embedded methods such as XGBoost, SVC linear with the SelectFromModel class from scikit-learn, Random Forest, Extra Trees with Feature Importance, and LASSO (a regularization-based embedded method). By combining Filter, Wrapper, and Embedded feature selection techniques, we used an ensemble approach to identify features present in at least five methods. These 38 features show potential as biomarkers for classifying and predicting normal versus cancerous patients.


Installation and Usage:

You can install the package using the following command:


    git clone https://github.com/GITractCancer/READPred.git
    cd READPred



### Predict using READPred

    import pandas as pd
    from READPred import predict

    df = pd.read_csv("path/to/your/data.csv")

    predict(df, model_type='svc')

    
Specify the model type you want to use Models


## Models

The following classifiers are supported:

    svc
    rf
    ab
    xgb
    dt
    et
    lr
    gnb
    knn
    mlp
