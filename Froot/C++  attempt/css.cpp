#include <iostream> //cout
#include <vector>   //vector    
#include <fstream>  //files
#include <string>   //strings
#include <utility>  //pair
using namespace std;

enum color {
    A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,Y,Z,AA,BB,CC,DD,
    EE,FF,GG,HH,II,JJ,KK,LL,MM,NN,OO,PP,QQ,RR,SS,TT,UU,VV,WW,XX,YY,ZZ
};

struct Corte{
    string name;
    short x, y, n;
    Corte(short x, short y, short n, string name) : 
        x(x), y(y), n(n), name(name){};
    void print(){
        cout << name << " " << x << " " << y << " " << n << endl;
    }
};

vector<string> splitString(string line){
    size_t pos = 0;
    vector<string>tokens;
    while ((pos = line.find(" ")) != string::npos) {
        tokens.push_back(line.substr(0, pos));
        line.erase(0, pos + 1);
    }
    tokens.push_back(line);
    return tokens;
}

//TO-DO: make sure the file is clean - this was boring
int openFile(string namefile, short &n,pair <short, short> &m, vector<Corte*> &c){
    string line;
    vector<string> temp;

    ifstream inFile (namefile);
    if (inFile.is_open()){
        //get medidas
        getline (inFile,line); temp = splitString(line);
        m.first = atoi(temp[0].c_str()); m.second = atoi(temp[0].c_str());

        //get n tablas
        getline (inFile,line);
        n = atoi(line.c_str());

        //add cortes to the vector
        while (getline (inFile,line)){
            temp = splitString(line);
            c.push_back(new Corte(atoi(temp[1].c_str()),atoi(temp[2].c_str()),atoi(temp[3].c_str()), temp[0].c_str()));
        }
        //test >>
        for(int i = 0; i < c.size(); i++)
            c[i]->print();
    
        inFile.close();
        return 1;
    }
    return 0;
}

int atempt(){
}

int main(){
    short planchas;

    pair <short, short> medidas;
    vector<Corte*> cortes;
    openFile("test", planchas, medidas, cortes); 
    return 0;
}