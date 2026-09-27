# ================================================================
# MICT802 - Assessment 3
# Student Performance Tracking and Decision Support System
# ================================================================

from statistics import mean, median, stdev


# ================================================================
# STUDENT CLASS
# ================================================================

class Student:
    """Represents one student and provides performance analysis."""

    def __init__(self, student_id, name, course,
                 assignment_mark, quiz_mark, exam_mark,
                 attendance, study_hours):

        self.student_id = student_id
        self.name = name
        self.course = course
        self.assignment_mark = assignment_mark
        self.quiz_mark = quiz_mark
        self.exam_mark = exam_mark
        self.attendance = attendance
        self.study_hours = study_hours

    # ------------------------------------------------------------
    # Calculate weighted overall mark
    # Assignment = 30%, Quiz = 20%, Exam = 50%
    # ------------------------------------------------------------

    def calculate_overall_mark(self):

        return (
            self.assignment_mark * 0.30
            + self.quiz_mark * 0.20
            + self.exam_mark * 0.50
        )

    # ------------------------------------------------------------
    # Rule-Based Performance Classification
    # ------------------------------------------------------------

    def classify_performance(self):

        mark = self.calculate_overall_mark()

        if mark >= 85:
            return "Excellent"

        elif mark >= 75:
            return "Good"

        elif mark >= 60:
            return "Average"

        else:
            return "Poor"

    # ------------------------------------------------------------
    # Rule-Based Recommendation Engine
    # ------------------------------------------------------------

    def generate_recommendations(self):

        recommendations = []

        overall = self.calculate_overall_mark()

        if overall < 50:

            recommendations.append(
                "Academic support is strongly recommended."
            )

        if self.assignment_mark < 60:

            recommendations.append(
                "Improve assignment preparation and submission quality."
            )

        if self.quiz_mark < 60:

            recommendations.append(
                "Revise weekly topics and practise more quiz questions."
            )

        if self.exam_mark < 60:

            recommendations.append(
                "Increase exam revision and practise past questions."
            )

        if self.attendance < 75:

            recommendations.append(
                "Improve class attendance."
            )

        if self.study_hours < 5:

            recommendations.append(
                "Increase weekly independent study hours."
            )

        if overall >= 85 and self.attendance >= 85:

            recommendations.append(
                "Maintain the current excellent performance."
            )

        if not recommendations:

            recommendations.append(
                "Continue current study habits and monitor progress."
            )

        return recommendations

    # ------------------------------------------------------------
    # Convert Student Object into Dictionary
    # ------------------------------------------------------------

    def to_dictionary(self):

        return {
            "Student ID": self.student_id,
            "Name": self.name,
            "Course": self.course,
            "Assignment": self.assignment_mark,
            "Quiz": self.quiz_mark,
            "Exam": self.exam_mark,
            "Attendance": self.attendance,
            "Study Hours": self.study_hours,
            "Overall": round(self.calculate_overall_mark(), 2),
            "Classification": self.classify_performance()
        }


# ================================================================
# STUDENT PERFORMANCE TRACKING SYSTEM
# ================================================================

