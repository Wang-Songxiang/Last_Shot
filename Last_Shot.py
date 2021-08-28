import sys

with open("config.txt", "r", encoding="utf-8") as f1:
    t = int(f1.readline().strip("剩余时间(秒):"))

with open("timeline.txt", "r", encoding="utf-8") as f2:
    with open("timeline_out.txt", "w", encoding="utf-8") as f3:
        f3.write("剩余时间为"+str(t)+"秒\n")
        minutes=int(t/60)
        seconds=t%60
        if seconds<10:
            seconds='0'+str(seconds)
        f3.write(str(minutes)+':'+str(seconds)+" 战斗开始\n")
        line = f2.readlines()
        for i in range(len(line)):
            line[i] = line[i].replace('　',' ')
            line[i] = line[i].replace('\n',' ')
            line[i]=line[i].split(" ")
            if line[i][0][0].isdigit()==False:
                for j in range(len(line[i])):
                    f3.write(line[i][j]+" ")
                f3.write('\n')
                continue
            if line[i][0].find(':', 0, len(line[i][0]))>0:
                m,s=line[i][0].strip().split(':')
                time=(int(m)*60+int(s))-(90-t)
                m=int(time/60)
                s=time%60
                if time<0:
                    sys.exit(0)
                if(s<10):
                    s='0'+str(s)
                line[i][0]=str(m)+':'+str(s)
            else:
                if len(line[i][0])==3:
                    time=(int(line[i][0][0])*60+int(line[i][0][1])*10+int(line[i][0][2]))-(90-t)
                else:
                    time=int(line[i][0])-(90-t)
                    if time<0:
                        sys.exit(0)
                if time>60:
                    if time-60<10:
                        time="0"+str(time-60)
                    else:
                        time=str(time-60)
                    time="1"+time
                line[i][0]=str(time)
            for j in range(len(line[i])):
                f3.write(line[i][j]+" ")
            f3.write('\n')