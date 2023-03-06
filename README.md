Overwiew.
Customer: public speakers, civil servants, comedians, etc.
Goal: Customers want a speech emotion recognition model that is accurate and reliable.
Pains: noise problems, fuzziness of data, lack of tagging data.
Gains: will help to find the right emotion for the speech.

Value proposition.
Product: a service on the right emotions.
Alleviates: will help pick up the emotion.
Advantages: clients do not have to think about emotions during the performance.

Objectives.
Allow clients to add their own prescribed texts.
[OUR FOCUS] Getting the emotion right.
Collect qualitative data quantitatively. 
Preprocess and classify them.
Get good points at testing.
Give to people for using.


Solution.
The solution will consist of a speech emotion
recognition model that is trained using a large
dataset of speech samples and emotional labels.
The model will be integrated into an easy-to-use
web-based interface that will allow customers to
input speech and receive emotional information in
real-time.The solution will be designed to be
scalable and able to handle a large number of
customers.

Core features:

ML service that will predict the correct categories for inbound content. [OUR FOCUS.]
User feedback process for incorrectly categorised content.

Integrations:
Classified content will be sent to the UI service for display.
textual feedback from users will be sent to development.

Alternatives:
Allow users to add content manually (bottleneck).

Constraints:
Maintain low latency (>100ms) when classifying incoming content. [Latency].

Feasibility.
We have a data set that we will use.

Engineering.
We have developed our own approach to creating our product.

Data.
Training:
access to raw data for training.
was any sampling used to create this dataset?
no data leakage?

Production:
access to timely batches of ML content from sources.
how can we trust that this stream contains only data that is consistent with what we have seen in the past?

Labeling.
Labelling: labelling using machine learning categories.

Features: textual characteristics.

Labels: reflect the categories of content we currently display on our platform.

Evaluation.
Themodelwillbeevaluatedusingbothoffline andonlineevaluationcriteria.
Theoffline evaluation will be performed on a test set of
speech samples, and the online evaluation will be
performed by allowing customers to input speech
and receive emotional information in real-time.

Modeling. 
Use some model from https://paperswithcode.com/task/speech-emotion-recognition.

Feedback. 
The system will collect feedback from customers
to use for iteration. This feedback will be used to
improve the model and ensure that it is meeting
the needs of customers. For example it can be
Google Forms.

Team. 
The team required for this project will include
individual swith expertise in speech processing,
machine learning, and web development.
Product: Product managers, Executives

System design:
Data collectors: Collect the necessary data and label it. 
Machine learner: Develops the ML model.
Designer: Designs UX/UI for the application.
Programmer: Develops the application.
Testers: Test the application before release.

Project: Team leader, Project manager

Deliverables.
Objective			     Priority	Release		Status
Create aalgorithm  of growing corps  High            v0 


Deliverable	Contributors	   Dependencies		Acceptance criteria	Status		Timelines

Labeled         Data collectors,   Unlabeled data       Valid dataset           In-progress     ? weeks
dataset for     labeling team
training

Trained model   Machine Learner    Labeled dataset      Evoluation results      In-progress     ? week

Design of
the application Designer           Information about    Modern comfortable      In-progress     ? week
                                   the project          design

Application     Programmer,        UX/UI design         Working application     In-progress     ? week
		Machine learner

Testing         Testers            Application          Positive ratings        In-progress     ? week
							and a minimum 
							number of bugs

Production      Product managers,  Tested application   Release of the		In-progress     ? weeks
		Advertisers				application to
							production