class StudentPerformanceSystem:

    def __init__(self):

        # List data structure
        self.students = []

        # Dictionary data structure
        # Student ID is used as the key
        self.student_lookup = {}

        # Set data structure
        # Stores unique courses
        self.courses = set()

        # Tuple data structure
        # Stores fixed performance categories
        self.performance_categories = (
            "Excellent",
            "Good",
            "Average",
            "Poor"
        )

    # ------------------------------------------------------------
    # Validate Numeric Marks
    # ------------------------------------------------------------

    @staticmethod
    def validate_mark(value, field_name):

        try:

            value = float(value)

            if value < 0 or value > 100:

                raise ValueError(
                    f"{field_name} must be between 0 and 100."
                )

            return value

        except (ValueError, TypeError):

            raise ValueError(
                f"Invalid value for {field_name}."
            )

    # ------------------------------------------------------------
    # Validate Study Hours
    # ------------------------------------------------------------

    @staticmethod
    def validate_study_hours(value):

        try:

            value = float(value)

            if value < 0 or value > 100:

                raise ValueError(
                    "Study hours must be between 0 and 100."
                )

            return value

        except (ValueError, TypeError):

            raise ValueError(
                "Invalid study hours."
            )

    # ------------------------------------------------------------
    # Add Student Record
    # ------------------------------------------------------------

    def add_student(self, student_id, name, course,
                    assignment, quiz, exam,
                    attendance, study_hours):

        try:

            student_id = str(student_id).strip()
            name = str(name).strip()
            course = str(course).strip()

            # Check empty Student ID
            if not student_id:

                raise ValueError(
                    "Student ID cannot be empty."
                )

            # Check empty name
            if not name:

                raise ValueError(
                    "Student name cannot be empty."
                )

            # Check empty course
            if not course:

                raise ValueError(
                    "Course cannot be empty."
                )

            # Check duplicate Student ID
            if student_id in self.student_lookup:

                raise ValueError(
                    f"Student ID {student_id} already exists."
                )

            # Validate numerical values
            assignment = self.validate_mark(
                assignment,
                "Assignment Mark"
            )

            quiz = self.validate_mark(
                quiz,
                "Quiz Mark"
            )

            exam = self.validate_mark(
                exam,
                "Exam Mark"
            )

            attendance = self.validate_mark(
                attendance,
                "Attendance"
            )

            study_hours = self.validate_study_hours(
                study_hours
            )

            # Create Student Object
            student = Student(
                student_id,
                name,
                course,
                assignment,
                quiz,
                exam,
                attendance,
                study_hours
            )

            # Add student to list
            self.students.append(student)

            # Add student to dictionary
            self.student_lookup[student_id] = student

            # Add course to set
            self.courses.add(course)

            return True

        except ValueError as error:

            print(f"\nWARNING: {error}")
            print("Invalid record skipped.\n")

            return False

    # ------------------------------------------------------------
    # Find Student Using Student ID
    # ------------------------------------------------------------

    def find_student(self, student_id):

        student = self.student_lookup.get(student_id)

        if student is None:

            print("\nStudent not found.")

            return None

        return student

    # ------------------------------------------------------------
    # Display Individual Student
    # ------------------------------------------------------------

    def display_student(self, student):

        print("\n" + "=" * 65)
        print("STUDENT PERFORMANCE DETAILS")
        print("=" * 65)

        print(
            f"Student ID       : {student.student_id}"
        )

        print(
            f"Name             : {student.name}"
        )

        print(
            f"Course           : {student.course}"
        )

        print(
            f"Assignment Mark  : {student.assignment_mark:.2f}"
        )

        print(
            f"Quiz Mark        : {student.quiz_mark:.2f}"
        )

        print(
            f"Exam Mark        : {student.exam_mark:.2f}"
        )

        print(
            f"Attendance       : {student.attendance:.2f}%"
        )

        print(
            f"Study Hours      : {student.study_hours:.2f} hours"
        )

        print(
            f"Overall Mark     : "
            f"{student.calculate_overall_mark():.2f}"
        )

        print(
            f"Classification   : "
            f"{student.classify_performance()}"
        )

        print("\nRecommendations:")

        for number, recommendation in enumerate(
                student.generate_recommendations(), 1):

            print(
                f"{number}. {recommendation}"
            )

        print("=" * 65)

    # ------------------------------------------------------------
    # Display All Students
    # ------------------------------------------------------------

    def display_all_students(self):

        if not self.students:

            print(
                "\nNo student records available."
            )

            return

        print("\n" + "=" * 110)

        print(
            "ALL STUDENT PERFORMANCE RECORDS"
        )

        print("=" * 110)

        print(
            f"{'ID':<8}"
            f"{'Name':<22}"
            f"{'Course':<10}"
            f"{'Assign':>8}"
            f"{'Quiz':>8}"
            f"{'Exam':>8}"
            f"{'Attend':>10}"
            f"{'Overall':>10}"
            f"{'Class':>12}"
        )

        print("-" * 110)

        for student in self.students:

            print(
                f"{student.student_id:<8}"
                f"{student.name:<22}"
                f"{student.course:<10}"
                f"{student.assignment_mark:>8.1f}"
                f"{student.quiz_mark:>8.1f}"
                f"{student.exam_mark:>8.1f}"
                f"{student.attendance:>9.1f}%"
                f"{student.calculate_overall_mark():>10.2f}"
                f"{student.classify_performance():>12}"
            )

        print("=" * 110)

    # ------------------------------------------------------------
    # Descriptive Analytics
    # ------------------------------------------------------------

    def descriptive_analytics(self):

        if not self.students:

            print(
                "\nNo data available for analysis."
            )

            return

        # Store overall marks
        overall_marks = [

            student.calculate_overall_mark()

            for student in self.students
        ]

        # Store attendance
        attendance_values = [

            student.attendance

            for student in self.students
        ]

        # Store study hours
        study_hours = [

            student.study_hours

            for student in self.students
        ]

        print("\n" + "=" * 70)

        print(
            "DESCRIPTIVE ANALYTICS"
        )

        print("=" * 70)

        # Total number of students
        print(
            f"Total Students          : "
            f"{len(self.students)}"
        )

        # Minimum value
        print(
            f"Minimum Overall Mark    : "
            f"{min(overall_marks):.2f}"
        )

        # Maximum value
        print(
            f"Maximum Overall Mark    : "
            f"{max(overall_marks):.2f}"
        )

        # Average value
        print(
            f"Average Overall Mark    : "
            f"{mean(overall_marks):.2f}"
        )

        # Median
        print(
            f"Median Overall Mark     : "
            f"{median(overall_marks):.2f}"
        )

        # Standard deviation
        if len(overall_marks) > 1:

            print(
                f"Standard Deviation      : "
                f"{stdev(overall_marks):.2f}"
            )

        else:

            print(
                "Standard Deviation      : N/A"
            )

        # Average attendance
        print(
            f"Average Attendance      : "
            f"{mean(attendance_values):.2f}%"
        )

        # Average study hours
        print(
            f"Average Study Hours     : "
            f"{mean(study_hours):.2f}"
        )

        # Number of passed students
        passed = sum(

            1 for mark in overall_marks

            if mark >= 50
        )

        # Number of failed students
        failed = len(self.students) - passed

        # Pass rate
        pass_rate = (

            passed / len(self.students)

        ) * 100

        print(
            f"Students Passed         : {passed}"
        )

        print(
            f"Students Failed         : {failed}"
        )

        print(
            f"Pass Rate               : {pass_rate:.2f}%"
        )

        # Highest performing student
        highest_student = max(

            self.students,

            key=lambda s: s.calculate_overall_mark()
        )

        # Lowest performing student
        lowest_student = min(

            self.students,

            key=lambda s: s.calculate_overall_mark()
        )

        print(
            f"Highest Performer       : "
            f"{highest_student.name} "
            f"({highest_student.calculate_overall_mark():.2f})"
        )

        print(
            f"Lowest Performer        : "
            f"{lowest_student.name} "
            f"({lowest_student.calculate_overall_mark():.2f})"
        )

        print("=" * 70)

    # ------------------------------------------------------------
    # Performance Classification Summary
    # ------------------------------------------------------------

    def classification_summary(self):

        if not self.students:

            print(
                "\nNo data available."
            )

            return

        classification_count = {

            category: 0

            for category in self.performance_categories
        }

        for student in self.students:

            category = (
                student.classify_performance()
            )

            classification_count[
                category
            ] += 1

        print("\n" + "=" * 60)

        print(
            "PERFORMANCE CLASSIFICATION SUMMARY"
        )

        print("=" * 60)

        for category, count in \
                classification_count.items():

            percentage = (

                count / len(self.students)

            ) * 100

            print(
                f"{category:<15}: "
                f"{count:<3} students "
                f"({percentage:.2f}%)"
            )

        print("=" * 60)

    # ------------------------------------------------------------
    # Course Performance Summary
    # ------------------------------------------------------------

    def course_summary(self):

        if not self.students:

            print(
                "\nNo data available."
            )

            return

        print("\n" + "=" * 75)

        print(
            "PERFORMANCE SUMMARY BY COURSE"
        )

        print("=" * 75)

        # Loop through each unique course
        for course in sorted(self.courses):

            course_students = [

                student

                for student in self.students

                if student.course == course
            ]

            course_marks = [

                student.calculate_overall_mark()

                for student in course_students
            ]

            course_attendance = [

                student.attendance

                for student in course_students
            ]

            print(
                f"\nCourse: {course}"
            )

            print(
                f"Number of Students : "
                f"{len(course_students)}"
            )

            print(
                f"Average Mark       : "
                f"{mean(course_marks):.2f}"
            )

            print(
                f"Highest Mark       : "
                f"{max(course_marks):.2f}"
            )

            print(
                f"Lowest Mark        : "
                f"{min(course_marks):.2f}"
            )

            print(
                f"Average Attendance : "
                f"{mean(course_attendance):.2f}%"
            )

        print("\n" + "=" * 75)

    # ------------------------------------------------------------
    # Identify Students Requiring Academic Support
    # ------------------------------------------------------------

    def students_at_risk(self):

        at_risk = []

        for student in self.students:

            overall = (
                student.calculate_overall_mark()
            )

            # At-risk rules
            if (
                overall < 60
                or student.attendance < 75
                or student.exam_mark < 50
            ):

                at_risk.append(student)

        print("\n" + "=" * 85)

        print(
            "STUDENTS REQUIRING ACADEMIC SUPPORT"
        )

        print("=" * 85)

        if not at_risk:

            print(
                "No students currently identified as at risk."
            )

            return

        for student in at_risk:

            print(
                f"\n{student.student_id} - "
                f"{student.name}"
            )

            print(
                f"Overall: "
                f"{student.calculate_overall_mark():.2f}"
            )

            print(
                f"Attendance: "
                f"{student.attendance:.2f}%"
            )

            print(
                "Recommended Actions:"
            )

            for recommendation in \
                    student.generate_recommendations():

                print(
                    f"  - {recommendation}"
                )

        print("=" * 85)

    # ------------------------------------------------------------
    # Overall Decision-Support Recommendations
    # ------------------------------------------------------------

    def system_recommendations(self):

        if not self.students:

            print(
                "\nNo data available."
            )

            return

        overall_marks = [

            student.calculate_overall_mark()

            for student in self.students
        ]

        attendance = [

            student.attendance

            for student in self.students
        ]

        # Count poor-performing students
        poor_students = sum(

            1

            for student in self.students

            if student.classify_performance()
            == "Poor"
        )

        # Count low attendance students
        low_attendance = sum(

            1

            for student in self.students

            if student.attendance < 75
        )

        print("\n" + "=" * 75)

        print(
            "SYSTEM DECISION-SUPPORT RECOMMENDATIONS"
        )

        print("=" * 75)

        average_mark = mean(
            overall_marks
        )

        average_attendance = mean(
            attendance
        )

        print(
            f"Overall Average Mark : "
            f"{average_mark:.2f}"
        )

        print(
            f"Average Attendance   : "
            f"{average_attendance:.2f}%"
        )

        print(
            "\nRecommendations:"
        )

        recommendation_number = 1

        # Recommendation 1
        if average_mark < 60:

            print(
                f"{recommendation_number}. "
                "Provide additional academic "
                "support classes."
            )

            recommendation_number += 1

        # Recommendation 2
        if average_attendance < 80:

            print(
                f"{recommendation_number}. "
                "Introduce attendance improvement "
                "strategies."
            )

            recommendation_number += 1

        # Recommendation 3
        if poor_students >= 5:

            print(
                f"{recommendation_number}. "
                "Review teaching and assessment "
                "support for low-performing students."
            )

            recommendation_number += 1

        # Recommendation 4
        if low_attendance >= 5:

            print(
                f"{recommendation_number}. "
                "Contact students with low attendance "
                "and provide early intervention."
            )

            recommendation_number += 1

        # Recommendation 5
        if average_mark >= 75:

            print(
                f"{recommendation_number}. "
                "Overall academic performance is strong; "
                "maintain current learning support."
            )

        print("=" * 75)


