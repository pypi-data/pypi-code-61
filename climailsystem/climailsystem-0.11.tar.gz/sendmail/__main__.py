import click
import sendmail as sm
@click.group()
def main():
    pass
@click.command(name="mdetails")
def umdetails():
    click.echo(sm.usermessagedetails())
@click.command()
def udetails():
    click.echo(sm.userdetails())
@click.command()
def deleteapicreds():
    sm.deleteapicreds()
    click.echo("deleted successfully")
@click.command()
def relogin():
    sm.login()
    click.echo("success")
@click.command()
@click.argument('email_id_of_sender')
@click.argument('Subject')
@click.argument('mssg')
def sendmessage(email_id_of_sender,subject,mssg):
    click.echo("Sending Email")
    sm.sendmessage(email_id_of_sender,subject,mssg)
@click.command()
@click.argument('email_id')
@click.argument('subject')
@click.argument('mssg')
@click.argument('file_path')
def sendmessage_attach(email_id,subject,mssg,file_path):
    click.echo('Sending Email')
    sm.sendmessage_attach(email_id,subject,mssg,file_path)
@click.command()
@click.argument('email_adrss')
@click.argument('subject')
@click.option('htmlfile',help="enter the complete address for html mail file")
@click.option('html',help="Enter the html mail to send")
@click.option('text')
def sendhtml(email_adrss,subject,html_file = None,html = None,text = None):
    if html_file:
        htm = ""
        with open(html_file,'r+') as fl:
            for x in fl:
                htm += x
        sm.sendhtmlmssg(email_adrss,subject,htm,text)
    else:
        sm.sendhtmlmssg(email_adrss,subject,html,text)
main.add_command(sendmessage);
main.add_command(sendmessage_attach)
main.add_command(relogin)
main.add_command(deleteapicreds)
main.add_command(udetails)
main.add_command(umdetails)
main.add_command(sendhtml)
main()
