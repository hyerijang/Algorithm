#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

class Student
{
public:
    string name;
    int score;
    Student(string name, int score)
    {
        this->name = name;
        this->score = score;
    }
    bool operator<(Student &student)
    {
        return this->score < student.score;
    }
    bool operator>(Student &student)
    {
        return this->score > student.score;
    }
};

bool compare(pair<string, pair<int, int>> a, pair<string, pair<int, int>> b)
{
    if (a.second.first == b.second.first)
        return a.second.second < b.second.second;
    return a.second.first > b.second.first;
};

int main(void)
{

    Student students[] = {Student("김나나", 90),
                          Student("김가가", 93),
                          Student("에웅", 97),
                          Student("롬람롬", 80),
                          Student("최바나나", 90)};
    sort(students, students + 5);
    for (int i = 0; i < 5; i++)
    {
        cout << students[i].score << students[i].name << endl;
    }
    cout << endl;

    vector<pair<string, pair<int, int>>> v; // int, string 으로 묶어서 사용
    v.push_back(pair<string, pair<int, int>>("모모", make_pair(97, 17)));
    v.push_back(pair<string, pair<int, int>>("영희", make_pair(90, 22)));
    v.push_back(pair<string, pair<int, int>>("철수", make_pair(90, 15)));
    v.push_back(pair<string, pair<int, int>>("유유", make_pair(96, 32)));

    sort(v.begin(), v.end(), compare);
    for (int i = 0; i < v.size(); i++)
    {
        cout << v[i].first << ":" << v[i].second.first << " " << v[i].second.second << endl;
    }
}