# ================================================================
# SAMPLE STUDENT DATASET
# 24 Student Records
# ================================================================

def load_sample_data(system):

    sample_students = [

        # --------------------------------------------------------
        # Group Member Names
        # --------------------------------------------------------

        (
            "S001",
            "Sujan Bhujel",
            "MICT",
            88,
            82,
            91,
            95,
            12
        ),

        (
            "S002",
            "Samarpan Kharel",
            "MICT",
            72,
            75,
            78,
            88,
            9
        ),

        (
            "S003",
            "Anshu Chaudhary",
            "MIT",
            65,
            68,
            61,
            80,
            7
        ),

        (
            "S004",
            "Samyog Bajgain",
            "MIT",
            92,
            90,
            94,
            97,
            14
        ),

        (
            "S005",
            "Prassanna Kaami",
            "MICT",
            48,
            55,
            45,
            68,
            4
        ),

        (
            "S006",
            "Prasun Damai",
            "MIT",
            81,
            84,
            79,
            92,
            11
        ),

        # --------------------------------------------------------
        # Additional Nepali Student Names
        # --------------------------------------------------------

        (
            "S007",
            "Aayush Shrestha",
            "MICT",
            58,
            62,
            54,
            72,
            5
        ),

        (
            "S008",
            "Sushmita Karki",
            "MIT",
            76,
            74,
            80,
            86,
            10
        ),

        (
            "S009",
            "Bikash Thapa",
            "MICT",
            69,
            65,
            71,
            83,
            8
        ),

        (
            "S010",
            "Pratiksha Gurung",
            "MIT",
            95,
            93,
            96,
            98,
            16
        ),

        (
            "S011",
            "Roshan Adhikari",
            "MICT",
            52,
            48,
            50,
            70,
            4
        ),

        (
            "S012",
            "Asmita Rai",
            "MIT",
            84,
            80,
            86,
            90,
            12
        ),

        (
            "S013",
            "Nischal Pandey",
            "MICT",
            61,
            64,
            59,
            78,
            6
        ),

        (
            "S014",
            "Sneha Bhandari",
            "MIT",
            78,
            82,
            75,
            89,
            10
        ),

        (
            "S015",
            "Sagar Poudel",
            "MICT",
            43,
            50,
            46,
            65,
            3
        ),

        (
            "S016",
            "Anisha Maharjan",
            "MIT",
            89,
            87,
            91,
            94,
            13
        ),

        (
            "S017",
            "Bibek Ghimire",
            "MICT",
            73,
            70,
            76,
            84,
            8
        ),

        (
            "S018",
            "Rojina Lama",
            "MIT",
            67,
            72,
            69,
            81,
            7
        ),

        (
            "S019",
            "Kiran Oli",
            "MICT",
            56,
            58,
            52,
            74,
            5
        ),

        (
            "S020",
            "Sarita Tamang",
            "MIT",
            86,
            88,
            84,
            93,
            12
        ),

        (
            "S021",
            "Nabin Koirala",
            "MICT",
            63,
            60,
            66,
            79,
            7
        ),

        (
            "S022",
            "Puja Basnet",
            "MIT",
            91,
            89,
            92,
            96,
            15
        ),

        (
            "S023",
            "Rajan Gautam",
            "MICT",
            77,
            73,
            79,
            87,
            9
        ),

        (
            "S024",
            "Manisha Rijal",
            "MIT",
            54,
            57,
            51,
            71,
            4
        )
    ]

    # Add each sample student to the system
    for record in sample_students:

        system.add_student(
            record[0],
            record[1],
            record[2],
            record[3],
            record[4],
            record[5],
            record[6],
            record[7]
        )


