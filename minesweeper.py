import mysql.connector as sqltor
import random as r
mycon=sqltor.connect(host='localhost',user='root',password='root')
c1=mycon.cursor()
def load():
     for i in range(0,25):
          for j in range(0,int(10E5)+1):
               if j==10E5:
                    print('■',end='')
     print()
#loading bar:
print('\n'*10)
print("""
                ███╗   ███╗██╗███╗   ██╗███████╗███████╗██╗    ██╗███████╗███████╗██████╗ ███████╗██████╗ 
                ████╗ ████║██║████╗  ██║██╔════╝██╔════╝██║    ██║██╔════╝██╔════╝██╔══██╗██╔════╝██╔══██╗
                ██╔████╔██║██║██╔██╗ ██║█████╗  ███████╗██║ █╗ ██║█████╗  █████╗  ██████╔╝█████╗  ██████╔╝
                ██║╚██╔╝██║██║██║╚██╗██║██╔══╝  ╚════██║██║███╗██║██╔══╝  ██╔══╝  ██╔═══╝ ██╔══╝  ██╔══██╗
                ██║ ╚═╝ ██║██║██║ ╚████║███████╗███████║╚███╔███╔╝███████╗███████╗██║     ███████╗██║  ██║
                ╚═╝     ╚═╝╚═╝╚═╝  ╚═══╝╚══════╝╚══════╝ ╚══╝╚══╝ ╚══════╝╚══════╝╚═╝     ╚══════╝╚═╝  ╚═╝
                                                                                          
""")
print("\n"*14)
print(" "*45,end='')
load()
print('\n'*32)
print("Welcome to minesweeper!")
c1.execute("show databases")
datbase=c1.fetchall()
if ('minesweeper',) not in datbase:
     c1.execute("Create database minesweeper")
     c1.execute("commit")
     c1.execute("use minesweeper")
     c1.execute("create table login(username varchar(20), password varchar(8))")
     c1.execute("commit")
     c1.execute("create table easyleaderboard(username varchar(20), gametime int)")
     c1.execute("commit")
     c1.execute("create table mediumleaderboard(username varchar(20), gametime int)")
     c1.execute("commit")
     c1.execute("create table hardleaderboard(username varchar(20), gametime int)")
     c1.execute("commit")
     c1.execute("create table extremeleaderboard(username varchar(20), gametime int)")
     c1.execute("commit")
c1.execute("use minesweeper")
c1.execute('select * from login')
data=c1.fetchall()

while True:
    ans=input('new user?(y/n):')

    if ans=='y':
        username=input('enter username (upto 20 characters):')
        for i in range(0,len(data)):
            m=data[i][0]
            if m.lower()==username.lower():
                print('username taken already,please try again')
                break
        else:
            password=input('enter your password( upto 8 characters ):')
            c1.execute("insert into login values('{}','{}')".format(username,password))
            c1.execute('commit')
            print('username and password successfully registered')
            c1.execute("create table {}(savename varchar(20),hiddencells text,minecells text,displayedcells text,flagcells text,gametime int,rowlen int)".format(username))
            break
    elif ans=='n':
        username=input('enter username(case sensitive):')
        password=input('enter your password(case sensitive):')
        if (username,password) in data:
            print('welcome')
            break
        else:
            print('incorrect username or password, please try again')


#mechanism to add 1 for each mine nearby
def ad1(a,b,c,d='c',e='c',f='c',g='c',h='c',i='c'):
    lelements=[a,b,c,d,e,f,g,h,i]
    for j in lelements:
        if j=='c':
            continue
        if minenear[j-1]!='f':
            minenear[j-1]+=1

def showcell(a='c',b='c',c='c',d='c',e='c',f='c',g='c',h='c',i='c'):
    lelements=[a,b,c,d,e,f,g,h,i]
    for j in lelements:
        if j!='c':
            if minenear[j-1]!='f'and j not in displayedcells and j not in flagcells:
                if j in hiddencells and j not in flagcells:
                    displayedcells.append(j)
                    hiddencells.remove(j)
                    selectzerocells(j)


