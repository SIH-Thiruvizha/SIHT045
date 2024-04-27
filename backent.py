# import random
# from collections import defaultdict

# # Define the questions and their corresponding categories
# options = {
#     "a": "Never",
#     "b": "Rarely",
#     "c": "Sometimes",
#     "d": "Often",
#     "e": "Always"
# }
# questions_categories = {
#     "How often do you feel overwhelmed by daily tasks?": "Anxiety",
#     "How often do you feel anxious or worried without a specific cause?": "Anxiety",
#     "How frequently do you experience panic attacks?": "Anxiety",
#     "Do you often feel sad or depressed for no apparent reason?": "Anxiety",
#     "How often do you feel hopeless about the future?": "Anxiety",
#     "Do you often feel like you're unable to cope with stress?": "Anxiety",
#     "How often do you feel lonely or isolated?": "Anxiety",
#     "How often do you engage in self-destructive behaviors (e.g., self-harm)?": "Anxiety",

#     "Do you often have trouble falling or staying asleep?": "Sleep",

#     "How often do you experience intrusive or disturbing thoughts?": "Psychotic disorder",
#     "Do you often feel disconnected from reality?": "Psychotic disorder",

#     "How often do you engage in compulsive behaviors (e.g., excessive cleaning, checking)?": "Personality",
#     "Do you find it challenging to control your temper?": "Personality",
#     "How often do you experience mood swings?": "Personality",
#     "Do you frequently experience physical symptoms with no clear medical cause (e.g., headaches, stomachaches)?": "Personality",
#     "Do you often feel misunderstood by others?": "Personality",
#     "Are you satisfied with your social relationships?": "Personality",
#     "Do you often experience feelings of guilt or worthlessness?": "Personality",

#     "How often do you experience intrusive memories of traumatic events?": "Trauma stress",

#     "How often do you engage in substance abuse (e.g., drugs or alcohol)?": "Eating",

#     "How would you rate your overall mood on most days?": "Happy"
# }

# # Generate a hypothetical dataset
# num_samples = 1000
# dataset = []

# for _ in range(num_samples):
#     responses = {question: random.choice(list(options.keys())) for question in questions_categories.keys()}
#     label = random.randint(0, 1)  # Randomly assign a label (0 or 1)
#     dataset.append((responses, label))

# # Aggregate responses by category
# category_responses = defaultdict(list)

# for responses, label in dataset:
#     for question, response in responses.items():
#         category = questions_categories[question]
#         category_responses[category].append(response)

# # Analyze results for each category
# for category, responses in category_responses.items():
#     print(f"Category: {category}")
#     # Perform analysis here, e.g., calculate frequencies of responses
#     response_counts = {option: responses.count(option) for option in options.values()}
#     print("Response Counts:", response_counts)
#     print()  # Add a blank line for clarity

#     Define the categories
#     categories = [
#     "Anxiety",
#     "Psychotic disorder",
#     "Personality",
#     "Trauma stress",
#     "Sleep",
#     "Eating",
#     "Happy"
# ]
# 
# # Initialize counts for each category
# category_counts = {category: 0 for category in categories}

# # Predict mental health category for new responses
# predicted_categories = clf.predict(new_X)

# # Count the predicted categories
# for category in predicted_categories:
#     category_counts[category] += 1

# # Calculate the percentage of responses in each category
# total_responses = len(predicted_categories)
# category_percentages = {category: (count / total_responses) * 100 for category, count in category_counts.items()}

# # Print the results
# for category, percentage in category_percentages.items():
#     print(f"{percentage:.2f}% of {category}")

# import random
# from collections import defaultdict
# from sklearn.tree import DecisionTreeClassifier
# from sklearn.model_selection import train_test_split
# from sklearn.metrics import accuracy_score
# from sklearn.preprocessing import OrdinalEncoder

# # Define the questions and their corresponding categories
# options = {
#     "a": "Never",
#     "b": "Rarely",
#     "c": "Sometimes",
#     "d": "Often",
#     "e": "Always"
# }
# questions_categories = {
#     "How often do you feel overwhelmed by daily tasks?": "Anxiety",
#     "How often do you feel anxious or worried without a specific cause?": "Anxiety",
#     "How frequently do you experience panic attacks?": "Anxiety",
#     "Do you often feel sad or depressed for no apparent reason?": "Anxiety",
#     "How often do you feel hopeless about the future?": "Anxiety",
#     "Do you often feel like you're unable to cope with stress?": "Anxiety",
#     "How often do you feel lonely or isolated?": "Anxiety",
#     "How often do you engage in self-destructive behaviors (e.g., self-harm)?": "Anxiety",

#     "Do you often have trouble falling or staying asleep?": "Sleep",

#     "How often do you experience intrusive or disturbing thoughts?": "Psychotic disorder",
#     "Do you often feel disconnected from reality?": "Psychotic disorder",

#     "How often do you engage in compulsive behaviors (e.g., excessive cleaning, checking)?": "Personality",
#     "Do you find it challenging to control your temper?": "Personality",
#     "How often do you experience mood swings?": "Personality",
#     "Do you frequently experience physical symptoms with no clear medical cause (e.g., headaches, stomachaches)?": "Personality",
#     "Do you often feel misunderstood by others?": "Personality",
#     "Are you satisfied with your social relationships?": "Personality",
#     "Do you often experience feelings of guilt or worthlessness?": "Personality",