# ================================================================
# ADD STUDENT MANUALLY
# ================================================================

def add_student_manually(system):

    print("\nADD NEW STUDENT")
    print("-" * 40)

    try:

        student_id = input(
            "Student ID: "
        ).strip()

        name = input(
            "Student Name: "
        ).strip()

        course = input(
            "Course: "
        ).strip()

        assignment = input(
            "Assignment Mark (0-100): "
        )

        quiz = input(
            "Quiz Mark (0-100): "
        )

        exam = input(
            "Exam Mark (0-100): "
        )

        attendance = input(
            "Attendance Percentage (0-100): "
        )

        study_hours = input(
            "Weekly Study Hours: "
        )

        success = system.add_student(
            student_id,
            name,
            course,
            assignment,
            quiz,
            exam,
            attendance,
            study_hours
        )

        if success:

            print(
                "\nStudent successfully added."
            )

    except Exception as error:

        print(
            f"\nUnexpected error: {error}"
        )


# ================================================================
# SEARCH STUDENT
# ================================================================

def search_student(system):

    student_id = input(
        "\nEnter Student ID: "
    ).strip()

    student = system.find_student(
        student_id
    )

    if student:

        system.display_student(
            student
        )


# ================================================================
# MAIN MENU
# ================================================================

def display_menu():

    print("\n")

    print("=" * 70)

    print(
        "      STUDENT PERFORMANCE TRACKING SYSTEM"
    )

    print("=" * 70)

    print(
        "1. Display All Students"
    )

    print(
        "2. Search Student"
    )

    print(
        "3. Add New Student"
    )

    print(
        "4. Descriptive Analytics"
    )

    print(
        "5. Performance Classification Summary"
    )

    print(
        "6. Course Performance Summary"
    )

    print(
        "7. Students Requiring Support"
    )

    print(
        "8. Decision-Support Recommendations"
    )

    print(
        "9. Exit"
    )

    print("=" * 70)