def selectzerocells(showncell):
    if minenear[showncell-1]==0:
        if showncell==rowlen:#top right corner
            showcell(showncell-1,showncell+rowlen,showncell+rowlen-1)
            
        elif showncell==celltotal:#bottom right corner
            showcell(showncell-1,showncell-rowlen,showncell-rowlen-1)
            
        elif showncell==1:#top left corner
            showcell(showncell+1,showncell+rowlen,showncell+rowlen+1)
            
        elif showncell==celltotal-rowlen+1:#bottom left corner
            showcell(showncell+1,showncell-rowlen,showncell-rowlen+1)
            
        elif 1<showncell<rowlen:#top row
            showcell(showncell-1,showncell+1,showncell+rowlen-1,showncell+rowlen,showncell+rowlen+1)
            
        elif celltotal-rowlen+1<showncell<celltotal:#bottom row
            showcell(showncell+1,showncell-rowlen,showncell-rowlen+1,showncell-rowlen-1,showncell-1)
            
        elif showncell%rowlen==0:#right edge
            showcell(showncell-1,showncell-rowlen,showncell-rowlen-1,showncell+rowlen-1,showncell+rowlen)
            
        elif (showncell-1)%rowlen==0:#left edge
            showcell(showncell+1,showncell-rowlen,showncell-rowlen+1,showncell+rowlen+1,showncell+rowlen)
            
        else:#anywhere else(middle positions)
            showcell(showncell-rowlen-1,showncell-rowlen,showncell-rowlen+1,showncell-1,showncell+1,showncell+rowlen-1,showncell+rowlen,showncell+rowlen+1)
    
def showboard():
    print('   '+'̲',end='')
    for i in range(1,rowlen+1):
        if i!=rowlen:
            if i<10:
                print(str(i)+'̲'+' '+'̲',end='')
        else:
            if i<10:
                print(str(i),end='')
    if rowlen<=10:
        print('---->x')
    else:
        #length of top row: rowlen*2-1
        #18 spaces covered by numbers
        toprowlength=rowlen*2-1
        topnumberlength=18
        for i in range(1,toprowlength-topnumberlength):
            print('-̲',end='')
        print('->x')

    
    for i in range(rowlen):
        if i<9:
            print(str(i+1)+' ',end='')
            print('|',end='')
        else:
            print(i+1,end='')
            print('|',end='')
        for j in range(1,rowlen+1):
            cellno=rowlen*i+j
            if cellno in hiddencells:
                print("■",end=' ')
            if cellno in displayedcells:
                if minenear[cellno-1]=='f':
                    print('✶',end=' ')
                else:
                    print(minenear[cellno-1],end=' ')
            if cellno in flagcells:
                print("▲",end=' ')
        print()
    print('|')
    print('|')
    print('˅')
    print('y')

