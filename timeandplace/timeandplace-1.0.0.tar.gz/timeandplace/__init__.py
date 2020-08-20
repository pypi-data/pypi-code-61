import requests
import re
from typing import List, Tuple, Generator

# Exceptions
class InvalidAuthException(Exception):
    def __init__(self):
        super().__init__("Invalid login credentials")

class NotLoggedInException(Exception):
    def __init__(self):
        super().__init__("Not logged in")

class StudentNotFoundException(Exception):
    def __init__(self):
        super().__init__("Student not found")

class NotImplementedException(Exception):
    def __init__(self):
        super().__init__("Not implemented")

class StudentInfo(object):
    def __init__(self, json: dict, endpoint: str):
        self.json = json
        self.student_id = json["record"]["studentID"]
        self.name = (json["record"]["firstname"], json["record"]["lastname"])
        self.gender = json["record"]["gender"]
        self.dob = json["record"]["dob"]
        self.timetable = json["record"]["timetable"].split(" ")
        self.username = json["record"]["loginID"]
        self.age = json["age"]
        self.photo = endpoint + json["photoURL"]

        self.gaurdian_phone = json["record"]["guardianPhone"]
        self.gaurdian_email = json["record"]["guardianEmail"]

    def __str__(self):
        return str(self.json)

class CourseInfo(object):
    def __init__(self, code: str, teacher_fname: str, teacher_lname: str, period: int):
        self.code = code
        self.teacher_name = (teacher_fname, teacher_lname)
        self.period = period

    def __str__(self):
        return str({
            "code": self.code,
            "period": self.period,
            "teacher_name": self.teacher_name
        })

class TimeAndPlace(object):

    logged_in: bool = False
    
    def __init__(self, endpoint: str = "http://demo.iquark.ca:8009"):
        """Create a TimeAndPlace client

        Args:
            endpoint (str, optional): TimeAndPlace server endpoint. Defaults to "http://demo.iquark.ca:8009".
        """
        self.endpoint = endpoint

    def _checkLogin(self):
        if not self.logged_in:
            raise NotLoggedInException()

    def login(self, username: str, password: str):
        """Log in to TimeAndPlace

        Args:
            username (str): Application username
            password (str): Application password

        Raises:
            Exception: Thrown if CSRF data cannot be parsed from TimeAndPlace
            InvalidAuthException: Thrown if login details are invalid
        """

        # Build a session
        sess = requests.session()

        # Get needed cookies from server
        login_page = sess.get(f"{self.endpoint}/login").text

        # Determine the CSRF token
        try:
            self.csrf_token = re.findall(r'<input type="hidden" name="_token" value="([a-zA-Z0-9]*)">', login_page, re.M)[0]
        except IndexError as e:
            raise Exception("Remote server responded with unusual data. Please contact administrator")

        # Make actual login request
        resp = sess.post(f"{self.endpoint}/login", data={
            "username": username,
            "password": password,
            "_token":self.csrf_token
        })

        # Look for the error message
        if "These credentials do not match our records." not in resp.text:
            self.logged_in = True
            self.rsession = sess
        else:
            raise InvalidAuthException()

    def getStudentInfo(self, student_id: int) -> StudentInfo:
        """Get a student's info object

        Args:
            student_id (int): Student ID

        Raises:
            StudentNotFoundException: Thrown if the student does not exist

        Returns:
            StudentInfo: StudentInfo object
        """

        # Make a creds request
        student = requests.get(f"{self.endpoint}/studentsJSON/{student_id}").json()

        # Check for invalid ID
        if student["age"] == -1:
            raise StudentNotFoundException()

        # Create student object
        student_obj = StudentInfo(student, self.endpoint)
        return student_obj

    def getAllStudents(self) -> Generator[int, None, None]:
        """Get a list of all registered student IDs

        Returns:
            List[int]: List of student IDs
        """
        
        # Require auth
        self._checkLogin()

        # Get student listing
        students_raw = self.rsession.get(f"{self.endpoint}/allstudents").text

        # Parse out all student info
        students = re.findall(r'<tr><td>([0-9]*) \. \. \. ([a-zA-Z -]*), ([a-zA-Z -]*)<\/td><td>([a-zA-Z0-9]*)<\/td><\/tr>', students_raw, re.M)

        # Send data
        for student in students:
            yield student[0]

    def getAllCourses(self) -> List[CourseInfo]:
        """Get a list of all current courses

        Returns:
            List[CourseInfo]: List of courses
        """
        raise NotImplementedException()
    
    def signInStudentToTerminal(self, terminal_id: int, student_id: int):
        """Sign a student in to a terminal

        Args:
            terminal_id (int): Terminal ID
            student_id (int): Student ID

        Raises:
            StudentNotFoundException: Thrown if the student does not exist
        """

        # Make a toggle request
        status = requests.get(f"{self.endpoint}/terminals/{terminal_id}/toggleStudentID/{student_id}").json()

        # Check if the student was already signed in
        if status.get("status", "signed in") == "signed out":
            # Do signin again to fix the state
            requests.get(f"{self.endpoint}/terminals/{terminal_id}/toggleStudentID/{student_id}").json()

        elif status.get("status", "signed in") == "not found":
            raise StudentNotFoundException()

    def signOutStudentFromTerminal(self, terminal_id: int, student_id: int):
        """Sign a student out of a terminal

        Args:
            terminal_id (int): Terminal ID
            student_id (int): Student ID

        Raises:
            StudentNotFoundException: Thrown if the student does not exist
        """

        # Make a toggle request
        status = requests.get(f"{self.endpoint}/terminals/{terminal_id}/toggleStudentID/{student_id}").json()

        # Check if the student was already signed out
        if status.get("status", "signed in") == "signed in":
            # Do signin again to fix the state
            requests.get(f"{self.endpoint}/terminals/{terminal_id}/toggleStudentID/{student_id}").json()

        elif status.get("status", "signed in") == "not found":
            raise StudentNotFoundException()

    

    