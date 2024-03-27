Project 2 Persistent Form: Proposal

Jayden Han: 1005654542
Khawlah Ali: 1008833390
Anvi Islam: 108866666

Institute of Communication, Culture, Information and Technology

CCT211H5: Fundamentals of User Interface Programming

Professor Michael Nixon

March 11, 2024

In Canada, most medical clinics require patients to fill out different forms. These forms usually differ from clinic to clinic, and patients need to fill out the form with a pen upon arrival, leading to inefficiencies and delays in the healthcare process. This antiquated method not only consumes valuable time for patients and healthcare workers but also increases the possibility of errors due to illegible handwriting and the possibility of germs spreading between patients from using the same pens. Recognizing the need for improvement, our team is planning to implement a solution using Python’s Tkinter library to create a persistent electronic form system. Digitalizing the patient intake process will streamline the registration process, reduce wasting time, reduce the usage of paper, lower the chance of spread of germs, and enhance data accuracy. The persistent form can be adopted in medical clinics and ensure a seamless transition to a more efficient and modernized healthcare experience.

The project aims to emulate a professional sign-up sheet commonly used in walk-in clinics. This form will intake different types of data from the user, such as by inputting information (e.g., textbox) and clicking (e.g., toggle box). Besides the user's ability to input data, the user will also be allowed to modify/update and review their data before submitting the form, ensuring CRUD functionality. After the form is submitted, a welcome message featuring the user's name will be displayed. The data received will be used to provide optimized results that are suitable to the user. For example, if the age of the user is below 18 years old, another section for the parent or guardian information will appear. The graphical user interface (GUI) will be designed to be tidy and well-spaced for the best user experience; it will have a function to increase the font size for people who are having issues reading tiny letters.

Low-Fidelity Prototype Model of Sign-Up Form

Patient Information:
a. Name:
i. Title: Mr, Ms, Mrs, Miss, Master, Madam, Sir, Doctor
ii. First Name:
iii. Middle Name:
iv. Last Name:
v. Preferred Name:
b. Address:
i. Street Address:
ii. Apt/Suite/Unit:
iii. City:
iv. Province:
v. Postal Code:
vi. Country:

c. Date of Birth: (calculates the age; if age is below 18, collect parent/guardian info/ if 16 years old or older show marital status section)
i. Month
ii. Day
iii. Year

d. Health Card Number:
i. Version Code:

e. Contact Information
i. Phone Number:

Home:
Cell:
Work:
ii. Email Address
f. Occupation:

g. Employer:

h. Marital Status: (if married, show spouse section)
i. Married

Spouse Name:
a. First:
b. Middle:
c. Last:
d. Preferred Name:
ii. Single
iii. Divorced
iv. Widowed

Billing Information: (if it is the same as the patient’s information, toggle the tick box that will fill in automatically)

Insurance Information:
a. Primary Insurance:
b. The patient is Subscriber/Policy Holder: Y/N
c. Secondary Insurance:
d. The patient is Subscriber/Policy Holder: Y/N

Insured information (if other than patient)
a. Subscriber/policy holder:
b. Relationship with the patient:

Emergency Contact:
a. Name:
i. First
ii. Middle
iii. Last
iv. Preferred
b. Relationship with Patient

Parent/ Guardian Contact Information
a. Name:
i. First
ii. Middle
iii. Last
iv. Preferred
b. Relationship with Patient
c. Phone Number
d. Email address

Medical Details:
a. Height: (conversion function of cm and ft & inch)
b. Weight: (conversion function of kg and lbs)
c. Current Medication
d. Allergies (medical/general)
e. Relevant Medical History

GitHub Link: https://github.com/jaydenhan8/Project-2
