#include<stdio.h>
#include<string.h> 
#include <stdlib.h>

// char* transtime(char *time,int x);


int main(){
    FILE *fp1,*fp2;
    char buf[50];
    char tmp[40];
    char time_in[6];
    char describe[40];
    char out[6];
    char minutes[6];
    char seconds[6];
    int m,s,t,x;
    printf("สฃำเร๋สý:\n");
    scanf("%d",&x);
    fp1=fopen("timeline.txt","r");
    fp2=fopen("timeline_out.txt","w");
    if(!fp1){
        printf("can't open file1\n");
    }
    if(!fp2){
        printf("can't open file2\n");
    }
    while(fgets(buf, sizeof(buf), fp1))
    {
        strcpy(time_in,strtok(buf," "));
        strcpy(describe,strtok(NULL," "));
        // printf("%s\n",time_in,describe);

        strcpy(minutes,strtok(time_in,":"));
        strcpy(seconds,strtok(NULL,":"));
        m=atoi(minutes);
        s=atoi(seconds);
        // printf("%d %d\n",m,s);

        memset(minutes,0,sizeof(minutes)/sizeof(char));
        memset(seconds,0,sizeof(seconds)/sizeof(char));
        t=(m*60+s)-(90-x);
        m=t/60;
        s=t%60;
        itoa(m,minutes,10);
        strcat(minutes,":");
        itoa(s,seconds,10);
        // printf("%s %s\n",minutes,seconds);
        if(s<0)break;
        strcpy(out,strcat(minutes, seconds));
        printf("%s %s",out,describe);
        fprintf(fp2,"%s %s",out,describe);
    }
    fclose(fp1);
    fclose(fp2);
    return 0;
}
