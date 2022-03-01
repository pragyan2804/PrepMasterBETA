import tkinter as tk
import mysql.connector as mysql

def result():
    root = tk.Tk()
    root.geometry('1280x720')
    root.title('RESULTS')
    root.resizable(False, False)
    root.config(bg='#0073FF')
    root.eval('tk::PlaceWindow . center')
    mycon = mysql.connect(host='localhost', user='root', passwd='dhruv_789_$1', database='prepmaster')
    mycursor = mycon.cursor()
    mycursor.execute('select * from student_record;')
    fetch_data_response = mycursor.fetchall()
    label_heading = tk.Label(root,
                        text= 'RESULTS',
                        justify='center',
                        font='BurbankBigCondensed-Bold 70',
                        bg='#0073FF',
                        fg='white',
                        borderwidth=0).place(x=400, y=10, width=500, height=100)

    label_recs = tk.Label(root,
                    text= 'RECOMMENDATIONS',
                    justify= 'center',
                    font= 'BurbankBigCondensed-Bold 30',
                    bg= '#0073FF',
                    fg= 'black',
                    borderwidth=3, width=10, relief='raised').place(x=450, y=500, width=350, height=80)

    label_attempt= tk.Label(root,
                    text= 'MARKS OBTAINED',
                    justify= 'center',
                    font= 'BurbankBigCondensed-Bold 25',
                    bg= '#0073FF',
                    fg= 'black',
                    borderwidth=0).place(x=6, y=100, width=300, height= 100)

    label_attempt_= tk.Label(root,
                    text= fetch_data_response[0][0],
                    justify= 'center',
                    font= 'BurbankBigCondensed-Bold 25',
                    bg= '#0073FF',
                    fg= 'black',
                    borderwidth=0).place(x=6, y=200, width=300, height= 100)

    label_cor_response= tk.Label(root,
                    text= 'TOTAL CORRECT RESPONSES',
                    justify= 'center',
                    font= 'BurbankBigCondensed-Bold 25',
                    bg= '#0073FF',
                    fg= 'black',
                    borderwidth=0).place(x=510, y=100, width=300, height= 100)

    label_cor_response_ = tk.Label(root,
                    text= fetch_data_response[0][1],
                    justify= 'center',
                    font= 'BurbankBigCondensed-Bold 25',
                    bg= '#0073FF',
                    fg= 'black',
                    borderwidth=0).place(x=510, y=200, width=300, height= 100)

    label_wrong_responses= tk.Label(root,
                    text= 'TOTAL INCORRECT RESPONSES',
                    justify= 'center',
                    font= 'BurbankBigCondensed-Bold 25',
                    bg= '#0073FF',
                    fg= 'black',
                    borderwidth=0).place(x=980, y=100, width=300, height= 100)

    label_wrong_responses= tk.Label(root,
                    text= fetch_data_response[0][2],
                    justify= 'center',
                    font= 'BurbankBigCondensed-Bold 25',
                    bg= '#0073FF',
                    fg= 'black',
                    borderwidth=0).place(x=980, y=200, width=300, height= 100)

    root.mainloop()
result()