import s3

con = s3.Connection()
con.connect()
con.process_all("lake")