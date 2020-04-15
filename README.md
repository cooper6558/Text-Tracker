## Text Tracker
### Background: Running Records
Research shows that one of the best ways to promote literacy in elementary aged
students is to track their progress via the Running Records program, in which
the teacher scores the student's reading abilities in a live, in-person reading
test. This way, teachers can help students in the areas they need most.
However, this process is extremely time consuming, and so a small team of
students at Clemson University is researching ways to automate the scoring
process.
### Following Along
The two primary challenges of the project are transcribing the student's words,
and keeping track of where the student is in the testing book so that the
transcription may be accurately scored. The transcription part is handled by
third party services such as IBM's Watson, but we were unable to find
pre-existing algorithms that could accomplish the second part: following along
with the student.
### Applications
This package includes tools to analyze text files and align two texts with each
other so that they may be compared or scored. This addresses the problem of
following along with a student during a Running Records assessment.
Applications may extend to any unlimited number of projects, such as plagiarism
detection, soft string matching, and more.
### Usage
This package is available on PyPI and can be installed via

`pip install text_tracker`

and used via

`import text_tracker`

`text_tracker.track()`

View this project on GitHub:

[hyperlink here]
### Credits
This was developed by Cooper Sanders in 2020 and is MIT licensed. You can
contact me at

<tromboneguy@coopersanders.com>

clemson.edu domain email addresses can contact me at 

<cssande@clemson.edu>

My website:

<coopersanders.com>