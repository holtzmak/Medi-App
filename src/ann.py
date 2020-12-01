import pandas as pd
from sklearn import preprocessing 
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPClassifier
import ann_train_test_split
from sklearn.metrics import plot_confusion_matrix
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.svm import SVC


class ArtificialNeuralNetwork:
    def data_sweep(self):
        link = "data.csv"
        #Assigning cloumn names to the dataset
        names =['itching', 'skin_rash', 'chills', 'vomiting', 'fatigue','Class' ]
        #reading datas to panda dataframe 
        data = pd.read_csv(link, names=names)
        #assign data from first five columns to X variable 
        self.x=data.iloc[:,0:5]
        #assign data from first fifth columns to y variable 
        y=data.select_dtypes(include=[object])
        le= preprocessing.LabelEncoder()
        self.y=y.apply(le.fit_transform)
        return self.x,self.y

    def ann_train_test_split(self):
        self.data_sweep()
        sweep_x= self.x
        sweep_y=self.y
        X_train, X_test,y_train, y_test =train_test_split(sweep_x,sweep_y,test_size=0.20)
        #Feature Scaling for uniform evaluation 
        scaler= StandardScaler()
        scaler.fit(X_train)
        X_train=scaler.transform(X_train)
        X_test=scaler.transform(X_test)

    def ann_training(self):
        mlp=MLPClassifier(hidden_layer_sizes=(5,5,5), max_iter=1000)
        mlp.fit(ann_train_test_split.X_train,ann_train_test_split.y_train)
        predictions = mlp.predict(ann_train_test_split.X_test)
        clf = SVC(random_state=0)
        clf.fit(ann_train_test_split.X_train, ann_train_test_split.y_train)
        plot_confusion_matrix(clf, ann_train_test_split.X_test, ann_train_test_split.y_test)
        print("The ANN reported:")
        print(confusion_matrix(ann_train_test_split.y_test,predictions))
        print(classification_report(ann_train_test_split.y_test,predictions))