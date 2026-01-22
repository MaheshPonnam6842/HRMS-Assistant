from mcp.server.fastmcp import FastMCP
from torch.profiler import schedule

from HRMS import *
from  utils import seed_services
mcp= FastMCP('hr-assistant')

# tools
#resources
#prompt
employee_manager= EmployeeManager()
meeting_manager= MeetingManager()
leave_manager= LeaveManager()
ticket_manager= TicketManager()
import os
from dotenv import load_dotenv
load_dotenv()
from emails import EmailSender
seed_services(employee_manager, leave_manager, meeting_manager, ticket_manager)
email_sender = EmailSender(
        smtp_server="smtp.gmail.com",
        port=587,
        username=os.getenv("EMAIL"),
        password=os.getenv("EMAIL_PWD"),
        use_tls=True)

@mcp.tool()
def add_employee(emp_name:str, manager_id: str, email: str) -> str:
    """
      Add a new employee to the HRMS system.
      :param emp_name: Employee name
      :param manager_id: Manager ID (optional)
      :return: Confirmation message
      """
    emp= EmployeeCreate(
        emp_id= employee_manager.get_next_emp_id(),
        name= emp_name,
        manager_id= manager_id,
        email= email
    )
    employee_manager.add_employee(emp)
    return f"Employee {emp_name} added successfully"

@mcp.tool()
def et_employee_details(name:str) -> dict[str, str]:
    """
    Get employee details by name.
    :param name: Name of the employee
    :return: Employee ID and manager ID
    """
    matches= employee_manager.search_employee_by_name(name)
    if len(matches)== 0:
        raise f"No Employees matches found"

    emp_id= matches[0]

    return employee_manager.get_employee_details(emp_id)

@mcp.tool()
def send_mail(subject: str, body: str, to_emails: str):
    """
       Sends an email with the given subject and body to one or more recipients.

       Args:
           subject (str): The subject line of the email.
           body (str): The plain-text content or message body of the email.
           to_emails (str): The recipient email address or a comma-separated list of addresses.

       Returns:
           None

       Notes:
           This function uses the global `email_sender` instance to send the email.
           Ensure that `email_sender.username` and SMTP credentials are configured properly
           before calling this function.
       """
    email_sender.send_email(
    subject=subject,
    body=body,
    to_emails=to_emails,
    from_email=email_sender.username)

@mcp.tool()

def create_ticket(emp_id: str, item: str, reason: str)-> str:
    ticket_req= TicketCreate(
        emp_id= emp_id,
        item=item,
        reason= reason
    )
    return ticket_manager.create_ticket(ticket_req)

mcp.tool()

def schedule_meeting(employee_id: str, meeting_datetime: datetime, topic: str )-> str:
    """
        Schedule a meeting for an employee.
        :param employee_id: Employee ID
        :param meeting_datetime: Date and time of the meeting in python datetime format
        :param topic: Topic of the meeting
        :return: Confirmation message
        """
    meeting_req= MeetingCreate(
        employee_id= employee_id,
        meeting_dt= meeting_datetime,
        topic= topic
    )
    return meeting_manager.schedule_meeting(meeting_req)


@mcp.prompt()
def apply_leave(emp_id: str, leave_dates: list)->str:
    """
      Apply for leave for an employee.
      :param emp_id: Employee ID
      :param leave_dates: List of leave dates
      :return: Leave application status message
      """
    leave_req= LeaveApplyRequest(emp_id= emp_id, leave_dates= leave_dates)
    return leave_manager.apply_leave(leave_req)

@mcp.prompt("Onboard new employee")
def onboard_new_employee(employee_name: str, manager_name: str):
    return f"""Onboard a new employee with the following details:
       - Name: {employee_name}
       - Manager Name: {manager_name}
       Steps to follow:
       - Add the employee to the HRMS system.
       - Send a welcome email to the employee with their login credentials. (Format: employee_name@atliq.com)
       - Notify the manager about the new employee's onboarding.
       - Raise tickets for a new laptop, id card, and other necessary equipment.
       - Schedule an introductory meeting between the employee and the manager
    
       
       """




if __name__=="__main__":
    mcp.run(transport='stdio')
