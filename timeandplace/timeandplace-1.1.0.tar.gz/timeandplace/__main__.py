from . import *
import argparse
import json
import sys
import terminaltables

def sign_in(args, client: TimeAndPlace):
    
    # Ensure we have needed args
    if not args.student or not args.terminal:
        print("Requires --student and --terminal to be set", file=sys.stderr)
        exit(1)

    # Make signin request
    try:
        client.signInStudentToTerminal(args.terminal, args.student)
    except StudentNotFoundException:
        print(f"Student {args.student} does not exist", file=sys.stderr)
        exit(1)

    print("Signed in")

def sign_out(args, client: TimeAndPlace):
    
    # Ensure we have needed args
    if not args.student or not args.terminal:
        print("Requires --student and --terminal to be set", file=sys.stderr)
        exit(1)

    # Make signout request
    try:
        client.signOutStudentFromTerminal(args.terminal, args.student)
    except StudentNotFoundException:
        print(f"Student {args.student} does not exist", file=sys.stderr)
        exit(1)
    
    print("Signed out")

def get_student_info(args, client: TimeAndPlace):
    
    # Ensure we have needed args
    if not args.student:
        print("Requires --student to be set", file=sys.stderr)
        exit(1)

    # Make lookup request
    student:dict
    try:
        student = client.getStudentInfo(args.student)
    except StudentNotFoundException:
        print(f"Student {args.student} does not exist", file=sys.stderr)
        exit(1)

    # Build user data table
    table = terminaltables.SingleTable([
        ["Name", f"{student.name[1]}, {student.name[0]}"],
        ["ID", f"{student.student_id}"],
        ["Username", f"{student.username}"],
        ["Gender", f"{student.gender}"],
        ["Birthdate", f"{student.dob}"],
        ["Age", f"{student.age}"],
        ["Photo", f"{student.photo}"],
        ["Gaurdian Email", f"{student.gaurdian_email}"],
        ["Gaurdian Phone", f"{student.gaurdian_phone}"],
        ["Courses", ", ".join(student.timetable)],
    ])

    print(table.table)
    

def get_student_ids(args, client: TimeAndPlace):
    
    # Ensure we have needed args
    if not args.username or not args.password:
        print("Requires --username and --password to be set", file=sys.stderr)
        exit(1)
    
    # Log in
    try:
        client.login(args.username, args.password)
    except InvalidAuthException:
        print("Invalid authentication info", file=sys.stderr)
        exit(1)

    # Make lookup request
    students = list(client.getAllStudents())
    students.sort()

    # Dump data
    for student in students:
        print(student)

# Command map
command_actions = {
    "signin": (sign_in, "Sign a student in to a terminal"),
    "signout": (sign_out, "Sign a student out form a terminal"),
    "student/info": (get_student_info, "Get JSON-formatted info about a student"),
    "students/ids": (get_student_ids, "Get a raw list of all valid student IDs"),
}

# Handle CLI args
ap = argparse.ArgumentParser(description="Use the \"help\" action for info on actions")

# Endpoints
ap.add_argument("-e", "--endpoint", help="Set a custom server address")

# Auth
ap.add_argument("--username", help="TimeAndPlace username", required=False)
ap.add_argument("--password", help="TimeAndPlace password", required=False)

# Flags
ap.add_argument("-s", "--student", help="Student ID", required=False)
ap.add_argument("-t", "--terminal", help="Terminal ID", required=False)

# Action
ap.add_argument("action", help="Action to run")

# Get args
args = ap.parse_args()

# Handle help action
if args.action == "help":
    # Build table data
    data = [[key, command_actions[key][1]] for key in command_actions]
    table = terminaltables.SingleTable(data)

    # Display table
    table.title = "Available actions"
    table.inner_heading_row_border = False
    print(table.table)

    # print("List of available actions:")
    # print("  Action\t\tDescription")

    # for key in command_actions:
    #     print(f"  {key}\t\t{command_actions[key][1]}")

    exit(0)

# Check that action is valid
if not args.action in command_actions:
    print("Action not valid. See help.", file=sys.stderr)
    exit(1)

# Create a new client
if args.endpoint:
    client = TimeAndPlace(endpoint = args.endpoint)
else:
    client = TimeAndPlace()

# Run action
command_actions[args.action][0](args, client)