#is it a saved game?
while True:
    dec2=input('''What do you want to do?
1->Load a saved game
2->Show leaderboard
3->Start a new game
4->Show rules
5->Exit
''')
    if dec2 not in ['1','2','3','4','5']:
         print('Enter a valid option')
         continue
    if dec2=='4':
         print("""
════════════════════════════════════════════════════════════════════════════════
                                 MINESWEEPER RULES
════════════════════════════════════════════════════════════════════════════════

OBJECTIVE:
Reveal all the safe cells on the board without opening any mines.
If you open a mine (✶), you lose the game immediately.

────────────────────────────────────────────────────────────────────────────────
HOW THE GAME WORKS:

The board is made up of hidden cells arranged in a grid.  
Some of them hide mines, others are safe.

When you reveal a safe cell, it shows a number (0–8) that tells you
how many mines are hidden in the 8 cells around it.

Use logic to figure out which cells are safe, and mark dangerous ones with a flag (▲).

────────────────────────────────────────────────────────────────────────────────
BOARD EXAMPLES

🔹 When you start, every cell is hidden:

     1  2  3  4   → x (horizontal)
  1 | ■  ■  ■  ■
  2 | ■  ■  ■  ■
  3 | ■  ■  ■  ■
  4 | ■  ■  ■  ■
    |
    ↓
    y (vertical)

Each ■ is a hidden cell. You’ll choose which cell to reveal or flag by its coordinates.

────────────────────────────────────────────────────────────────────────────────
After a few moves, the board might look like this:

     1  2  3  4
  1 | 1  1  ■  ■
  2 | 1  ▲  2  ■
  3 | 0  1  2  1
  4 | 0  0  0  0

Here’s what you’re seeing:
- Numbers (1, 2, etc.) show how many mines are nearby.
- ▲ means you marked a suspected mine.
- ■ are still hidden cells.
- 0 means there are no mines around that cell — so it’s safe.

────────────────────────────────────────────────────────────────────────────────
SYMBOL GUIDE:

| Symbol | Meaning |
|---------|----------|
| ■ | Hidden cell (not opened yet) |
| ▲ | Flag – you think there’s a mine here |
| ✶ | Mine (revealed only if you lose) |
| 0–8 | Number of mines near this cell |

────────────────────────────────────────────────────────────────────────────────
DIFFICULTY LEVELS:

When starting a new game, choose one of these:

   1. Easy    → 4×4 grid, 5 mines  
   2. Medium  → 9×9 grid, 20 mines  
   3. Hard    → 13×13 grid, 43 mines  
   4. Extreme → 20×20 grid, 133 mines

────────────────────────────────────────────────────────────────────────────────
COMMANDS DURING THE GAME:

Type these commands when playing:

  • help → Show all available commands  
  • m    → Mark a cell with a flag (▲)  
  • d    → Remove a flag from a cell  
  • r    → Reveal (open) a cell  
  • s    → Save your current game  
  • q    → Quit (you can choose to save before quitting)  
  • b    → Go back / cancel an action

────────────────────────────────────────────────────────────────────────────────
ENTERING COORDINATES:

Cells are selected using coordinates written as (x, y)

Example:
  Enter x coordinate, y coordinate of the cell to reveal:
  (2, 3)

This means:
- Move 2 steps right (x = 2)
- Move 3 steps down (y = 3)
That’s the cell you’re selecting.

────────────────────────────────────────────────────────────────────────────────
REVEALING CELLS:

- If it’s safe, the cell shows a number (0–8).  
- If the number is 0, the game automatically opens all nearby cells.  
- If it’s a mine (✶), the game ends immediately.

────────────────────────────────────────────────────────────────────────────────
FLAGGING CELLS:

If you suspect a cell hides a mine:
→ Use the `m` command to mark it with a flag (▲)

To remove the flag:
→ Use the `d` command.

────────────────────────────────────────────────────────────────────────────────
WINNING THE GAME:

You win when:
 -Every mine is correctly flagged (▲)  
 -Every safe cell is revealed.

Once you win, the game automatically reveals the full board.

────────────────────────────────────────────────────────────────────────────────
SAVING & LOADING:

You can save your game using `s` anytime.
Later, load it from the main menu to continue where you left off.
Leaderboards show your best times for each difficulty.

────────────────────────────────────────────────────────────────────────────────
""")
         continue

    if dec2=='5':
        print('Thank you for playing')
        break
    if dec2=='1':
        savedgame=True
        c1.execute("select savename from {}".format(username))
        b=c1.fetchall()
        if len(b)==0:
            print("You havent saved any game yet")
            continue
        else:
            print("Your saved games:")
            for i in b:
                print(i[0])
        while True:
            savename=input('Enter the name of your saved game:')
            savedgame=True
            c1.execute("select savename from {}".format(username))
            b=c1.fetchall()
            try:
                if savename not in b[0]:
                    print('Please enter a valid savename')
                else:
                    valid=True
                    break
            except IndexError:
                print('Please enter a valid savename')
                continue
            if valid==True:
                break
    elif dec2=='2':
        while True:
            mode=input("Enter the difficulty mode for which you want to see the leaderboard:")
            if mode not in ['easy','medium','hard','extreme']:
                print('Enter a valid option')
                continue
            else:
                break        
        
        table_name = mode + 'leaderboard'
        cursor = mycon.cursor()
        
        # Fetch data sorted by gametime ascending (fastest first)
        cursor.execute("SELECT username, gametime FROM {} ORDER BY gametime ASC".format(table_name))
        data = cursor.fetchall()
        usernames=[]
        times=[]
        for i in data:
            usernames.append(i[0])
            times.append(i[1])
        # Print table header
        print()
        print("| Rank |       Username       | Time (hh:mm:ss) |")
        print("|" + "-"*6 + "|" + "-"*22 + "|" + "-"*17 + "|")
        
        # Print leaderboard rows
        for i in range(len(usernames)):
            time=times[i]
            user=usernames[i]
            hours = time // 3600
            minutes = (time % 3600) // 60
            seconds = time % 60
            if len(str(hours))==1:
                hours='0'+str(hours)
            if len(str(minutes))==1:
                minutes='0'+str(minutes)
            if len(str(seconds))==1:
                seconds='0'+str(seconds)
            
            if i in range(0,9):
                print('|  {}   | '.format(i+1)+user+' '*(21-len(user))+'|    {}:{}:{}     |'.format(hours,minutes,seconds))
            else:
                print('|  {}  | '.format(i+1)+user+' '*(21-len(user))+'|    {}:{}:{}     |'.format(hours,minutes,seconds))
        
        print()
        continue

    else:
        savedgame=False
        savedgamefirstturn=0

    #loading a saved game
    if savedgame==True:
        c1.execute("select * from {} where savename='{}'".format(username,savename))
        b=c1.fetchall()
        print(b)
        hiddencells=eval(b[0][1])
        minecells=eval(b[0][2])
        displayedcells=eval(b[0][3])
        flagcells=eval(b[0][4])
        prelapsedtime=int(b[0][5])
        rowlen=int(b[0][6])
        mode_map={4: 1, 9: 2, 13: 3, 20: 4}
        mode=mode_map[rowlen]
        print(hiddencells)
        savedgamefirstturn=1

    #removing all other instances of the game
    if savedgame==True:
        print("\nDon't forget to save your game again! Or else you cant recover this game\n")
        c1.execute("delete from {} where savename='{}'".format(username,savename))

    if savedgame!=True:
        while True:
            try:
                mode=int(input('''Select the difficulty:
1-Easy
2-Medium
3-Hard
4-Extreme
'''))
            except NameError:
                print('Enter valid difficulty')
                continue
            except TypeError:
                print('Enter valid difficulty')
                continue
            except SyntaxError:
                print('Enter valid difficulty')
                continue
            except ValueError:
                print('Enter valid difficulty')
                continue
            if mode not in [1,2,3,4]:
                print('Enter a valid option')
                continue
            else:
                break
        lengthlist=[4,9,13,20]
        modelist=[1,2,3,4]
        minelist=[3,27,56,133]
        for i in modelist:
            if mode==i:
                rowlen=lengthlist[i-1]
        mineno=minelist[mode-1]
        minecells=[]

    celltotal=rowlen*rowlen

    if savedgame!=True:
        for i in range(mineno):
            while True:
                k=r.randint(1,celltotal)
                if k not in minecells:
                    minecells.append(k)
                    break

    #finding no of mines near each cell
    minenear=[]
    for i in range(celltotal):
        minenear.append(0)

    #mines are marked as f 
    for i in minecells:
        minenear[i-1]='f'
        
    

    #mechanism to calculate no of mines near each cell
    for i in minecells:
        if i==rowlen:#top right corner
            ad1(i-1,i+rowlen,i+rowlen-1)
            
        elif i==celltotal:#bottom right corner
            ad1(i-1,i-rowlen,i-rowlen-1)
            
        elif i==1:#top left corner
            ad1(i+1,i+rowlen,i+rowlen+1)
            
        elif i==celltotal-rowlen+1:#bottom left corner
            ad1(i+1,i-rowlen,i-rowlen+1)
            
        elif 1<i<rowlen:#top row
            ad1(i-1,i+1,i+rowlen-1,i+rowlen,i+rowlen+1)
            
        elif celltotal-rowlen+1<i<celltotal:#bottom row
            ad1(i+1,i-rowlen,i-rowlen+1,i-rowlen-1,i-1)
            
        elif i%rowlen==0:#right edge
            ad1(i-1,i-rowlen,i-rowlen-1,i+rowlen-1,i+rowlen)
            
        elif (i-1)%rowlen==0:#left edge
            ad1(i+1,i-rowlen,i-rowlen+1,i+rowlen+1,i+rowlen)
            
        else:#anywhere else(middle positions)
            ad1(i-rowlen-1,i-rowlen,i-rowlen+1,i-1,i+1,i+rowlen-1,i+rowlen,i+rowlen+1)

    #print(minenear) #these 2 lines display the answers to the game
    #print(minecells)



    if savedgame!=True:
        hiddencells=[]
        displayedcells=[]
        flagcells=[]
        for i in range(rowlen*rowlen):
            hiddencells.append(i+1)

    gameresult=''

    if savedgame!=True:
        firstturn=1
    else:
        firstturn=0

    #getting the game start time
    c1.execute('select now()')
    a=c1.fetchall()
    x=list(a[0])
    starttime=x[0]
    c1.execute('commit')

    while True:
        if firstturn!=1:
            if savedgamefirstturn==1:
                showboard()
                savedgamefirstturn=0

                
            if set(flagcells)==set(minecells):
                print("YAY!!! You Won!!!!")
                print('\n')
                gameresult='won'
                break
        
            dec=input('''What do you want to do? Enter 'help' to access keywords
''')
            
            if dec=='help':
                print('''Enter m to mark mines
Enter d to delete marked mines
Enter r to reveal cells
Enter s to save the current state
Enter q to quit
Enter b to cancel an accidental action
■ : hidden cell
▲ : flagged mine
✶ : revealed mine
numbers : mines nearby
''')
                continue
            if dec=='m' or dec=='d':
                while True:
                    while True:
                        back=False
                        try:
                            if dec=='m':
                                lflag=input('''Enter x coordinate, y coordinate of the cell to be marked:
''')
                            if dec=='d':
                                lflag=input('''Enter x coordinate, y coordinate of the cell to be unmarked:
''')
                            if lflag=='b':
                                back=True
                                break
                            else:
                                lflag=eval(lflag)
                            flagcell=(lflag[1]-1)*rowlen+lflag[0]
                            if flagcell < 1 or flagcell > celltotal:
                                print('Enter valid coordinates')
                                continue
                            break
                        except NameError:
                            print('Enter valid coordinates')
                        except TypeError:
                            print('Enter valid coordinates')
                        except SyntaxError:
                            print('Enter valid coordinates')
                    if back==True:
                        break
                    if flagcell in displayedcells:
                        print('You cannot flag a displayed cell: try again')
                        continue
                    if flagcell in flagcells:
                        flagcells.remove(flagcell)
                        if flagcell not in hiddencells:
                            hiddencells.append(flagcell)
                        showboard()
                        break
                    if flagcell in hiddencells:
                        hiddencells.remove(flagcell)
                        flagcells.append(flagcell)
                        showboard()
                        break
                
            if dec=='r':
                back=False
                while True:
                    if firstturn!=1:
                        back=False
                        while True:
                            try:
                                a=input('''Enter x coordinate, y coordinate of the cell to select:
''')
                                if a=='b':
                                    back=True
                                    break
                                else:
                                    a=eval(a)
                                selectedcell=(a[1]-1)*rowlen+a[0]
                                if selectedcell < 1 or selectedcell > celltotal:
                                    print('Enter valid coordinates')
                                    continue
                                break
                            except NameError:
                                print('Enter valid coordinates')
                            except TypeError:
                                print('Enter valid coordinates')
                            except SyntaxError:
                                print('Enter valid coordinates')
                        if back==True:
                            break
                        if selectedcell in hiddencells:
                            break
                        else:
                            print('The cell you selected is already displayed. Please select a hidden cell.')
                
                if back==True:
                    continue
                hiddencells.remove(selectedcell)
                displayedcells.append(selectedcell)
                #showing cells with 0 mines nearby
                selectzerocells(selectedcell)
                showboard()
                for i in displayedcells:
                    if minenear[i-1]=='f':
                        print('You selected a mine! You lose!')
                        print()
                        gameresult='lost'
                        break
                if gameresult=='lost':
                    break

            if dec=='s':
                c1.execute('select sysdate()')
                b=c1.fetchall()
                y=list(b[0])
                endtime=y[0]
                overalltime=str(endtime-starttime)          
                print(overalltime)
                h=int(overalltime[0:1])
                m=int(overalltime[2:4])
                s=int(overalltime[5:7])
                gametime=3600*h+60*m+s
                if savedgame==True:
                    gametime+=prelapsedtime
                if savedgame!=True:
                    savename=input('Enter save name(up to 8 characters):')
                c1.execute("Commit")
                print('Saving game...')
                c1.execute("insert into {} values('{}','{}','{}','{}','{}',{},{})".format(username,savename,str(hiddencells),str(minecells),str(displayedcells),str(flagcells),gametime,rowlen))
                c1.execute('commit')
                load()
                break
            if dec=='q':
                print("Do you want to save your game? (y/n)")
                ca=input()
                if ca=='y':
                    c1.execute('select sysdate()')
                    b=c1.fetchall()
                    y=list(b[0])
                    endtime=y[0]
                    overalltime=str(endtime-starttime)          
                    print(overalltime)
                    h=int(overalltime[0:1])
                    m=int(overalltime[2:4])
                    s=int(overalltime[5:7])
                    gametime=3600*h+60*m+s
                    if savedgame==True:
                        gametime+=prelapsedtime
                    if savedgame!=True:
                        savename=input('Enter save name(up to 8 characters):')
                    c1.execute("Commit")
                    print('Saving game...')
                    c1.execute("insert into {} values('{}','{}','{}','{}','{}',{},{})".format(username,savename,str(hiddencells),str(minecells),str(displayedcells),str(flagcells),gametime,rowlen))
                    c1.execute('commit')
                    load()
                    break
                if ca=='n':
                    break               
                
            elif dec not in ['m','r','help','d','s','q','b']:
                print('Please enter a valid option')
                continue
        
        if firstturn==1:
            zerocells=[]
            a=1
            for i in minenear:
                if i==0:
                    zerocells.append(a)
                a+=1
            if len(zerocells)==0:
                b=1
                for i in minenear:
                    if i==1:
                        zerocells.append(b)
                    b+=1
            selectedcell=zerocells[r.randint(0,len(zerocells)-1)]     
            hiddencells.remove(selectedcell)
            displayedcells.append(selectedcell)
            #shwoing cells with 0 mines nearby
            selectzerocells(selectedcell)
            firstturn=0
            showboard()
            continue
    #time addition
    if gameresult=='won':
        c1.execute('select sysdate()')
        b=c1.fetchall()
        y=list(b[0])
        endtime=y[0]
        c1.execute('commit')
        overalltime=str(endtime-starttime)
        print(overalltime)
        h=int(overalltime[0:1])
        m=int(overalltime[2:4])
        s=int(overalltime[5:7])
        gametime=3600*h+60*m+s
        if savedgame==True:
            gametime+=prelapsedtime  
        print(gametime)   
        c1.execute('show tables')
        b=c1.fetchall()
        print(b)
        inserttime=''
        inserttime=str(h)+':'+str(m)+':'+str(s)
        stringmodes=['easy','medium','hard','extreme']
        c1.execute("insert into {} values('{}','{}')".format(stringmodes[mode-1]+'leaderboard',username,gametime))
        c1.execute('commit')


