


Models & Relationships
User Model ->Students and tutors

Tutor Profile Model -> Tutors' expertise and availability

Lesson Model -> Scheduled learning sessions

Review Model -> Feedback on tutors

Relationships:
A User can be either a tutor or a student.

A User can have one Tutor Profile if they register as a tutor.

A Student can book multiple Lessons.

A Lesson is associated with a Tutor Profile and a Student.

A Review belongs to a Student and references a Tutor Profile.