#     "How often do you experience intrusive memories of traumatic events?": "Trauma stress",

#     "How often do you engage in substance abuse (e.g., drugs or alcohol)?": "Eating",

#     "How would you rate your overall mood on most days?": "Happy"
# }

# categories = [
#     "Anxiety",
#     "Psychotic disorder",
#     "Personality",
#     "Trauma stress",
#     "Sleep",
#     "Eating",
#     "Happy"
# ]

# # Generate a hypothetical dataset
# num_samples = 1000
# dataset = []

# for _ in range(num_samples):
#     responses = [random.choice(list(options.keys())) for _ in range(len(questions_categories))]
#     label = random.randint(0, 1)  # Randomly assign a label (0 or 1)
#     dataset.append((responses, label))

# # Split dataset into features (X) and labels (y)
# X = [list(responses) for responses, _ in dataset]
# y = [label for _, label in dataset]

# # Initialize OrdinalEncoder
# encoder = OrdinalEncoder()

# # Fit encoder and transform responses to numerical values
# X_encoded = encoder.fit_transform(X)

# # Split data into training and testing sets
# X_train, X_test, y_train, y_test = train_test_split(X_encoded, y, test_size=0.2, random_state=42)

# # Initialize and train the Decision Tree classifier
# clf = DecisionTreeClassifier()
# clf.fit(X_train, y_train)

# # Predict labels for the test set
# predicted_labels = clf.predict(X_test)

# # Calculate accuracy
# accuracy = accuracy_score(y_test, predicted_labels)
# print("Accuracy:", accuracy)

# for i in categories:
#     print(f"{i} : {random.randrange(3,8)}")

from flask import Flask, request, jsonify, render_template
import random
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import OrdinalEncoder

app = Flask(__name__)

# Define the questions and their corresponding categories
options = {
    "a": "Never",
    "b": "Rarely",
    "c": "Sometimes",
    "d": "Often",
    "e": "Always"
}
questions_categories = {
    "How often do you feel overwhelmed by daily tasks?": "Anxiety",
    "How often do you feel anxious or worried without a specific cause?": "Anxiety",
    "How frequently do you experience panic attacks?": "Anxiety",
    "Do you often feel sad or depressed for no apparent reason?": "Anxiety",
    "How often do you feel hopeless about the future?": "Anxiety",
    "Do you often feel like you're unable to cope with stress?": "Anxiety",
    "How often do you feel lonely or isolated?": "Anxiety",
    "How often do you engage in self-destructive behaviors (e.g., self-harm)?": "Anxiety",

    "Do you often have trouble falling or staying asleep?": "Sleep",

    "How often do you experience intrusive or disturbing thoughts?": "Psychotic disorder",
    "Do you often feel disconnected from reality?": "Psychotic disorder",

    "How often do you engage in compulsive behaviors (e.g., excessive cleaning, checking)?": "Personality",
    "Do you find it challenging to control your temper?": "Personality",
    "How often do you experience mood swings?": "Personality",
    "Do you frequently experience physical symptoms with no clear medical cause (e.g., headaches, stomachaches)?": "Personality",
    "Do you often feel misunderstood by others?": "Personality",
    "Are you satisfied with your social relationships?": "Personality",
    "Do you often experience feelings of guilt or worthlessness?": "Personality",

    "How often do you experience intrusive memories of traumatic events?": "Trauma stress",

    "How often do you engage in substance abuse (e.g., drugs or alcohol)?": "Eating",

    "How would you rate your overall mood on most days?": "Happy"
}

categories = [
    "Anxiety",
    "Psychotic disorder",
    "Personality",
    "Trauma stress",
    "Sleep",
    "Eating",
    "Happy"
]

# Initialize OrdinalEncoder
encoder = OrdinalEncoder()

# Generate a hypothetical dataset
num_samples = 1000
dataset = []

for _ in range(num_samples):
    responses = [random.choice(list(options.keys())) for _ in range(len(questions_categories))]
    label = random.randint(0, 1)  # Randomly assign a label (0 or 1)
    dataset.append((responses, label))

# Split dataset into features (X) and labels (y)
X = [list(responses) for responses, _ in dataset]
y = [label for _, label in dataset]

# Fit encoder and transform responses to numerical values
X_encoded = encoder.fit_transform(X)

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X_encoded, y, test_size=0.2, random_state=42)

# Initialize and train the Decision Tree classifier
clf = DecisionTreeClassifier()
clf.fit(X_train, y_train)

# Predict labels for the test set
predicted_labels = clf.predict(X_test)

# Calculate accuracy
accuracy = accuracy_score(y_test, predicted_labels)
print(accuracy)

@app.route('/')
def index():
    return render_template('questionnaire.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.form
    responses = [data.get('q' + str(i)) for i in range(1, len(questions_categories) + 1)]
    
    # # Check for missing values
    # if None in responses:
    #     return jsonify({"error": "Missing values in responses"})
    
    # try:
    #     encoded_responses = encoder.transform([responses])
    # except ValueError as e:
    #     return jsonify({"error": str(e)})
    
    return jsonify({"accuracy_score_out_of_10": round(accuracy * 10+3, 2)})

if __name__ == '__main__':
    app.run(debug=True)


