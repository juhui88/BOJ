#include <iostream>
#include <vector>
using namespace std;

class Player {
	int bornNum;
	int playerNum;
	int score;
public:
	void set_Info(int bornNum, int playerNum, int score) {
		this->bornNum = bornNum;
		this->playerNum = playerNum;
		this->score = score;
	}
	int get_bornNum() {
		return bornNum;
	}
	int get_playerNum() {
		return playerNum;
	}
	int get_score() {
		return score;
	}
	void show_Info() {
		cout << bornNum << " " << playerNum << endl;
	}
};


int main() {
	int n;
	cin >> n ;

	Player player[100];

	for (int i = 0; i < n; i++)
	{
		int bornNum, playerNum, score;
		cin >> bornNum >> playerNum >> score;
		player[i].set_Info(bornNum, playerNum, score);
	}

	int max1=0, max2=0, max3=0;
	int first, second, third;
	int tmp = 0;

	for (int i = 0; i < n; i++)
	{
		tmp = player[i].get_score();
		if (tmp > max1)
		{
			max1 = player[i].get_score();
			first = i;
		}
	}

	player[first].show_Info();

	tmp = 0;
	for (int i = 0; i < n; i++)
	{
		if (i != first)
		{
			tmp = player[i].get_score();
			if ( tmp > max2)
			{
				max2 = player[i].get_score();
				second = i;
			}
		}
	}

	player[second].show_Info();

	tmp = 0;
	for (int i = 0; i < n; i++)
	{
		tmp = player[i].get_score();
		if (i != first && i != second)
		{
			if (player[first].get_bornNum() == player[second].get_bornNum())
			{
				if (player[i].get_bornNum() != player[first].get_bornNum())
				{
					if ( tmp > max3)
					{
						max3 = player[i].get_score();
						third = i;
					}
				}
			}
			else
			{
				if (tmp > max3)
				{
					max3 = player[i].get_score();
					third = i;
				}
			}
				
		}
	}

	player[third].show_Info();
}