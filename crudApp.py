'''
1. Insert
2. Read all
3. Read Data by ID
4. Update
5. Exit
'''

import DBUtil as db


while True:
    print('\n1.Insert    2.Read all    3.Read Data by ID    4.Update    5.Delete    6.Exit')
    ch=int(input('Enter choice-->'))

    if ch==1:
        c_name=input('Enter course name: ')
        c_desc=input('Enter course description: ')
        c_dur=input('Enter course duration: ')
        db.insert_data(c_name, c_desc, c_dur)  

    elif ch==2:
        db.view_data()

    elif ch==3:
        c_id=int(input('Enter course ID: '))
        db.get_by_cid(c_id)  

    elif ch==4:
        cid=int(input('Enter course ID: '))
        isExists = db.get_by_cid(cid)
        if isExists:
            c_name=input('Enter course name: ')
            c_desc=input('Enter course description: ')
            c_dur=input('Enter course duration: ')

            db.update_data(cid, c_name, c_desc, c_dur )

    elif ch==5:
        cid=int(input('Enter course ID: '))
        isExists = db.get_by_cid(cid)
        if isExists:
            db.delete_data(cid )

    elif ch==6:
        print('Thanks for using our app!')
        break

    else:
        print('invalid choice!')

    

    
