def reset_leaderboard(eventid,client,phase):
    import mysql
    reset_query = """update mdl_hack_score set exclude =1 where eventid = {} and client = '{}' and phase = '{}'""".format(eventid,client, phase)
    try:
        mydb = mysql.connector.connect(host="www.fnmathlogic.com",user="mlportal_hack", password="m@thhackathon", database="mlportal_mdln1")
        mycursor = mydb.cursor()
        mycursor.execute(reset_query)
        mydb.commit()
        mydb.close()
        return(0,"Rows Removed :"+str(mycursor.rowcount))
    except mysql.connector.Error as err:
        print("Something went wrong: {}".format(err))
        return "1","Something went wrong: {}".format(err)

def upload_key(eventid,client,phase,indf,Bucket='hackathon.key'):
    import pandas as pd
    import boto3
    from io import StringIO
    from mathlogic import aws_access_key_id, aws_secret_access_key
    s3 = boto3.client('s3',aws_access_key_id=aws_access_key_id,aws_secret_access_key=aws_secret_access_key)
    if "id" in indf.columns:
        csv_buffer = StringIO()
        indf.to_csv(csv_buffer,index=False)
        act_file = str(eventid)+"_"+client+"_"+phase+"_"+"key.csv"
        s3.put_object(Bucket=Bucket, Key=act_file,Body=csv_buffer.getvalue())
        print("act_file :"+act_file)
    else:
        print("Dataframe should have column id")
        exit()

