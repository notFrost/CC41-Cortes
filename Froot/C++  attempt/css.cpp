#include <iostream> //cout
#include <vector>   //vector    
#include <fstream>  //files
#include <string>   //strings
#include <utility>  //pair
using namespace std;

enum color {
    A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,w,h,Z,AA,BB,CC,DD,
    EE,FF,GG,HH,II,JJ,KK,LL,MM,NN,OO,PP,QQ,RR,SS,TT,UU,VV,WW,YY,XX,ZZ
};

struct Corte{
    //name, w=ancho, h=alto, n = ammount of cortes
    string name;
    short w, h, n;
    short x, y;
    Corte(short w, short h, short n, string name) : 
        w(w), h(h), n(n), name(name){};
    void print(){
        cout << name << " " << w << " " << h << " " << n << endl;
    }
    void cut(short x, short y){
        this->x = x; 
        this->y=y;
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
        /*test >>
        for(int i = 0; i < c.size(); i++)
            c[i]->print();
    */
        inFile.close();
        return 1;
    }
    return 0;
}

bool compareWidth(Corte* a, Corte* b) { 
    return (a->w > b->w); 
} 
bool compareHeight(Corte* a, Corte* b) { 
    return (a->h > b->h); 
} 
bool compareArea(Corte* a, Corte* b) { 
    return (a->w * a->h > b->w * b->h); 
} 
//order bh width
void order(vector<Corte*> &c){
    sort(c.begin(), c.end(), compareWidth);
}

int area(vector<Corte*> &c){
    short area = 0;
    for(short i = 0; i < c.size(); i++){
        area += c[i]->w * c[i]->h * c[i]->n;
        cout << endl<<c[i]->w <<" "<< c[i]->h<<" "<< c[i]->w * c[i]->h<<endl;
    }
    return area;
}

//cortando una pieza
//how do hou keep track?


int main(){
    short planchas;
    pair <short, short> medidas;
    vector<Corte*> cortes; 
    openFile("test", planchas, medidas, cortes); 
    order(cortes);
    cout << medidas.first*medidas.second<<endl;
    cout << endl<< area(cortes) <<endl;
    /*for(short i = 0; i < cortes.size(); i++)
        cortes[i]->print();*/
    cut();
    return 0;
}