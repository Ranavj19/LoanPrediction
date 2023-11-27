import pandas as pd 
import numpy as np 
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, classification_report
from sklearn.impute import SimpleImputer


class LoanModel : 
    def model(self , x):
        data = pd.read_csv(r"train.xls")
        training_data = data.drop(columns=['Loan_ID'])
        training_data_encoded = pd.get_dummies(training_data,drop_first=True)

        ########## Split Features and Target Varible ############
        X = training_data_encoded.drop(columns='Loan_Status_Y')
        y = training_data_encoded['Loan_Status_Y']
        X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2,random_state =42)
        imp = SimpleImputer(strategy='mean')
        imp_train = imp.fit(X_train)
        X_train = imp_train.transform(X_train)
        X_test_imp = imp_train.transform(X_test)
        tree_clf = DecisionTreeClassifier(max_depth=3,min_samples_leaf = 35)
        tree_clf.fit(X_train,y_train)
        y_pred = tree_clf.predict(X_test_imp)

        ## for the test cases
        res = tree_clf.predict(x)
        return res
    
    

# obj = LoanModel()
# new_case = np.array([[0],[0],[350],[180],[1],[1],[1],[1],[0],[0],[0],[1],[0],[1]])
# new = new_case.reshape(1,-1)
# result = obj.model(new)
# print(result)

    
        