// Department maintains student information. The file contains roll no, name, division, and address. Allow user to add, delete information of student. display information of particular student. If record of student does not exits an approprite message is diaplayed . If it is then the system displays the student details. use reuirmental file to maintain the data.

#include<iostream>
#include <fstream>
using namespace std;

 class Student{
    public :
    int rno;
    char name[30], address[50];
    char div;


    void setdata(){
        cout<< "\n Enter the name of student = ";
        cin >>name;
        cout << "\n Enter the roll no of student = ";
        cin >>rno;
        cout << "\n Enter the division of student = ";
        cin >> div;

        cout<< "\n Enter the addresss of student = ";
        cin >> address;

    }

    void getdata(){
        cout << "\n Name = " <<name;
        cout <<"\n Roll no = "<<rno;
        cout << "\n Division = "<<div;
        cout << "\n Address = "<<address;

    }

    int getRollNo(){
        return rno;
    }
};

void writedata(){
    ofstream fout;
    fout.open("student.txt" , ios::binary | ios::app );
    Student s;
    s.setdata();
    fout.write((char*)&s, sizeof(s));

    fout.close();
}

void displayfile(){
    ifstream fin;
    fin.open("student.txt", ios :: binary);
    Student s;

    while(fin.read((char*)&s, sizeof(s))){
        s.getdata();
    }

    fin.close();
    cout<<"\n\n";
}

void searchdata(int key){
    ifstream fin;
    fin.open("student.txt", ios::binary);
    Student s;

    int flag=0;
    while(fin.read((char*)&s, sizeof(s))){
        if(s.getRollNo()==key){
            s.getdata();
            flag=1;
            break;
        }
    }

    if(flag==0){
        cout<< " \n Data not found ";
    }
}

void deletedata(int key){
    ifstream fin;
    fin.open("student.txt", ios::binary);
    ofstream fout;
    fout.open("temp.txt", ios::out | ios::binary);
    Student s;
    int flag=0;
    while(fin.read((char*)&s, sizeof(s))){
        if(s.getRollNo()!= key){
            fout.write((char*)&s, sizeof(s));
            flag=1;
        }
    }

    if(flag==0)
    cout << "\n Data not found : ";
    fin.close();
    fout.close();
    remove("student.txt");
    rename("temp.txt", "student.txt");
}

int main(){
    int ch;
    do{
        cout<<"\n\n";
        cout<<"\n1.Write\n2.Display\n3.Search\n4.Delete\n5.Exit\n";
        cout<< "\n Enter your choices = ";
        cin >>ch;

        switch(ch){
            case 1 :
            writedata();
            break;

            case 2 :
            displayfile();
            break;

            case 3 :
            int key;
            cout <<"\n Enter the roll no to be searched = ";
            cin >>key;
            searchdata(key);
            break;

            case 4 :
            int val;
            cout << "\n Enter the roll no to be deleted = ";
            cin >>val;
            deletedata(val);
            break;

            case 5 :
            cout << "\n Exited ";
            exit(0);
            
        }
    } while(ch <=5);
    return 0;
}