# ================================================================
# MAIN APPLICATION
# ================================================================

def main():

    # Create the system
    system = StudentPerformanceSystem()

    # Load the sample dataset
    load_sample_data(system)

    print(
        "\nStudent Performance Tracking "
        "System started."
    )

    print(
        f"{len(system.students)} "
        "student records loaded successfully."
    )

    # Continue displaying menu until user exits
    while True:

        display_menu()

        try:

            choice = input(
                "Enter your choice (1-9): "
            ).strip()

            # ----------------------------------------------------
            # OPTION 1 - Display All Students
            # ----------------------------------------------------

            if choice == "1":

                system.display_all_students()

            # ----------------------------------------------------
            # OPTION 2 - Search Student
            # ----------------------------------------------------

            elif choice == "2":

                search_student(system)

            # ----------------------------------------------------
            # OPTION 3 - Add Student
            # ----------------------------------------------------

            elif choice == "3":

                add_student_manually(system)

            # ----------------------------------------------------
            # OPTION 4 - Descriptive Analytics
            # ----------------------------------------------------

            elif choice == "4":

                system.descriptive_analytics()

            # ----------------------------------------------------
            # OPTION 5 - Classification Summary
            # ----------------------------------------------------

            elif choice == "5":

                system.classification_summary()

            # ----------------------------------------------------
            # OPTION 6 - Course Summary
            # ----------------------------------------------------

            elif choice == "6":

                system.course_summary()

            # ----------------------------------------------------
            # OPTION 7 - At-Risk Students
            # ----------------------------------------------------

            elif choice == "7":

                system.students_at_risk()

            # ----------------------------------------------------
            # OPTION 8 - Recommendations
            # ----------------------------------------------------

            elif choice == "8":

                system.system_recommendations()

            # ----------------------------------------------------
            # OPTION 9 - Exit
            # ----------------------------------------------------

            elif choice == "9":

                print("\n" + "=" * 60)

                print(
                    "Thank you for using the "
                    "Student Performance Tracking System."
                )

                print("=" * 60)

                break

            # ----------------------------------------------------
            # Invalid Menu Selection
            # ----------------------------------------------------

            else:

                print(
                    "\nInvalid choice. "
                    "Please enter a number from 1 to 9."
                )

        # Handle Ctrl+C
        except KeyboardInterrupt:

            print(
                "\n\nProgram stopped by user."
            )

            break

        # Handle unexpected errors
        except Exception as error:

            print(
                f"\nAn unexpected error occurred: "
                f"{error}"
            )


# ================================================================
# START PROGRAM
# ================================================================

if __name__ == "__main__":

    main()