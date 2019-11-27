# Django Unit Test starter code and functional requirements template

Use the provided starter project for this exercise.

### Development Request
Your stakeholders have requested some enhancements to their software solution 'Good Vibes'.

* Add a new web page that returns a random good vibes message to the user.

### Exercise Deliverables
* Produce a Functional Requirements Brief document in regards to the new feature(s) requested
* Add the code to return a random good vibes message from a hardcoded list of messages in views.py and render it in the template ```mod.html```
* Create a test case that tests that your route to the message of the day page is valid and returns a web page

#### Challenge:
* Add a web page that contains a form that lets users submit their own good vibes message for addition to the available messages. (hint: just add message submitted to the existing message list)
* Add a test case for the form that ensures that the form cannot be submitted with message that does not contain the text ```good vibes``` somewhere in the text.


## Functional Requirements Template

### Application Purpose
Provide a high-level summary of what the requirements the application is attempting to address. Why are you building this particular application/solution?
### Assumptions About the Application
Note any assumptions the user should have about this application and it features (e.g. “this is only the first phase of development and does not represent the final version of this feature.”).
### Development Constraints
Typically in software development, the typical constraints are things like People, budget, outside dependencies, limitations on technologies that can be used, etc. 
### Application Design Considerations:
Put some time into thinking about the overall design of your application/solution and note things that should be considered that may impact how you design your application. (e.g. will require integration into some sort of payment processing service to handle transactions. 
### Application Requirements:
List the general requirements (as 1 or 2 sentences) and then providing any specific details as bullets. These requirements should be at a high level without concern for implementation details
* Application Wireframes
Planned frontend layout, use case flows between different features/screens. For backend applications, a documented list of expected endpoints with a brief description of function they serve, relationship(s) to any specific frontend features.

### Open Issues/Concerns/Future Enhancements
This section is used to capture ideas for future new enhancements and/or areas of the application that may need additional work, including documentation updates, code that needs refactoring due to performance, stability, or other concerns.
