Iris Dataset
The Iris dataset is a classic dataset in machine learning and statistics, widely used for classification tasks. It contains 150 samples of iris flowers, each described by four features:
•	Sepal Length
•	Sepal Width
•	Petal Length
•	Petal Width
The dataset classifies each sample into one of three species:
1.	Iris Setosa
2.	Iris Versicolor
3.	Iris Virginica
This dataset is well-suited for beginner-level projects to practice supervised learning algorithms, especially classification. In this project, we use the dataset to predict the species of an iris flower based on its features.

Steps to Run the Project
Follow the steps below to run the Iris Flower Prediction project on your local machine:
1.	Create a Folder:
o	On your desktop, create a new folder where the project files will be stored.
2.	Clone the Repository:
o	Open the command prompt or terminal in the folder you created.
o	Clone the GitHub repository by running the command:
bash
Copy code
git clone <repository-url>
Replace <repository-url> with the URL of this GitHub repository.
3.	Open the Project in VS Code:
o	After cloning, navigate to the project folder and open it in Visual Studio Code using the command:
bash
Copy code
code .
4.	Install Dependencies:
o	Ensure Python is installed on your system.
o	Install the required Python libraries by running:
bash
Copy code
pip install -r requirements.txt
5.	Run the Application:
o	Start the Flask application by executing:
bash
Copy code
python app.py
6.	Access the Website:
o	Open a web browser and navigate to http://127.0.0.1:8000 or http://localhost:8000.
7.	Use the Application:
o	Enter the values for sepal length, sepal width, petal length, and petal width in the form.
o	Click on Predict to get the type of iris flower.
🎉 Congratulations! You have successfully run the Iris Flower Prediction website using Flask.


The ranges of sepal length, sepal width, petal length, and petal width for each flower species in the Iris dataset can be summarized in a table. These values are derived from the dataset:
Flower Species	Sepal Length (cm)	Sepal Width (cm)	Petal Length (cm)	Petal Width (cm)
Iris Setosa	4.3 - 5.8	2.3 - 4.4	1.0 - 1.9	0.1 - 0.6
Iris Versicolor	4.9 - 7.0	2.0 - 3.4	3.0 - 5.1	1.0 - 1.8
Iris Virginica	4.9 - 7.9	2.2 - 3.8	4.5 - 6.9	1.4 - 2.5
Explanation:
•	Sepal Length (cm): The length of the sepal in centimeters.
•	Sepal Width (cm): The width of the sepal in centimeters.
•	Petal Length (cm): The length of the petal in centimeters.
•	Petal Width (cm): The width of the petal in centimeters.
•	Species:
o	Iris Setosa is characterized by smaller and narrower petals and sepals.
o	Iris Versicolor has intermediate dimensions.
o	Iris Virginica tends to have larger sepals and petals.
This table can be useful for quickly understanding the range of measurements for each flower type.
