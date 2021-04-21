import psycopg2
conn = psycopg2.connect("dbname=playground user=postgres password=nikhil")
cur = conn.cursor()
# cur.execute('''
#     CREATE TABLE  dept( 
#         dept NUMERIC(4) PRIMARY KEY NOT NULL, 
#         dname VARCHAR (50) NOT NULL,
#         location VARCHAR (50) NOT NULL
#     );
# ''')
# a='''insert into emp values (7369,'SMITH','CLERK',7902,800,0.00,20);
# insert into emp values (7499,'ALLEN','SALESMAN',7698,1600,300,30);
# insert into emp values (7521,'WARD','SALESMAN',7698,1500,500,30);
# insert into emp values (7566,'JONES','MANAGER',7839,2975,null,20);
# insert into emp values (7698,'BLAKE','MANAGER',7839,2850,null,30);
# insert into emp values (7782,'CLARK','MANAGER',7839,2450,null,10);
# insert into emp values (7788,'SCOTT','ANALYST',7566,3000,null,20);
# insert into emp values (7839,'KING','PRESIDENT',null,5000,0,10);
# insert into emp values (7844,'TURNER','SALESMAN',7698,1500,0,30);
# insert into emp values (7876,'ADAMS','CLERK',7788,1100,null,20);
# insert into emp values (7900,'JAMES','CLERK',7698,950,null,30);
# insert into emp values (7934,'MILLER','CLERK',7782,1300,null,10);
# insert into emp values (7902,'FORD','ANALYST',7566,3000,null,20);
# insert into emp values (7654,'MARTIN','SALESMAN',7698,1250,1400,30);'''.split(';')
# # print(a)
# for i in a:
#     if i:
#         cur.execute(i)
def op(i):
    for x in i:
        print(x)
cur.execute('''select *  from emp    left join dept on "emp.deptno"="dept.deptno"  ''')
op(cur.fetchall())


conn.commit()